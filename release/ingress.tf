
resource "consul_config_entry" "ingress_gateway" {
  name = "ingress-sfo2"
  kind = "ingress-gateway"

  config_json = jsonencode({
    TLS = {
      Enabled = true
    }
    Listeners = [{
        Port = 443,
        Protocol = "http",
        Services = [
          {
            Name = "site"
            Hosts = [
                "timbrook.dev"
            ]
          }
        ]
    }]
  })
}

# # Let the ingress reach the service
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

# Route myself to my new deploy with secret header
resource "consul_config_entry" "service-router-site" {
  name = "site" # use existing ingresses via site, steal traffic
  kind = "service-router"

  config_json = jsonencode({
    Routes = [
      {
        Match = {
          HTTP = {
            QueryParam = [
              {
                Name  = "force-new"
                Exact = "1"
              },
            ]
          }
        }
        Destination = {
          Service       = "django"
        }
      }
    ]
  })
  
  depends_on = [
    consul_config_entry.service-defaults
  ]
}
