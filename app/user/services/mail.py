from app.core import config
from app.mail import sender
from pathlib import Path
from .verification import generate_email_verification_token
from app.core import config
from app.mail import sender


def send_new_account_email(email_to: str) -> None:
    """Send welcome email to new user.

    Send an email to a newly created user and ask him/her
    to verify their email address.

    Args:
        email_to (str): The email address the mail will be sent to.
    """
    project_name = config.PROJECT_NAME
    subject = f"{project_name} - Email verification"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
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
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
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
