resource "kubernetes_deployment" "deployment" {

  wait_for_rollout = false

  metadata {
    name = "${var.service_name}-deployment-v2"
    labels = {
      deployVersion = "2"
      app           = "site"
    }
    namespace = kubernetes_namespace.namespace.metadata.0.name
  }

  spec {
    replicas = var.replicas

    selector {
      match_labels = {
        deployVersion = "2"
        app           = "site"
      }
    }

    template {
      metadata {
        labels = {
          deployVersion       = "2"
          app                 = "site"
          service_config_hash = filemd5("${path.module}/service.hcl")
        }
      }

      spec {
        # Shared
        volume {
          name = "service-config"
          config_map {
            name = kubernetes_config_map.service-config.metadata.0.name
          }
        }

        volume {
          name = "consul-token"
          empty_dir {
            medium = "Memory"
          }
        }

        automount_service_account_token = true
        service_account_name            = kubernetes_service_account.service.metadata.0.name

        # Main App Container
        container {
          image = var.image
          name  = "app"

          resources {
            limits {
              cpu    = "0.25"
              memory = "512Mi"
            }
            requests {
              cpu    = "250m"
              memory = "50Mi"
            }
          }

          liveness_probe {
            http_get {
              path = "/"
              port = 80
            }

            initial_delay_seconds = 1
            period_seconds        = 300
          }
          
          env {
            name = "HOST_IP"
            value_from {
              field_ref {
                field_path = "status.hostIP"
              }
            }
          }
          
          env {
            name  = "CONSUL_HTTP_ADDR"
            value = "https://$(HOST_IP):8501"
          }

          env {
            name  = "CONSUL_HTTP_SSL_VERIFY"
            value = "false"
          }
          
          volume_mount {
            mount_path = "/consul/token/"
            name       = "consul-token"
          }
        
        }

        # Service registration
        container {
          # Local Build
          image_pull_policy = "Always"
          image             = "7imbrook/sidecar:prod"
          name              = "consul-agent"
          command           = ["register_service", "/consul/services/service.hcl"]

          port {
            container_port = 21000
            name           = "proxy"
          }

          lifecycle {
            pre_stop {
              exec {
                command = ["/bin/shutdown"]
              }
            }
          }

          resources {
            limits {
              cpu    = "0.25"
              memory = "512Mi"
            }
            requests {
              cpu    = "250m"
              memory = "50Mi"
            }
          }

          env {
            name = "HOST_IP"
            value_from {
              field_ref {
                field_path = "status.hostIP"
              }
            }
          }

          env {
            name = "POD_IP"
            value_from {
              field_ref {
                field_path = "status.podIP"
              }
            }
          }

          env {
            name  = "SERVICE_NAME"
            value = var.service_name
          }

          env {
            name  = "CONSUL_HTTP_ADDR"
            value = "https://$(HOST_IP):8501"
          }

          env {
            name  = "CONSUL_HTTP_SSL_VERIFY"
            value = "false"
          }
          
          env {
            name  = "DJANGO_SETTINGS_MODULE"
            value = "backend.settings.prerelease"
          }

          volume_mount {
            mount_path = "/consul/services/"
            name       = "service-config"
          }
          
          volume_mount {
            mount_path = "/consul/token/"
            name       = "consul-token"
          }
        }
      }
    }
  }
}

# Load service configuration
resource "kubernetes_config_map" "service-config" {
  metadata {
    name      = "service-config"
    namespace = kubernetes_namespace.namespace.metadata.0.name
  }

  data = {
    "service.hcl" = file("${path.module}/service.hcl")
  }
}

# None default service account
resource "kubernetes_service_account" "service" {
  metadata {
    name      = var.service_name
    namespace = kubernetes_namespace.namespace.metadata.0.name
  }
  automount_service_account_token = true
}

resource "kubernetes_namespace" "namespace" {
  metadata {
    name = var.namespace
  }
}