Feature: Login
  Scenario: Validar inicio de sesion correcto
    Given Que estamos en login page
    When  Haya ingresado credenciales y iniciando sesion
    Then  Validar que la sesion este activa
