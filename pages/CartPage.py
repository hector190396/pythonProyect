import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class CartPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_checkout_btn = "//button[@id='checkout']"
    xpath_name = "//input[@id='first-name']"
    xpath_lastname = "//input[@id='last-name']"
    xpath_zip = "//input[@id='postal-code']"
    xpath_continue_button = "//input[@id='continue']"
    xpath_finish_btn = "//button[@id='finish']"

    def press_checkout_btn(self):
        self.press_element(self.xpath_checkout_btn, "xpath")

    class_title = "title"

    def verify_cart_page(self):
        if self.get_text(self.class_title, "class") != "YOUR CART":
            assert False

    def send_user_info(self, name, lastname, zipcode):
        self.send_text(name, self.xpath_name, "xpath")
        self.send_text(lastname, self.xpath_lastname, "xpath")
        self.send_text(zipcode, self.xpath_zip, "xpath")
        self.press_element(self.xpath_continue_button, "xpath")
        self.press_element(self.xpath_finish_btn, "xpath")
