import json
import os
from http.client import HTTPMessage, HTTPResponse
from typing import Callable, Union
from unittest.mock import MagicMock
from urllib.request import Request


def remove_os_env_temporarily() -> dict:
    old_env = os.environ.copy()
    os.environ.clear()
    return old_env


def restore_os_env(old_env: dict) -> None:
    os.environ.clear()
    os.environ.update(old_env)


def build_fake_urlopen(status: int = 200, headers=HTTPMessage(), body={}) -> Callable[..., HTTPResponse]:
    headers.add_header("content-type", 'application/json; charset="UTF-8"')

    mock_resp = HTTPResponse(MagicMock())
    mock_resp.headers = headers
    mock_resp.code = status
    mock_resp.read = MagicMock(return_value=json.dumps(body).encode("UTF-8"))

    def fake_urlopen(req: Union[str, Request], context, timeout):
        mock_resp.url = req.full_url if isinstance(req, Request) else req
        return mock_resp

    return fake_urlopen
