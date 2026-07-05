# Proyecto Final: Automatización de API
## 📋 Propósito del Proyecto
Este proyecto es un framework de automatización de pruebas diseñado para validar los endpoints de la API JSONPlaceholder. El objetivo es asegurar la funcionalidad y estabilidad de la API mediante pruebas automatizadas escalables, aplicando el patrón Page Object Model (POM) para separar la lógica de la API de la lógica de los tests.

----------------------------------------------------------

## 📂 Estructura del Proyecto
- pages/ : Clases (Page Objects) que gestionan las peticiones a la API
- tests/ : Casos de prueba (Scripts ejecutables con Pytest)
- conftest.py : Fixtures de Pytest para configuración global
- pytest.ini : Configuración de ejecución y sistema de logs
- requirements.txt : Dependencias del proyecto
- README.md : Documentación del proyecto

----------------------------------------------------------

## 🛠️ Tecnologías Utilizadas
- Python 3.13

- Pytest: Framework principal para estructurar y ejecutar los tests.

- Requests: Biblioteca para realizar peticiones HTTP y validar respuestas de forma sencilla.

----------------------------------------------------------

## 🚀 Instalación
- Clona el repositorio en tu máquina local.

- Crea y activa tu entorno virtual:
1. Crear entorno virtual
python -m venv venv

2. Activar en Windows
.\venv\Scripts\activate

3. Instala las dependencias necesarias:
pip install -r requirements.txt

----------------------------------------------------------

## ⚙️ Ejecución
- Para ejecutar toda la suite de pruebas y generar el reporte HTML automáticamente:
pytest

- Si deseas ejecutar solo pruebas específicas, usa el flag -m como se muestra en la sección de Clasificación.
----------------------------------------------------------

## 🏷️ Clasificación de Pruebas (Markers)
Este proyecto utiliza `markers` de Pytest para categorizar las pruebas y permitir una ejecución selectiva:

- smoke: Pruebas críticas y rápidas para verificar la estabilidad básica del servicio.
- regression: Pruebas completas que cubren todas las funcionalidades (incluyendo escritura y eliminación).

Puedes ejecutar grupos específicos de pruebas mediante:
### Ejecutar solo pruebas de humo
pytest -m smoke

### Ejecutar todo el conjunto de regresión
pytest -m "smoke or regression"

----------------------------------------------------------

## 📝 Reportes y Logging
Este framework genera automáticamente dos tipos de reportes tras la ejecución de las pruebas, configurados en pytest.ini:

- Reporte HTML (report.html): Un informe visual e interactivo generado en la raíz del proyecto. Permite visualizar el estado de cada test (pass/fail), su duración y los errores encontrados de manera clara.

- Logs (execution.log): Un archivo de registro detallado que contiene:

Timestamp: Fecha y hora exacta de cada interacción.

Status Codes: Validación de las respuestas HTTP recibidas.

Trazabilidad: Flujo de ejecución paso a paso para facilitar la detección de fallos.

----------------------------------------------------------

### 👩‍💻 Autor
Maria R. Narvaez

Estudiante de QA Automation.

