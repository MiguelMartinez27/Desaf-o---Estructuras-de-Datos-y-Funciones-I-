# Desafío - Estructuras de Datos y Funciones (I)
##### Desafío - Estructuras de Datos y Funciones (I) correspondiente al bootcamp fullstack python.
Este repositorio contiene los archivos para ejecutar "conversiones.py", "word_count.py" y "recordatorios.py". estos incluyen el uso de datos y funciones en python.

## Requisitos para ejecutar
* Sistema operativo Windows, MacOS o Linux
* Python 3.12 o superior

## Programas

### 1.- conversión

Este programa convertirá pesos chilenos a sol, peso argentino y dolares, ingresando las tasas de conversión y la cantidad de pesos chilenos a convertir

#### Ejecución
* Ejecutar por terminal conversiones.py junto con los argumentos correspondientes a las tasas de conversion de:
  * Sol
  * Peso Argentino
  * Dólar Americano
  * Además, ingresa un cuarto argumento que sea el valor en pesos chilenos a convertir.

* El programa debe devolver el valor en pesos chilenos convertido en las tres divisas ingresadas.

*Tasas de conversión de Peso Chileno:*
* Sol peruano: 0.0046
* Peso Argentino: 0.093
* Dólar Americano: 0.00013

#### Ejemplo:

sh

python conversiones.py 0.0046 0.093 0.00013 10000

Respuesta esperada:

Los 10000 pesos equivalen a:

46.0 Soles

930.0 Pesos Argentinos

13.0 Dólares

### 2.- word count
Este programa al ejecutarlo importara un texto desde un archivo y realizara las siguientes tareas:

Entregar la cantidad de caracteres distintos que componen el texto.

Entregar el número de palabras distintas que componen el texto ingresado.

#### Ejecución

* Ejecutar por terminal agregando el argumento, es decir el nombre del archivo (y la direccion de ser necesario) del que desea importar el texto y contar sus caracteres y palabras.
* el programa entregará el conteo de los distintos caracteres y distintas palabras en el texto.

#### Ejemplo

sh

python word_count.py lorem_ipsum.txt

Respuesta esperada:

El número de caracteres distintos es: 40

El número de palabras distintas es: 241

### 3.- Recordatorios

Este programa es un recordatorio de algunas tareas y actividades en determinados dias

como parte del desafio este recordatorio a sido editado a través de funciones

#### Ejecución

ejecutar por terminal el programa

#### Ejemplo

sh

python recordatorio.py

Respuesta esperada:

[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
['2021-01-02', '06:00', 'Empezar el año'],
['2021-07-16', '13:00', 'No hacer nada es feriado'],
['2021-09-18', '16:00', 'Ramadas'],
['2021-12-24', '22:00', 'Cena de Navidad'],
['2021-12-25', '00:00', 'Navidad'],
['2021-12-31', '22:00', 'Cena de Año Nuevo']]


## Autor

Grupo 1 Bootcamp Full Stack python talento digital G20
