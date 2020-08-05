
DATABASES = {
{{ with secret "secrets/database/sfo2-default" }}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin',
        {{ with secret "postgres/creds/site" }}
        'USER': '{{ .Data.username }}',
        'PASSWORD': '{{ .Data.password }}',
        {{ end }}
        'HOST': '{{ .Data.hostname }}',
        'PORT': '{{ .Data.port }}',
    }
{{ end }}
}