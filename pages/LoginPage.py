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
    xpath_error_container = "//div[@class='error-message-container error']"

    def verify_login_page(self):
        if self.is_element_displayed(self.xpath_logo, "xpath"):
            self.log.info("estamos en la pagina de login")
        else:
            self.log.error("No estamos en la pagina de login")

    def send_login_info(self, user, password):
        self.send_text(user, self.id_user_name_input, "xpath")
        self.send_text(password, self.id_password_input, "xpath")

    def press_login_btn(self):
        self.press_element(self.xpath_login_btn, "xpath")

    def validate_blocked_user(self):
        if not self.is_element_displayed(self.xpath_error_container, "xpath"):
            self.log.info("El mensaje no se encuentra")
