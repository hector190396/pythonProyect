from selenium import webdriver


class InitWebDriver:

    @staticmethod
    def init_web_driver():
        web_driver = webdriver.Chrome(r"driver_interactions/chromedriver.exe")
        return web_driver

