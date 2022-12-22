import time
from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import utilities.Logger as Logger

log = Logger.func_logger()


def before_all(context):
    log.info("Script started")


def after_all(context):
    time.sleep(15)
    context.web_driver.quit()
    print("Script ended")


def before_scenario(context, scenario):
    context.prepare_web_driver = InitWebDriver
    context.web_driver = context.prepare_web_driver.init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com/")


def after_scenario(context, scenario):
    context.web_driver.quit()
