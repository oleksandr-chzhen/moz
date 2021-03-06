import os
import logging

DEBUG = True
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SECRET_KEY = os.environ.get('MOZ_SECRET_KEY', 'SUPER_SECRET_KEY')
SECURITY_PASSWORD_SALT = '16756d01a4bbbfa4800b3af15953ada021ec508e'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/moz/files'
DB_NAME = os.environ.get('DB_NAME', 'sql11223417')
DB_USER = os.environ.get('DB_USER', 'sql11223417')
DB_PASSWORD = os.environ.get('DB_PWD')
DB_HOST = os.environ.get('DB_HOST', 'sql11.freemysqlhosting.net')
DB_PORT = int(os.environ.get('DB_PORT', 3306))
ADMIN_PATH = '/admin'
DEFAULT_ADMIN_USER = os.environ.get('ADMIN_USER', 'admin@admin.com')
DEFAULT_ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
MIN_PASSWORD_LENGTH = 8

PROTOCOL = 'http://'
DOMAIN = 'localhost:5000'
CHECK_LOCATION = False if os.environ.get('CHECK_LOCATION', True) == 'False' else True

# mail settings
MAIL_SERVER = 'email-smtp.eu-west-1.amazonaws.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('APP_MAIL_USERNAME', '')
MAIL_PASSWORD = os.environ.get('APP_MAIL_PASSWORD', '')
MAIL_DEFAULT_SENDER = 'moz.noreply@gmail.com'

# Cookies
REMEMBER_COOKIE_REFRESH_EACH_REQUEST = True
REMEMBER_COOKIE_DURATION = 86400  # 1 day

# logging
LOGGING_FOLDER = os.path.join(BASE_DIR, 'logs')
LOGGING_FILENAME = 'moz.log'
LOGGING_LEVEL = logging.WARNING
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# recapcha
RECAPTCHA_PUBLIC_KEY = '6LdEnFkUAAAAAPTmtd_dwd_8clh__PoCHyURE2lN'
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', '')