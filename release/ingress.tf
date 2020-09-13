
resource "consul_config_entry" "ingress_gateway" {
  name = "ingress-gateway"
  kind = "ingress-gateway"

  config_json = jsonencode({
    Listeners = [{
      Port     = 8080
      Protocol = "http"
      Services = [{
        Name = var.service_name
        Hosts = "*"
      }]
    }]
  })
}

# Let the ingress reach the service
resource "consul_intention" "ingress" {
  source_name      = consul_config_entry.ingress_gateway.name
  destination_name = var.service_name
  action           = "allow"
  depends_on = [
    consul_config_entry.service-defaults
  ]
}

resource "consul_config_entry" "service-defaults" {
  name = var.service_name
  kind = "service-defaults"

  config_json = jsonencode({
    Protocol = "http"
  })
}
