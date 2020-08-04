
# Temp
DEBUG = False

PRERELEASE = True
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Import runtime generated configs
from backend.conf.database import *
from backend.conf.static import *