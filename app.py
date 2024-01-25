import logging
import os

from slack_bolt import Ack, App, BoltContext, Complete, Fail, Say
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)


@app.function("sample_function")
def handle_sample_function_event(inputs: dict, say: Say, fail: Fail, logger: logging.Logger):
    user_id = inputs["user_id"]

    try:
        say(
            channel=user_id,  # sending a DM to this user
            text="Click button to complete function!",
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Click button to complete function!"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click me!"},
                        "action_id": "sample_click",
                    },
                }
            ],
        )
    except Exception as e:
        logger.exception(e)
        fail(f"Failed to handle a function request (error: {e})")


@app.action("sample_click")
def handle_sample_click(
    ack: Ack, body: dict, context: BoltContext, client: WebClient, complete: Complete, fail: Fail, logger: logging.Logger
):
    ack()

    try:
        # Since the button no longer works, we should remove it
        client.chat_update(
            channel=context.channel_id,
            ts=body["message"]["ts"],
            text="Congrats! You clicked the button",
        )

        # Signal that the function completed successfully
        complete({"user_id": context.actor_user_id})
    except Exception as e:
        logger.exception(e)
        fail(f"Failed to handle a function request (error: {e})")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
