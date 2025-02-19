import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class ProductListPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    xpath_welcome = "//h2[contains(text(), 'Bienvenido a Modyo')]"

    def verify_active_session(self):
        if self.is_element_displayed(self.xpath_welcome, "xpath"):
            self.log.info("Estamos en la pagina de login")
        else:
            self.log.error("No estamos en la pagina de Login")
