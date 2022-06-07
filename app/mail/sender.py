import emails
from emails.template import JinjaTemplate
from app.core.settings import get_environment_var
from typing import Any, Dict, Optional


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> Any:
    settings = get_mail_settings()
    assert settings["email_enabled"], "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings['from_name'], settings["from_name"]),

    )
    smtp_options = {"host": settings['host'], "port": settings['port']}
    if settings["user"]:
        smtp_options["user"] = settings['user']
    if settings['password']:
        smtp_options["password"] = settings.SMTP_PASSWORD
    return message.send(to=email_to, render=environment, smtp=smtp_options)


def send_test_email(email_to: str) -> None:
    project_name = "Fast API template"
    subject = f"{project_name} - Test email"
    # with open(Path(settings.EMAIL_TEMPLATES_DIR) / "test_email.html") as f:
    with open("./app/mail/templates/build/test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": project_name, "email": email_to},
    )


def get_mail_settings() -> dict:
    """Get Email settings from environment variables.

    Returns:
        dict: The settings.
    """
    return {
        "email_enabled": get_environment_var('EMAILS_ENABLED'),
        "from_name": get_environment_var('EMAILS_FROM_NAME'),
        "host": get_environment_var('EMAILS_SMTP_HOST'),
        "port": get_environment_var('EMAILS_PORT'),
        "user": get_environment_var('EMAILS_USER'),
        "password": get_environment_var('EMAILS_PASSWORD')
    }
