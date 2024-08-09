#librerias
import sys

#importar texto
lorem = sys.argv[1]

with open(lorem, "r") as file:
    texto = file.read()

#contar caracteres
cont_car = len(set(texto))

#contar palabras
palabras = texto.split()
cont_pal = len(set(palabras))

print(f"El número de caracteres distintos es: {cont_car}")
print(f"El número de palabras distintas es: {cont_pal}")