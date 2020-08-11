
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin',
        {{ with secret "dbs/creds/site" }}
        'USER': '{{ .Data.username }}',
        'PASSWORD': '{{ .Data.password }}',
        {{ end }}
        'HOST': '{{ key "site/database/host" }}',
        'PORT': '{{ key "site/database/port" }}',
    }
}