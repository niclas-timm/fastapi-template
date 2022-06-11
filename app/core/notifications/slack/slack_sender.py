from app.core.notifications.slack import slack_connect


def send_slack_message(blocks):
    webhook_client = slack_connect.get_webhook_client()
    res = webhook_client.send(
        text="fallback",
        blocks=blocks
    )
