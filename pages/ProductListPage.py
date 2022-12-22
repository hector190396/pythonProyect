import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class ProductListPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    xpath_products = "//span[contains(text(), 'Products')]"

    def verify_active_session(self):
        if self.is_element_displayed(self.xpath_products, "xpath"):
            self.log.info("Estamos en la pagina de login")
        else:
            self.log.error("No estamos en la pagina de Login")
