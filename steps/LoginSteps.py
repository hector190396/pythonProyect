from behave import given, when, then

from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage


class LoginSteps:

    @given(u'Que estamos en login page')
    def verify_login_page(context):
        context.login_page = LoginPage(context.web_driver)
        context.product_list_page = ProductListPage(context.web_driver)

    @when(u'Haya ingresado credenciales y iniciando sesion {user} {password}')
    def send_login_info(context, user, password):
        print("Ingresar credenciales")
        context.login_page.verify_login_page()
        context.login_page.send_login_info(user, password)
        context.login_page.press_login_btn()

    @then(u'Validar que la sesion este activa')
    def validate_active_session(context):
        print("Validamos sesion activa")
        context.product_list_page.verify_active_session()

    @then(u'Validar advertencia de usuario bloqueado')
    def validate_blocked_user(context):
        print("Validamos sesion activa")
        context.login_page.validate_blocked_user()
