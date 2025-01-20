import logging
from unittest.mock import Mock

import pytest
from slack_bolt import Ack, Complete, Fail, Say

from listeners.functions import handle_behavior_options, handle_sample_step_event

test_logger = logging.getLogger(__name__)


class TestHandleButtonBehaviorOptions:
    def setup_method(self):
        self.fake_ack = Mock(Ack)
        self.fake_complete = Mock(Complete)

    def test_handle_behavior_options(self):
        handle_behavior_options(ack=self.fake_ack, complete=self.fake_complete)

        self.fake_ack.assert_called_once()
        self.fake_complete.assert_called_once()
        kwargs = self.fake_complete.call_args.kwargs
        assert "options" in kwargs["outputs"]
        assert isinstance(kwargs["outputs"]["options"], list)

    def test_handle_behavior_options_with_exception(self):
        self.fake_complete.side_effect = Exception("test exception")

        with pytest.raises(Exception) as _:
            handle_behavior_options(ack=self.fake_ack, complete=self.fake_complete)

        self.fake_ack.assert_called_once()
        self.fake_complete.assert_called_once()


class TestHandleSampleStep:
    def setup_method(self):
        self.fake_inputs = {"user_id": "U1234", "button_behavior": "2"}
        self.fake_say = Mock(Say)
        self.fake_fail = Mock(Fail)

    def test_handle_sample_step(self):
        handle_sample_step_event(inputs=self.fake_inputs, say=self.fake_say, fail=self.fake_fail, logger=test_logger)

        self.fake_fail.assert_not_called()
        self.fake_say.assert_called_once()
        assert self.fake_say.call_args.kwargs["channel"] == self.fake_inputs["user_id"]

    def test_handle_sample_step_fail(self):
        self.fake_say.side_effect = Exception("test exception")

        handle_sample_step_event(inputs=self.fake_inputs, say=self.fake_say, fail=self.fake_fail, logger=test_logger)

        self.fake_say.assert_called_once()
        self.fake_fail.assert_called_once()
