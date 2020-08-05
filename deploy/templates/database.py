
DATABASES = {
{{ with secret "secrets/database/sfo2-default" }}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin',
        'USER': '{{ .Data.username }}',
        'PASSWORD': '{{ .Data.password }}',
        'HOST': '{{ .Data.hostname }}',
        'PORT': '{{ .Data.port }}',
    }
{{ end }}
}

{{ with secret "postgrest/creds/site" }}
# {{ .Data }}
{{ end }}