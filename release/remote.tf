terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "timbrook"

    workspaces {
      name = "personal-site"
    }
  }
}