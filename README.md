Proposito del proyecto:

    Aplicar los conocimientos adquiridos para demostrar la capacidad para automatizar flujos básicos de navegación web utilizando Selenium WebDriver  y Python. asi poner en práctica lo  aprendido sobre interacción con elementos web, estrategias de localización y validación de estados en una página.  

Se realizaron pruebas automaticas usando el sitio web: www.saucedemo.com 

las Tecnologías Usadas son:

    Python como lenguaje principal
    Pytest para estructura de testing
    Selenium WebDriver para automatización
    Git y GitHub para control de versiones

Instrucciones:
    Instalamos las dependencias con los siguientes codigos:

    pip install pytest-html
    pytest -v en la terminal para ejecutar tus pruebas con detalles verbosos.
    pip install selenium 

Se automatizaron 3 fixtures con diferentes casos de prueba:

    1 Automatización de Login:

        Navegar a la página de login de saucedemo.com
        Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
        Validar login exitoso verificando que se haya redirigido a la página de inventario

    2 Navegación y Verificación del Catálogo: 

        Verificar que el título de la página de inventario sea correcto
        Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
        Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)


    3 Interacción con Productos: 

        Añadir un producto al carrito haciendo clic en el botón correspondiente
        Verificar que el contador del carrito se incremente correctamente
        Navegar al carrito de compras
        Comprobar que el producto añadido aparezca correctamente en el carrito

Al final ejecutamos el codigo: pytest -v --html=reports/resporte.html
para mostrar los resultados en el archivo correspondiente de las pruebas ejecutas en nuestra entrega parcial