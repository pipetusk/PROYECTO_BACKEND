# FIT Core - Backend para App de Fitness

## Propósito del Proyecto

Sistema diseñado para digitalizar la gestión de rutinas y el progreso deportivo. La plataforma soluciona la distribución de la información en distintos registros al centralizarlos entre usuarios y entrenadores. Permite almacenar antecedentes históricos, controlar situaciones excepcionales, validar reglas de negocio, entre otros. Además, contiene indicadores de gestión para analizar tendencias, actividad reciente, utilización de recursos y comportamiento de los usuarios.

## Instrucciones de instalación y ejecución

Pasos para levantar el entorno virtual desde 0:

1. **Clonar el repositorio desde GitHub.**

2. **Crear el ambiente virtual:**
   ```
   python -m venv ambiente
   ```

3. **Activar el ambiente virtual (Windows PowerShell):**
   ```bash
   .\ambiente\Scripts\Activate
   ```

    - Si PowerShell bloquea la ejecución:
    ```
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

4. **Instalar dependencias:**
   ```
   pip install -r requirements.txt
   ```

5. **Iniciar el servidor Django:**
   ```
   python manage.py runserver
   ```

6. **Verificación de Rutas:**
   - **Vista de Bienvenida:** Ingresa a `http://127.0.0.1:8000/` para ver el panel principal.
   - **Error 404:** Ingresa a `http://127.0.0.1:8000/hola` u otra ruta para validar el diseño de la página de error personalizada.

## Instalar base de datos

**RECUERDA** iniciar WampServer antes de iniciar.

1. Crear la base de datos en el WAMPSERVER, con MySQL. Agrupé todos los comandos para hacer todo de una.
```
CREATE DATABASE IF NOT EXISTS fitness_db;
CREATE USER IF NOT EXISTS 'Fitness'@'%' IDENTIFIED BY 'fit12345';
GRANT ALL PRIVILEGES ON fitness_db.* TO 'Fitness'@'%';
FLUSH PRIVILEGES;
```

2. Aplica el `migrate` para poder clonar los datos de la base de datos:

```
python manage.py migrate
```

- En caso de que se quiera añadir cambios, usa este comando:
   ```
   python manage.py makemigrations
   ```


3. Crea la cuenta de acceso a Admin:
   - Se ingresa el nombre, correo (no es necesario) y contraseña.

```
python manage.py createsuperuser
```

