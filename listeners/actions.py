import logging

from slack_bolt import Ack, BoltContext, Complete, Fail
from slack_sdk import WebClient


def handle_sample_click(
    ack: Ack, body: dict, context: BoltContext, client: WebClient, complete: Complete, fail: Fail, logger: logging.Logger
):
    ack()
    try:
        # Signal that the step completed successfully
        complete(outputs={"user_id": context.actor_user_id})

        # Since the button no longer works, we should remove it
        client.chat_update(
            channel=context.channel_id,
            ts=body["message"]["ts"],
            text="Step completed successfully!",
        )
    except Exception as e:
        logger.exception(e)
        fail(f"Failed to complete the step: {e}")
