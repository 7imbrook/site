variable "service_name" {
  default = "django"
}

variable "namespace" {
  default = "production-django"
}

variable "replicas" {
  default = 1
}

variable "image" {
  default = "nginx:mainline"
}