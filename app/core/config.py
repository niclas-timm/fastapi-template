"""
Configuration variables that can be used accross the app.
"""
import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()


def get_environment_var(name: str) -> Optional[str]:
    """Get environment variable.

    Helper method to get value from .env file.

    Args:
        name (str): The name of the environment var.

    Returns:
        str: The value of the enironment var.
    """
    return os.getenv(name)


# =============================================================================
# General.
#
# General app settings like name and host.
# =============================================================================
PROJECT_NAME = get_environment_var('PROJECT_NAME') or "FastAPI Template"
SERVER_HOST = get_environment_var('SERVER_HOST') or 'http://app.example.com'
CONFIG_YML_PATH = 'app/config/config.yml'


# =============================================================================
# Database.
#
# Database related settings like DB connection parameters.
# =============================================================================
DB_USERNAME = get_environment_var('DB_USERNAME') or None
DB_PASSWORD = get_environment_var('DB_PASSWORD') or None
DB_HOST = get_environment_var('DB_HOST') or None
DB_PORT = get_environment_var('DB_PORT') or None
DB_NAME = get_environment_var('DB_NAME') or None


# =============================================================================
# User.
#
# User related settings like authentication data for the super user.
# =============================================================================
SUPER_USER_NAME = get_environment_var('SUPER_USER_NAME') or None
SUPER_USER_EMAIL = get_environment_var('SUPER_USER_EMAIL') or None
SUPER_USER_PASSWORD = get_environment_var('SUPER_USER_PASSWORD') or None


# =============================================================================
# General.
#
# Configure hosts for CORS.
# =============================================================================
CORS_ALLOWED_ORIGINS = get_environment_var('CORS_ALLOWED_ORIGINS') or None


# =============================================================================
# Redis.
#
# Configure redis connection settings.
# =============================================================================
REDIS_HOST = get_environment_var('REDIS_HOST') or None
REDIS_PORT = get_environment_var('REDIS_PORT') or None
REDIS_USERNAME = get_environment_var('REDIS_USERNAME') or None
REDIS_PASSWORD = get_environment_var('REDIS_PASSWORD') or None


# =============================================================================
# JWT.
#
# JWT settings. Especially configuration for various secrets for authentication
# and password resets.
# =============================================================================
JWT_TOKEN = get_environment_var('JWT_TOKEN')
JWT_EMAIL_VERIFICATION_TOKEN = get_environment_var(
    'JWT_EMAIL_VERIFICATION_TOKEN')
JWT_PASSWORD_RESET_TOKEN = get_environment_var('JWT_PASSWORD_RESET_TOKEN')


# =============================================================================
# Email.
#
# Configure this like smtp connection and if emails are enabled in your app.
# =============================================================================
EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
EMAILS_ENABLED = get_environment_var('EMAILS_ENABLED') or False
EMAIL_TEMPLATES_DIR = "./app/core/notifications/mail/templates/build"
EMAILS_FROM_NAME = get_environment_var(
    'EMAILS_FROM_NAME') or "example@email.com"
EMAILS_SMTP_HOST = get_environment_var('EMAILS_SMTP_HOST') or "localhost"
EMAILS_PORT = get_environment_var('EMAILS_PORT') or 587
EMAILS_USER = get_environment_var('EMAILS_USER') or 'FastAPI template'
EMAILS_PASSWORD = get_environment_var('EMAILS_PASSWORD') or ""


# =============================================================================
# Password.
#
# Configure password specific options like the duration of password reset token
# validity.
# =============================================================================
PASSWORD_RESET_TOKEN_EXPIRE_HOURS: int = 1


# =============================================================================
# Slack.
#
# Configure Slack (e.g., Webhook URL).
# =============================================================================
SLACK_WEBHOOK_URL = get_environment_var('SLACK_WEBHOOK_URL') or None
