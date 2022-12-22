Feature: Login
  Scenario: Validar inicio de sesion correcto
    Given Que estamos en login page
    When  Haya ingresado credenciales y iniciando sesion standard_user  secret_sauce
    Then  Validar que la sesion este activa

  Scenario: Validar Inicio de sesion con usuario bloqueado
    Given Que estamos en login page
    When  Haya ingresado credenciales y iniciando sesion locked_out_user secret_sauce
    Then  Validar advertencia de usuario bloqueado