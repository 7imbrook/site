
{{ with secret "secrets/database/sfo2-default" }}
CONNSTR = '{{ .Data.username }}:{{ .Data.password }}'
{{ end }}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}