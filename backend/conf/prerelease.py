
# Temp
DEBUG = False

PRERELEASE = True
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

IS_BUILD_ENV = os.environ.get('RELEASE_STAGE', 'prerelease') is 'build'

if not IS_BUILD_ENV:
    # Import runtime generated configs
    from backend.conf.database import *
    from backend.conf.static import *