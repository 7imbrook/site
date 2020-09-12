from backend.default import *

DEBUG = False
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]

# Allow all subdomains to access session from django.
# used for lookaside auth from nginx for things like vault and consul
SESSION_COOKIE_DOMAIN = ".timbrook.dev"

AWS_LOCATION = 'static'
AWS_STORAGE_BUCKET_NAME = 'timbrook'
AWS_S3_REGION_NAME = 'sfo2'

AWS_DEFAULT_ACL = 'public-read'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_ENDPOINT_URL = 'https://sfo2.digitaloceanspaces.com'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Import runtime generated configs
# TODO, I don't like this hack
try:
    from backend.conf.database import *
    from backend.conf.static import *
except:
    print("failed to import all...")
    pass