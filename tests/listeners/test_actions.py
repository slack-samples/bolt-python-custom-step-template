import logging
from unittest.mock import Mock

from slack_bolt import Ack, BoltContext, Complete, Fail
from slack_sdk import WebClient

from listeners import actions

test_logger = logging.getLogger(__name__)


class TestHandleSampleClick:
    def test_handle_sample_click(self):
        fake_ack = Mock(Ack)
        fake_body = {"message": {"ts": "12345"}}
        fake_fail = Mock(Fail)
        fake_complete = Mock(Complete)

        fake_context = BoltContext()
        fake_context["channel_id"] = "C1A2B3C"
        fake_context["actor_user_id"] = "U1234"

        fake_client = Mock(WebClient)
        fake_client.chat_update = Mock()

        actions.handle_sample_click(
            ack=fake_ack,
            body=fake_body,
            context=fake_context,
            client=fake_client,
            complete=fake_complete,
            fail=fake_fail,
            logger=test_logger,
        )

        fake_ack.assert_called_once()
        fake_fail.assert_not_called()

        fake_client.chat_update.assert_called_once()
        _, kwargs = fake_client.chat_update.call_args
        assert kwargs["channel"] == fake_context.channel_id
        assert kwargs["ts"] == fake_body["message"]["ts"]

        fake_complete.assert_called_once()
        _, kwargs = fake_complete.call_args
        assert kwargs["outputs"] == {"user_id": fake_context.actor_user_id}
