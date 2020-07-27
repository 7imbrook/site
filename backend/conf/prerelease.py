
# Temp
DEBUG = False

PRERELEASE = True
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Import runtime generated configs
from backend.conf.database import *
from backend.conf.static import *