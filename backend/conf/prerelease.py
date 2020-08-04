
# Temp
DEBUG = False

PRERELEASE = True
PROD = True

ALLOWED_HOSTS = [
    "timbrook.dev"
]

# Import runtime generated configs
from backend.conf.database import *
from backend.conf.static import *