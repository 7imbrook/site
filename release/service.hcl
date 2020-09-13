service {
  id   = "${HOSTNAME}"
  name = "site"
  address = "${POD_IP}"

  check {
    id   = "http-check-${POD_IP}"
    name = "Basic Reachablity"
    http = "http://${POD_IP}:80/"
    interval = "10s"
    timeout  = "5s"
  }
}