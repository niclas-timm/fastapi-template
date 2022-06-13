# -------------------------------------------------------------------------------
# Manage SMTP configuration and helper methods for sending email.
# -------------------------------------------------------------------------------
import emails
from emails.template import JinjaTemplate
from app.core import config
from typing import Any, Dict
from pathlib import Path


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> Any:
    """Helper method to send emails.

    Args:
        email_to (str): The email address the mail will be sent to.
        subject_template (str, optional): The subject of the mail. Defaults to "".
        html_template (str, optional): The html template (content of the mail). Defaults to "".
        environment (Dict[str, Any], optional): The values that will be replaced in the html template. Defaults to {}.

    Returns:
        Any: _description_
    """

    assert config.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(config.EMAILS_FROM_NAME, config.EMAILS_FROM_NAME),

    )
    smtp_options = {"host": config.EMAILS_SMTP_HOST, "port": config.EMAILS_PORT}
    if config.EMAILS_USER:
        smtp_options["user"] = config.EMAILS_USER
    if config.EMAILS_PASSWORD:
        smtp_options["password"] = config.EMAILS_PASSWORD
    return message.send(to=email_to, render=environment, smtp=smtp_options)


def send_test_email(email_to: str) -> None:
    """Send a test mail.

    Helper method to test if email settings are valid.
    Should be deleted after email setup is finished.

    Args:
        email_to (str): The email address the mail will be sent to.
    """
    project_name = "Fast API template"
    subject = f"{project_name} - Test email"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": project_name, "email": email_to},
    )
