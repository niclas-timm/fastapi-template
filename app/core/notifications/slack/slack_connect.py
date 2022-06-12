# -------------------------------------------------------------------------------
# Get a slack webhook client.
# -------------------------------------------------------------------------------
from slack.webhook.client import WebhookClient
from app.core import config
from slack_sdk.webhook import WebhookClient


def get_webhook_client():
    """Create instance of Slacks webhook client.

    Returns:
        WebhookClient: The webhook client
    """
    return WebhookClient(config.SLACK_WEBHOOK_URL)  # type: ignore
