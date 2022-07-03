"""
Send a slack message with a custom text.
"""

from slack_sdk.webhook import WebhookResponse

from app.core.notifications.slack import slack_connect


def send_slack_message(blocks) -> WebhookResponse:
    """Send a slack message."""
    webhook_client = slack_connect.get_slack_webhook_client()
    return webhook_client.send(
        text="fallback",
        blocks=blocks
    )  # type: ignore
