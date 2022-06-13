# -------------------------------------------------------------------------------
# Send a slack message with a custom text.
# -------------------------------------------------------------------------------
from app.core.notifications.slack import slack_connect
from slack_sdk.webhook import WebhookResponse


def send_slack_message(blocks) -> WebhookResponse:
    webhook_client = slack_connect.get_webhook_client()
    return webhook_client.send(
        text="fallback",
        blocks=blocks
    )  # type: ignore
