import logging

from slack_bolt import Ack, Complete, Fail, Say

button_behaviors = [
    "signal the step has completed",
    "summon a dramatic kazoo solo",
    "release a random pun bomb",
    "unleash a parade of emoji",
    "spawn a random dad joke",
    "trigger a confetti explosion",
]


def handle_behavior_options(ack: Ack, complete: Complete):
    try:
        complete(
            outputs={
                "options": [
                    {
                        "text": {"text": behavior, "type": "plain_text"},
                        "value": str(index),
                    }
                    for index, behavior in enumerate(button_behaviors)
                ]
            }
        )
    finally:
        ack()


def handle_sample_step_event(inputs: dict, say: Say, fail: Fail, logger: logging.Logger):
    user_id = inputs["user_id"]
    button_behavior = inputs["button_behavior"]

    try:
        text = f"Click this button to {button_behaviors[int(button_behavior)]}"
        say(
            channel=user_id,  # sending a DM to this user
            text=text,
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "plain_text", "text": text},
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
        fail(f"Failed to complete the step: {e}")
