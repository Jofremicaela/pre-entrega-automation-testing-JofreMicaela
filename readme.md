# Proyecto de automatizacion QA - Jofre Micaela


## Descripcion

Proyecto de automatizacion de pruebas realizadas con Python, Selenium WebDriver y Pytest.


El objetivo del proyecto es automatizar distintas pruebas funcionales de una aplicacion web.

## Tecnologias usadas 
- Python
- Selenium WebDriver
- Pytest
- Pytest html
- Git

## Instalacion

Git clone https: //github.com/Jofremicaela/pre-entrega-automation-testing-JofreMicaela.git

## Instalacion de dependencias

pip install -r requirements.txt

## Funcionamiento de las pruebas

-Test login:

 Navega a la página de login de 'saucedemo.com'

 Ingresa credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")

 Valida login exitoso verificando que se haya redirigido a la página de inventario

-Test Inventory:

 Verifica que el título de la página de inventario sea correcto
 
 Comprueba que existan productos visibles en la página (al menos verificar la presencia de uno)
 
 Valida que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

-Test CAR:

 Añade un producto al carrito haciendo clic en el botón correspondiente
 
 Verifica que el contador del carrito se incremente correctamente
 
 Navega al carrito de compras
 
 Comprueba que el producto añadido aparezca correctamente en el carrito