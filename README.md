# Lenguajes de Programación y Transducción
## Parcial Segundo Corte
### Juan Camilo

---

# Punto 1

# Lenguaje para Operaciones con Números Complejos

Este proyecto implementa un lenguaje que permite realizar operaciones con números complejos, como suma y resta, utilizando ANTLR para generar el parser y Python como lenguaje de destino.

## Requisitos

- Python 3.12.x
- ANTLR 4.13.2
- Librerías de ANTLR para Python (`antlr4-python3-runtime==4.13.2`)

## Instalación

1. Clonar el repositorio o descargar los archivos del proyecto.

2. Crear un entorno virtual para instalar las dependencias:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar la versión correcta del runtime de ANTLR para Python:

   ```bash
   pip install antlr4-python3-runtime==4.13.2
   ```


## Generación de los archivos de ANTLR

1. Para generar los archivos del lexer y parser, usa el siguiente comando:

   ```bash
   antlr4 -Dlanguage=Python3 Complejos.g4
   ```

   Esto generará los archivos `ComplejosLexer.py`, `ComplejosParser.py`, y otros archivos necesarios.

## Ejecución del Programa

1. Después de generar los archivos con ANTLR, puedes ejecutar el programa de pruebas. Usa el archivo `test_complejos.py` para ingresar expresiones con números complejos y obtener los resultados.

2. Ejecuta el programa con el siguiente comando:

   ```bash
   python3 test_complejos.py
   ```

3. Ingresa expresiones con números complejos, por ejemplo:

   ```text
   (2 + 3i) + (1 - 2i)
   ```
   El archivo pruebas.txt contiene diversos casos de prueba para usar y probar el programa y la gramática 

   El programa evaluará la expresión y te mostrará el resultado.


## Estructura del Proyecto

- `Complejos.g4`: Archivo de gramática que define las reglas del lenguaje para los números complejos.
- `test_complejos.py`: Script de prueba para evaluar las expresiones con números complejos.
- `ComplejosLexer.py` y `ComplejosParser.py`: Archivos generados por ANTLR que definen el lexer y el parser.

## Estructura del proyecto

```plaintext
├── Complejos.g4       # Gramática ANTLR para números complejos
├── test_complejos.py                     # Script principal que parsea el caso a probar
├── pruebas.txt                  # Archivo de entrada con ejemplos de MAP y FILTER
├── venv/                       # Entorno virtual de Python
```

##Nota
Envio todos los archivos para probar directamente pues ANTLR4 compila mal la libreria cmath. Para compilarlo nuevamente, hay que modificar el Lexer, Listener o Parser ubicando bien la libreria al inicio dependiendo del erorr o lugar del error al compilar con ANTLR4.






#Punto2

## Implementación de funciones MAP y FILTER en ANTLR

Este proyecto implementa un lenguaje que permite aplicar funciones como `MAP` y `FILTER` sobre listas y tuplas en Python, utilizando una gramática definida en ANTLR.

## Requisitos

- Python 3.12.x
- ANTLR 4
- ANTLR4 Python runtime
- Entorno virtual

### Instalación de dependencias


1. **Crear y activar un entorno virtual**
   Si prefieres aislar las dependencias en un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

2. **Instalar dependencias en el entorno virtual (si aplica):**

   Si has creado un entorno virtual, instala el runtime de ANTLR dentro de él:

   ```bash
   pip install antlr4-python3-runtime
   ```

## Estructura del proyecto

```plaintext
├── FuncionesIterables.g4       # Gramática ANTLR para las funciones MAP y FILTER
├── main.py                     # Script principal que parsea el archivo de entrada
├── prueba.txt                  # Archivo de entrada con ejemplos de MAP y FILTER
├── venv/                       # (Opcional) Entorno virtual de Python
```

## Uso

### 1. Generar el código de ANTLR en Python

Antes de ejecutar el programa, necesitas generar los archivos de Python a partir de la gramática ANTLR. Usa el siguiente comando:

```bash
antlr4 -Dlanguage=Python3 FuncionesIterables.g4
```

Esto generará varios archivos Python que ANTLR utilizará para el análisis sintáctico y léxico.

