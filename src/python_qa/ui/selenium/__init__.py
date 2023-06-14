import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from ...logging.logging import Logging

logger = Logging.logger


class BaseElement(object):
    def __init__(
        self, by: object, selector: str, wait_time: object = 5, instance=None
    ):
        self.selector = (by, selector)
        self.wait_time = wait_time
        self.instance = instance

    def __get__(self, instance, owner):
        logger.info(f"Element requested: {self.selector[0]} {self.selector[1]}")
        self.instance = instance
        return self

    def __call__(self, *args, **kwargs) -> WebElement:
        if "driver" in dir(self.instance):
            logger.info(
                f"Search for an element by: {self.selector[0]} {self.selector[1]}"
            )
            return WebDriverWait(self.instance.driver, self.wait_time).until(
                EC.presence_of_element_located(self.selector),
                f"Element {self.selector} not found in {self.wait_time} sec",
            )
