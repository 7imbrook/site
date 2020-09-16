variable "service_name" {
  default = "django"
}

variable "namespace" {
  default = "production-django"
}

variable "replicas" {
  default = 4
}

variable "image" {
  default = "nginx:mainline"
}