from typing import Optional
from app.core import config
from app.core.notifications.mail import sender
from pathlib import Path
from datetime import datetime, timedelta
from jose import jwt, JWTError


def generate_email_verification_token(email: str) -> str:
    """Generate token for email verification.

    Generate a jwt token with a short expiration time with
    an email address as the sub. The token will be sent via email
    in order to verify the users email.

    Args:
        email (str): The email that will be the sub of the token.

    Returns:
        str: The token.
    """
    delta = timedelta(hours=config.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, config.JWT_EMAIL_VERIFICATION_TOKEN, algorithm="HS256",
    )
    return encoded_jwt


def verify_email_token(token: str) -> Optional[str]:
    """Verify email verification token.

    Args:
        token (str): The token to be verified.

    Returns:
        Optional[str]: If token is valid, the sub (email) from the token.
    """
    try:
        decoded = jwt.decode(
            token, config.JWT_EMAIL_VERIFICATION_TOKEN, algorithms="HS256")
        return decoded["sub"]
    except JWTError:
        return None


def send_new_account_email(email_to: str) -> None:
    """Send welcome email to new user.

    Send an email to a newly created user and ask him/her
    to verify their email address.

    Args:
        email_to (str): The email address the mail will be sent to.
    """
    project_name = config.PROJECT_NAME
    subject = f"{project_name} - Verify your account"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "new_account.html", encoding='utf-8') as f:
        template_str = f.read()
    token = generate_email_verification_token(email=email_to)
    link = f"{config.SERVER_HOST}/email/verify?token={token}"
    sender.send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "email": email_to,
            "link": link,
        },
    )


def send_reset_password_email(email_to: str, token: str) -> None:
    """Send email with JWT that can be used for password resets.

    Send a link with a token as a query param to a given email.
    The link can then be used to recover the password of the user.

    Args:
        email_to (str): The email the mail will be sent to.
        token (str): The token that will be included in the link.
    """
    project_name = config.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email_to}"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "reset_password.html", encoding='utf-8') as f:
        template_str = f.read()
    server_host = config.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"
    sender.send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "username": email_to,
            "email": email_to,
            "valid_hours": config.PASSWORD_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )
