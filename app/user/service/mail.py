from app.core import config
from app.mail import sender
from pathlib import Path


def send_new_account_email(email_to: str) -> None:
    project_name = config.PROJECT_NAME
    subject = f"{project_name} - Email verification"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
        template_str = f.read()

    # @TODO: Generate URL that includes token that then will be sent as the link.
    link = config.SERVER_HOST
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
