resource "kubernetes_deployment" "personal-site" {

  wait_for_rollout = false

  metadata {
    name = "personal-site-deployment-v2"
    labels = {
      deployVersion = "2"
      app           = "site"
    }
  }

  spec {
    replicas = 1

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

        automount_service_account_token = true
        service_account_name            = kubernetes_service_account.service.metadata.0.name

        # Main App Container
        container {
          image = "nginx:1.7.8"
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
        }

        # Service registration
        container {
          # Local Build
          image_pull_policy = "Never"
          image             = "7imbrook/sidecar:latest"
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
            name  = "CONSUL_HTTP_ADDR"
            value = "https://$(HOST_IP):8501"
          }

          env {
            name  = "CONSUL_HTTP_SSL_VERIFY"
            value = "false"
          }

          volume_mount {
            mount_path = "/consul/services/"
            name       = "service-config"
          }
        }
      }
    }
  }
}

# Load service configuration
resource "kubernetes_config_map" "service-config" {
  metadata {
    name = "service-config"
  }

  data = {
    "service.hcl" = file("${path.module}/service.hcl")
  }
}

# None default service account
resource "kubernetes_service_account" "service" {
  metadata {
    name = "nginx"
  }
  automount_service_account_token = true
}
