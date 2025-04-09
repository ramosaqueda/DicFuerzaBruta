# Instrucciones de Instalación - FuerzaBruta

## Descripción General

FuerzaBruta es una aplicación de escritorio desarrollada en Python que permite generar diccionarios personalizados para pruebas de seguridad. La aplicación utiliza PyQt5 para su interfaz gráfica y permite al usuario crear combinaciones de palabras basadas en información conocida sobre un objetivo (nombres, fechas importantes, lugares, etc.).

Desarrollado por:
- Carlitos de la V (Desarrollo principal)
- Rafa Ramos, Coquimbo (Interfaz gráfica)

## Requisitos Previos

Para instalar y ejecutar FuerzaBruta, necesitarás:

1. Python 3.6 o superior
2. Pip (gestor de paquetes de Python)
3. PyQt5

## Pasos de Instalación

### 1. Instalar Python

Si aún no tienes Python instalado:

- **Windows**: Descarga e instala Python desde [python.org](https://www.python.org/downloads/)
- **macOS**: 
  ```bash
  brew install python
  ```
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

### 2. Crear un Entorno Virtual (recomendado)

Es altamente recomendable usar un entorno virtual para evitar conflictos con otras aplicaciones Python:

**Windows**:
```bash
# Crear el entorno virtual
python -m venv venv_fuerzabruta

# Activar el entorno virtual
venv_fuerzabruta\Scripts\activate
```

**macOS/Linux**:
```bash
# Crear el entorno virtual
python3 -m venv venv_fuerzabruta

# Activar el entorno virtual
source venv_fuerzabruta/bin/activate
```

Una vez activado el entorno virtual, tu línea de comandos debería mostrar `(venv_fuerzabruta)` al inicio, indicando que estás trabajando dentro del entorno virtual.

### 3. Instalar PyQt5

PyQt5 es la biblioteca utilizada para la interfaz gráfica. Instálala usando pip (dentro del entorno virtual):

```bash
pip install PyQt5
```

### 4. Descargar el Código Fuente

Descarga el archivo `FuerzaBruta.py` y guárdalo en una carpeta de tu elección.

### 5. Preparar el Logo

La aplicación busca un archivo llamado `logo.png` en el mismo directorio. Debes:

1. Obtener o crear un archivo de imagen llamado `logo.png`
2. Colocarlo en la misma carpeta donde guardaste `FuerzaBruta.py`

> **Nota**: Si no deseas usar un logo, puedes modificar el código para omitir esta funcionalidad.

### 6. Ejecutar la Aplicación

Asegúrate de que el entorno virtual esté activado y ejecuta:

**Windows**:
```bash
# Desde el entorno virtual activado
python FuerzaBruta.py
```

**macOS/Linux**:
```bash
# Desde el entorno virtual activado
python3 FuerzaBruta.py
```

### 7. Desactivar el Entorno Virtual (cuando termines)

Cuando hayas terminado de usar la aplicación, puedes desactivar el entorno virtual con:

```bash
deactivate
```

## Uso de la Aplicación

1. Completa los campos con la información relevante:
   - Nombres/Apodos
   - Fechas importantes
   - Números de ID
   - Lugares
   - Intereses
   - Frases

2. Haz clic en "Generar Vista Previa" para ver las primeras 100 combinaciones generadas.

3. Haz clic en "Guardar Diccionario" para guardar todas las combinaciones en un archivo de texto.

4. Usa "Limpiar Campos" para reiniciar el formulario.

## Funcionalidades

- Genera combinaciones de 1 a 3 elementos a partir de los datos ingresados
- Elimina espacios y caracteres especiales automáticamente
- Incluye patrones comunes como "1234", "0000", etc.
- Guarda el diccionario en formato de texto plano (.txt)
- Muestra una vista previa antes de guardar

## Resolución de Problemas

- **Error al iniciar**: Verifica que PyQt5 esté correctamente instalado y que estás ejecutando desde el entorno virtual
- **Logo no visible**: Asegúrate de tener un archivo `logo.png` en la misma carpeta
- **Problemas de codificación**: La aplicación guarda usando UTF-8, si hay problemas con caracteres especiales, verifica la configuración de tu sistema
- **Entorno virtual no funciona**: Comprueba que estás usando la versión correcta de Python y que tienes permisos para crear carpetas en la ubicación seleccionada
- **Comando "venv" no reconocido**: En algunas distribuciones de Linux, puede ser necesario instalar el módulo venv por separado con `sudo apt install python3-venv`

## Información Adicional

Esta herramienta está diseñada para pruebas de seguridad legítimas. Úsala con responsabilidad y solo en sistemas para los que tengas autorización explícita.
