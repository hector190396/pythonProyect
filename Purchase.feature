Feature: Compra de productos

  Scenario: Compra exitosa
    Given Inicio de sesion standard_user secret_sauce
    When  Elegir un producto y agregar al carrito Hector Caldera 33085
    Then  Validar thank you page al comprar el producto