### 2. Crear el archivo de entrada

En tu archivo de entrada (`prueba.txt`), debes incluir las llamadas a las funciones `MAP` y `FILTER` con el siguiente formato, asegurándote de finalizar cada statement con un punto y coma (`;`):

```plaintext
MAP(multiply, [1, 2, 3]);
FILTER(is_even, (4, 5, 6));
```

### 3. Ejecutar el programa

Finalmente, puedes ejecutar el programa de la siguiente manera, asegurándote de tener activado el entorno virtual (si lo estás utilizando):

```bash
python main.py prueba.txt
```

### 4. Resultado esperado

El programa procesará las llamadas a las funciones `MAP` y `FILTER` y mostrará el resultado en la consola. Por ejemplo, para el archivo de entrada `prueba.txt`:

```plaintext
Resultado de MAP(multiply, [1, 2, 3]): [2, 4, 6]
Resultado de FILTER(is_even, (4, 5, 6)): [4, 6]
```

## Notas adicionales

- Puedes personalizar las funciones `MAP` y `FILTER` modificando el código en `main.py`.




#Punto3

---

# Fourier Transform Language

Este proyecto implementa un lenguaje de programación simple que calcula la **Transformada de Fourier**, la **Transformada Inversa de Fourier**, y permite consultar pares transformados asociados a frecuencias.

## Requisitos

- **Python 3.12+**
- **ANTLR4**
- **Numpy** 
- **Virtualenv**

### Instalación de Dependencias

1. Clona el repositorio o copia los archivos del proyecto en tu máquina local.

2. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias requeridas:

   ```bash
   pip install numpy antlr4-python3-runtime
   ```

## Generación del Lexer y Parser

Una vez que tengas los archivos de gramática (`FourierLexer.g4` y `FourierParser.g4`), genera los archivos de ANTLR ejecutando:

```bash
antlr4 -Dlanguage=Python3 -visitor FourierLexer.g4 FourierParser.g4
```

Esto generará los archivos necesarios para el lexer y el parser.

## Estructura de Archivos

```
│
├── FourierLexer.g4              # Definición del lexer de ANTLR
├── FourierParser.g4             # Definición del parser de ANTLR
├── FourierVisitorImpl.py        # Implementación de las funciones de Fourier y Visitor
├── FourierParserVisitor.py      # Visitor generado por ANTLR
├── FourierLexer.py              # Lexer generado por ANTLR
├── FourierParser.py             # Parser generado por ANTLR
├── main.py                      # Archivo principal que ejecuta el programa
├── input.txt                    # Archivo de entrada con las instrucciones a procesar
└── venv/                        # Entorno virtual
```

## Ejecución del Programa

### 1. Preparar el Archivo de Entrada

El archivo `input.txt` debe contener las instrucciones del lenguaje para ejecutar las transformadas. 

### 2. Ejecutar el Programa

Ejecuta el programa pasando como argumento el archivo de entrada `input.txt`:

```bash
python3 main.py input.txt
```

El programa procesará las instrucciones y mostrará los resultados de las transformadas en la terminal.

## Explicación del Lenguaje

El lenguaje soporta las siguientes operaciones:

- **Transformada de Fourier**: `fourier_transform([a, b, c, ...])`
  - Calcula la transformada de Fourier de la secuencia `[a, b, c, ...]`.
  
- **Transformada Inversa de Fourier**: `inverse_fourier_transform([a, b, c, ...])`
  - Calcula la transformada inversa de Fourier de la secuencia `[a, b, c, ...]`.

- **Consulta de pares transformados**: `get_transform_pair(frequency)`
  - Consulta el par transformado asociado a una frecuencia dada.

## Personalización

Puedes modificar el archivo `FourierVisitorImpl.py` para agregar más funcionalidades o cambiar el comportamiento de las operaciones.

## Notas

- Asegúrate de tener correctamente configurado el entorno virtual y todas las dependencias antes de ejecutar el programa.
- Si no ves el resultado esperado, verifica que el archivo de entrada `input.txt` está correctamente formateado y sigue las reglas de la gramática definida.

---
