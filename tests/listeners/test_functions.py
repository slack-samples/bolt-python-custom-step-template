import logging
from unittest.mock import Mock

from slack_bolt import Fail, Say

from listeners.functions import handle_sample_step_event

test_logger = logging.getLogger(__name__)


class TestHandleButtonBehaviorOptions:
    def test_handle_button_behavior_options(self):
        fake_inputs = {"user_id": "U1234", "button_behavior": "2"}
        fake_say = Mock(Say)
        fake_fail = Mock(Fail)

        handle_sample_step_event(inputs=fake_inputs, say=fake_say, fail=fake_fail, logger=test_logger)

        fake_fail.assert_not_called()
        fake_say.assert_called_once()
        assert fake_say.call_args.kwargs["channel"] == "U1234"

    def test_handle_sample_step_fail(self):
        fake_inputs = {"user_id": "U1234", "button_behavior": "2"}
        fake_say = Mock(Say, side_effect=Exception("test exception"))
        fake_fail = Mock(Fail)

        handle_sample_step_event(inputs=fake_inputs, say=fake_say, fail=fake_fail, logger=test_logger)

        fake_say.assert_called_once()
        fake_fail.assert_called_once()
        assert fake_fail.call_args.args[0] == "Failed to complete the step: test exception"


class TestHandleSampleStep:
    def test_handle_sample_step(self):
        fake_inputs = {"user_id": "U1234", "button_behavior": "2"}
        fake_say = Mock(Say)
        fake_fail = Mock(Fail)

        handle_sample_step_event(inputs=fake_inputs, say=fake_say, fail=fake_fail, logger=test_logger)

        fake_fail.assert_not_called()
        fake_say.assert_called_once()
        assert fake_say.call_args.kwargs["channel"] == "U1234"

    def test_handle_sample_step_fail(self):
        fake_inputs = {"user_id": "U1234", "button_behavior": "2"}
        fake_say = Mock(Say, side_effect=Exception("test exception"))
        fake_fail = Mock(Fail)

        handle_sample_step_event(inputs=fake_inputs, say=fake_say, fail=fake_fail, logger=test_logger)

        fake_say.assert_called_once()
        fake_fail.assert_called_once()
        assert fake_fail.call_args.args[0] == "Failed to complete the step: test exception"
