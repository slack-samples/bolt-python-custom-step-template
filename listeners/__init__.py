from slack_bolt import App

from .actions import handle_sample_click
from .functions import handle_button_behavior_options, handle_sample_step_event


def register_listeners(app: App):
    app.action("sample_click")(handle_sample_click)
    app.function("button_behavior_options", auto_acknowledge=False)(handle_button_behavior_options)
    app.function("sample_step")(handle_sample_step_event)
