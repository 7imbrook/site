
{{ with secret "secrets/database/sfo2-default" }}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin',
        'USER': '{{ .Data.username }}',
        'PASSWORD': '{{ .Data.password }}',
        'HOST': '{{ .Data.hostname }}',
        'PORT': '{{ .Data.port }}',
    }
}
{{ end }}