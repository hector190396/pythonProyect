import time

from driver_interactions.ElementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_logo = "//div[@class='login_logo']"
    id_user_name_input = "//div[@class='login_wrapper']/descendant::input[@id='user-name']"
    id_password_input = "//div[@class='login_wrapper']/descendant::input[@id='password']"
    xpath_login_btn = "//div[@class='login_wrapper']/descendant::input[@id='login-button']"

    def verify_login_page(self):
        if self.is_element_displayed(self.xpath_logo, "xpath"):
            self.log.info("estamos en la pagina de login")
        else:
            self.log.error("No estamos en la pagina de login")

    def send_login_info(self):
        self.send_text("standard_user", self.id_user_name_input, "xpath")
        self.send_text("secret_sauce", self.id_password_input, "xpath")

    def press_login_btn(self):
        self.press_element(self.xpath_login_btn, "xpath")
