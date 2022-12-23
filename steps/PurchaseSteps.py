from behave import given, when, then

from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.ThankyouPage import ThankyouPage


class PurchaseSteps:

    @given(u'Inicio de sesion {user} {password}')
    def login(context, user, password):
        context.login_page = LoginPage(context.web_driver)
        context.product_list_page = ProductListPage(context.web_driver)
        context.cart_page = CartPage(context.web_driver)
        context.login_page.verify_login_page()
        context.login_page.send_login_info(user, password)
        context.login_page.press_login_btn()

    @when(u'Elegir un producto y agregar al carrito {name} {lastname} {zipcode}')
    def select_product_and_add_to_cart(context, name, lastname, zipcode):
        context.product_list_page.press_add_product()
        context.product_list_page.press_cart_button()
        context.cart_page.verify_cart_page()
        context.cart_page.press_checkout_btn()
        context.cart_page.send_user_info(name, lastname, zipcode)

    @then(u'Validar thank you page al comprar el producto')
    def validate_thankyou_page(context):
        context.thankyou_page = ThankyouPage(context.web_driver)
        context.thankyou_page.validate_thk_page()
