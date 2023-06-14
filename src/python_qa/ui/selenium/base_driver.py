from selenium import webdriver


class BaseDriver:

    def __init__(self, driver: webdriver.Remote):
        self.driver = self.d = driver
