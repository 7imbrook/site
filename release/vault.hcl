exit_after_auth = true

pid_file = "/home/vault/pidfile"

auto_auth {
    method "kubernetes" {
        mount_path = "auth/kubernetes"
        config = {
            role = "django"
        }
    }

    sink "file" {
        config = {
            path = "/consul/token/vault-token"
        }
    }
}