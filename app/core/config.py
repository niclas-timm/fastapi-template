from app.core.settings import get_environment_var

# General
PROJECT_NAME = get_environment_var('PROJECT_NAME') or "FastAPI Template"
SERVER_HOST = get_environment_var('SERVER_HOST') or 'http://app.example.com'

# JWT
JWT_TOKEN = get_environment_var('JWT_TOKEN')
JWT_EMAIL_VERIFICATION_TOKEN = get_environment_var(
    'JWT_EMAIL_VERIFICATION_TOKEN')
JWT_PASSWORD_RESET_TOKEN = get_environment_var('JWT_PASSWORD_RESET_TOKEN')

# Email
EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
EMAILS_ENABLED = get_environment_var('EMAILS_ENABLED') or False
EMAIL_TEMPLATES_DIR = "./app/mail/templates/build"
EMAILS_FROM_NAME = get_environment_var(
    'EMAILS_FROM_NAME') or "example@email.com"
EMAILS_SMTP_HOST = get_environment_var('EMAILS_SMTP_HOST') or "localhost"
EMAILS_PORT = get_environment_var('EMAILS_PORT') or 587
EMAILS_USER = get_environment_var('EMAILS_USER') or 'FastAPI template'
EMAILS_PASSWORD = get_environment_var('EMAILS_PASSWORD') or ""

# Password
PASSWORD_RESET_TOKEN_EXPIRE_HOURS: int = 1
