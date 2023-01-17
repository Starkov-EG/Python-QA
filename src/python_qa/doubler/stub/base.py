import re

import cattr

from python_qa.logging.logging import Logging
from pytest_httpserver import HTTPServer

from python_qa.utils.wait import wait_for_server_start

logger = Logging.logger


class BaseServiceStub:
    _port: int = 10071
    _stub: HTTPServer = None

    def __int__(self, port: int = None):
        if port:
            self._port = port

    def add_rout(self, url: str, data=None, code: int = 200):
        logger.info(f"Adding stub: url={url}, data={data}, code={code}")
        json = cattr.Converter().unstructure_attrs_asdict(
            data
        )  # ToDo: type, converter
        self._stub.expect_request(re.compile(".*" + url)).respond_with_json(
            response_json=json, status=code
        )  # ToDo: variants

    def start(self):
        logger.info("Stub starting...")
        self._stub = HTTPServer(host="localhost", port=self._port)
        self._stub.start()
        wait_for_server_start(f"http://localhost:{self._port}")

    def stop(self):
        logger.info("Stub stopping...")
        self._stub.stop()
