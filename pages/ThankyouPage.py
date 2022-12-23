import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class ThankyouPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    class_title = "title"

    def validate_thk_page(self):
        if self.get_text(self.class_title, "class") != "text CHECKOUT: COMPLETE!":
            assert False
