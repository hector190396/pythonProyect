import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class ProductListPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    xpath_products = "//span[contains(text(), 'Products')]"
    xpath_product = "//button[@id='add-to-cart-sauce-labs-backpack']"
    xpath_cart_btn = "//div[@id='shopping_cart_container']/a"

    def verify_active_session(self):
        if self.is_element_displayed(self.xpath_products, "xpath"):
            self.log.info("Estamos en la pagina de login")
        else:
            self.log.error("No estamos en la pagina de Login")

    def press_add_product(self):
        self.press_element(self.xpath_product, "xpath")

    def press_cart_button(self):
        self.press_element(self.xpath_cart_btn, "xpath")



