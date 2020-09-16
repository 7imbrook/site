terraform {
  backend "consul" {
    address = "consul.timbrook.dev"
    scheme  = "https"
    path    = "terraform_states/django"
  }
}