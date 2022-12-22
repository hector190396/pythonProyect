import time
from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver


def before_all(context):
    context.prepare_web_driver = InitWebDriver
    context.web_driver = context.prepare_web_driver.init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com/")
    print("Script started")


def after_all(context):
    time.sleep(15)
    context.web_driver.quit()
    print("Script ended")
