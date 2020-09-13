
resource "consul_config_entry" "ingress_gateway" {
  name = "ingress-gateway"
  kind = "ingress-gateway"

  config_json = jsonencode({
    Listeners = [{
      Port     = 8080
      Protocol = "tcp"
      Services = [{ Name = "nginx" }]
    }]
  })
}

# Let the ingress reach the service
resource "consul_intention" "ingress" {
  source_name      = consul_config_entry.ingress_gateway.name
  destination_name = "nginx"
  action           = "allow"
}