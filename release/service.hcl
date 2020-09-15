services {
  name = "${SERVICE_NAME}"

  id   = "${HOSTNAME}"
  address = "${POD_IP}"

  check {
    id   = "http-check-${POD_IP}"
    name = "Basic Reachablity"
    http = "http://${POD_IP}:4000/info"
    interval = "10s"
    timeout  = "5s"
  }
}

# Need to use a different service block to register sidecar
# becasuse the agent expects is on localhost and not podip
services {
  id   = "${HOSTNAME}-sidecar-proxy"
  name = "${SERVICE_NAME}-sidecar-proxy"
  kind = "connect-proxy"

  address = "${POD_IP}"
  port    = 21000

  proxy {
    destination_service_name = "${SERVICE_NAME}"
    destination_service_id = "${HOSTNAME}"
    local_service_address = "127.0.0.1"
    local_service_port = 4000
  }

  checks {
    name = "Proxy Public Listener"
    tcp = "${POD_IP}:21000"
    interval = "10s"
    deregister_critical_service_after = "10m"
  }

  checks {
    name = "Destination Alias"
    alias_service = "${HOSTNAME}"
  }
}
