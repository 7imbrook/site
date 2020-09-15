consul {
  retry {
    enabled = true
    attempts = 12
    backoff = "250ms"
    max_backoff = "1m"
  }

  ssl {
    enabled = true
    verify = false
  }
}

vault {
  vault_agent_token_file = "/vault/secrets/token"
}

reload_signal = "SIGHUP"
kill_signal = "SIGINT"
max_stale = "10m"
block_query_wait = "60s"
log_level = "warn"
syslog {
  enabled = false
  facility = "LOCAL5"
}

exec {
  command = "uwsgi --ini ./conf/uwsgi.ini"
  
  splay = "5s"
  env {
    pristine = false
  }

  # This defines the signal that will be sent to the child process when a
  # change occurs in a watched template. The signal will only be sent after the
  # process is started, and the process will only be started after all
  # dependent templates have been rendered at least once. The default value is
  # nil, which tells Consul Template to stop the child process and spawn a new
  # one instead of sending it a signal. This is useful for legacy applications
  # or applications that cannot properly reload their configuration without a
  # full reload.
  reload_signal = "SIGUSR1"

  # This defines the signal sent to the child process when Consul Template is
  # gracefully shutting down. The application should begin a graceful cleanup.
  # If the application does not terminate before the `kill_timeout`, it will
  # be terminated (effectively "kill -9"). The default value is "SIGINT".
  kill_signal = "SIGQUIT"

  # This defines the amount of time to wait for the child process to gracefully
  # terminate when Consul Template exits. After this specified time, the child
  # process will be force-killed (effectively "kill -9"). The default value is
  # "30s".
  kill_timeout = "2s"
}

template {
  destination = "/etc/ssl/certs/consulCA.pem"
  contents = "{{ range caRoots }}{{ .RootCertPEM }}{{ end }}"
}

// template {
//   destination = "/app/backend/conf/database.py"
//   source = "/opt/deploy/templates/database.py"
//   command = "sh -c \"echo c > /tmp/fifo0\""
// }

// template {
//   destination = "/app/backend/conf/static.py"
//   source = "/opt/deploy/templates/static.py"
//   command = "sh -c \"echo c > /tmp/fifo0\""
// }
