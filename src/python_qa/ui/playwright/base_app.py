from common.logging import logger

from utils.wait import wait_for

from utils.iterable import filtered


class BaseApp:
    def open(self, url: str):
        logger.info(f"Open page by url: {url}")
        self._page.goto(self.host + url)
        self._page.wait_for_load_state("load")

    def get_cookie_value(self, name: str):
        cookies = wait_for(
            lambda: filtered(lambda c: c["name"] == name, self._context.cookies())
        )
        if cookies:
            return cookies[0]["value"]
