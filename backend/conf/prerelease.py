
DEBUG = False
PRERELEASE = True
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]


with file("/opt/config/dbconnection") as f:
    conn_string = f.read()

CONNSTR = conn_string

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