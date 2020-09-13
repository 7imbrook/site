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
          image   = "sidecar:latest"
          name    = "consul-agent"
          command = split(" ", "register_service /consul/services/service.hcl")

          lifecycle {
            pre_stop {
              exec {
                # command = split(" ", "consul services deregister -id $HOSTNAME")
                command =["/bin/sh", "-c", "consul services deregister -id $HOSTNAME"]
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
            value = "http://$(HOST_IP):8500"
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
