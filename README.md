🧮 Calculadora Moderna con Kivy
Una aplicación de calculadora de escritorio con una interfaz elegante inspirada en el modo oscuro, desarrollada íntegramente en Python utilizando el framework Kivy.

Python Kivy Licencia

✨ Características
Interfaz Estilizada: Diseño minimalista con botones de colores (naranja para operadores, gris para números).
Funciones Matemáticas: Suma, resta, multiplicación, división, porcentajes y cambio de signo (+/-).
Adaptativa: La disposición de los botones se ajusta mediante un GridLayout para mantener la proporción.
Manejo de Errores: Control de excepciones para evitar cierres inesperados en operaciones inválidas (como división por cero).
🚀 Instalación y Uso
Prerrequisitos
Tener instalado Python 3.8 o superior.

Pasos
Clonar el proyecto:

git clone [https://github.com/TU_USUARIO/calculadora-kivy.git](https://github.com/TU_USUARIO/calculadora-kivy.git)
cd calculadora-kivy
Instalar dependencias: pip install -r requirements.txt

Ejecutar la aplicación: python calculadora.py

🛠️ Detalles Técnicos Framework: Kivy para la renderización de la interfaz de usuario.

Lógica: Uso de la función eval() de Python para el procesamiento de expresiones matemáticas en cadena.

Diseño: Ventana configurada con un tamaño fijo de 399x500 píxeles para una experiencia óptima de escritorio.

📸 Vista Previa La calculadora utiliza una combinación de colores [0.1, 0.1, 0.1, 1] para el fondo y acentos naranjas [1, 0.65, 0, 1] en los operadores principales, imitando el estilo de las calculadoras de dispositivos móviles modernos.

Desarrollado por Pablo Galván
