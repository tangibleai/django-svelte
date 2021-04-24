from backend.settings import *

# assert statement is only here to tell some
# less sophisticated editors (*cough* pycharm *cough*)
# that we actually use the * import for something
assert SECURE_SSL_REDIRECT

# SECRET_KEY = r'@qa&1-#)+zb9#8r1(v+aj_t1tkxua+9@h9trfu+b@0^&55zh(g'
SECURE_SSL_REDIRECT = False
debug = True
# DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CSRF_COOKIE_SECURE = False
CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'http://127.0.0.1:8080']
CSRF_TRUSTED_ORIGINS = ['localhost', '127.0.0.1']
