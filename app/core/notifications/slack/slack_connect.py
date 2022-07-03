"""
Get a slack webhook client.
"""

from slack.webhook.client import WebhookClient

from app.core import config


def get_slack_webhook_client():
    """Create instance of Slacks webhook client.

    Returns:
        WebhookClient: The webhook client
    """
    return WebhookClient(config.SLACK_WEBHOOK_URL)  # type: ignore
