import logging
import os
from unittest.mock import MagicMock, patch
from urllib import request

from tests.utils import build_fake_urlopen, remove_os_env_temporarily, restore_os_env

old_env = remove_os_env_temporarily()
os.environ["SLACK_BOT_TOKEN"] = "xoxb-test"

with patch.object(request, "urlopen") as mock_urlopen:
    mock_urlopen.side_effect = build_fake_urlopen(body={"ok": True})
    from slack_bolt import BoltContext
    from slack_sdk import WebClient

    from app import handle_sample_click, handle_sample_step_event

restore_os_env(old_env)


class TestApp:
    def setup_method(self):
        self.old_os_env = remove_os_env_temporarily()
        os.environ["SLACK_BOT_TOKEN"] = "xoxb-test"

    def teardown_method(self):
        restore_os_env(self.old_os_env)

    def test_handle_sample_step_event(self):
        fake_inputs = {"user_id": "U1234"}
        fake_say = MagicMock()
        fake_fail = MagicMock()

        handle_sample_step_event(
            inputs=fake_inputs, say=fake_say, fail=fake_fail, logger=logging.Logger("tests/test_app.py")
        )

        fake_fail.assert_not_called()
        fake_say.assert_called_once()
        assert fake_say.call_args.kwargs["channel"] == "U1234"

    def test_handle_sample_click(self):
        fake_ack = MagicMock()
        fake_body = {"message": {"ts": "12345"}}
        fake_fail = MagicMock()
        fake_complete = MagicMock()

        fake_context = BoltContext()
        fake_context["channel_id"] = "C1A2B3C"
        fake_context["actor_user_id"] = "U1234"

        fake_client = WebClient("xoxb-test")
        fake_client.chat_update = MagicMock()

        handle_sample_click(
            ack=fake_ack,
            body=fake_body,
            context=fake_context,
            client=fake_client,
            complete=fake_complete,
            fail=fake_fail,
            logger=logging.Logger("tests/test_app.py"),
        )

        fake_ack.assert_called_once()
        fake_client.chat_update.assert_called_once()
        assert fake_client.chat_update.call_args.kwargs["channel"] == fake_context.channel_id
        assert fake_client.chat_update.call_args.kwargs["ts"] == fake_body["message"]["ts"]
        fake_complete.assert_called_once()
        assert fake_complete.call_args.args[0] == {"user_id": fake_context.actor_user_id}
        fake_fail.assert_not_called
