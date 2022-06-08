from app.core import config
from app.mail import sender
from pathlib import Path
from .verification import generate_email_verification_token


def send_new_account_email(email_to: str) -> None:
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
