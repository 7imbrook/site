variable "service_name" {
  default = "django"
}

variable "namespace" {
  default = "production-django"
}

variable "replicas" {
  default = 2
}

variable "image" {
  default = "7imbrook/site:migrate"
}