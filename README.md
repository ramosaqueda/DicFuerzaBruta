
## Descripción General

FuerzaBruta es una aplicación de escritorio desarrollada en Python que permite generar diccionarios personalizados para pruebas de seguridad. La aplicación utiliza PyQt5 para su interfaz gráfica y permite al usuario crear combinaciones de palabras basadas en información conocida sobre un objetivo (nombres, fechas importantes, lugares, etc.).

Desarrollado por:
- Carlitos de la V (Desarrollo principal)
- Rafa Ramos, Coquimbo (Interfaz gráfica) y otras opciones XD-

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

### 2. Instalar PyQt5

PyQt5 es la biblioteca utilizada para la interfaz gráfica. Instálala usando pip:

```bash
pip install PyQt5
```

### 3. Descargar el Código Fuente

Descarga el archivo `FuerzaBruta.py` y guárdalo en una carpeta de tu elección.

### 4. Preparar el Logo

La aplicación busca un archivo llamado `logo.png` en el mismo directorio. Debes:

1. Obtener o crear un archivo de imagen llamado `logo.png`
2. Colocarlo en la misma carpeta donde guardaste `FuerzaBruta.py`

> **Nota**: Si no deseas usar un logo, puedes modificar el código para omitir esta funcionalidad.

### 5. Ejecutar la Aplicación

Una vez instalados todos los requisitos:

```bash
python FuerzaBruta.py
```

O en algunos sistemas:

```bash
python3 FuerzaBruta.py
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

- **Error al iniciar**: Verifica que PyQt5 esté correctamente instalado
- **Logo no visible**: Asegúrate de tener un archivo `logo.png` en la misma carpeta
- **Problemas de codificación**: La aplicación guarda usando UTF-8, si hay problemas con caracteres especiales, verifica la configuración de tu sistema

## Información Adicional

Esta herramienta está diseñada para pruebas de seguridad legítimas. Úsala con responsabilidad y solo en sistemas para los que tengas autorización explícita.
