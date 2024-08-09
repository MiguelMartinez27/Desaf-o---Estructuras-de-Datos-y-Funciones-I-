#conversiones
#Este programa sirve para convertir pesos chilenos a soles, pesos agrentinos y dolares americanos


#librerias
import sys

#se verifica ingreso de datos correcto
if len(sys.argv) != 5:
        print("Uso: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar> <monto_pesos_chilenos>")
        sys.exit(1)
try:
        sol = float(sys.argv[1])
        peso_argentino = float(sys.argv[2])
        dolar = float(sys.argv[3])
        monto_pesos_chilenos = float(sys.argv[4])
except ValueError:
        print("Error: Todos los argumentos deben ser números.")
        sys.exit(1)

#conversion de divisas
con_sol = (sol * monto_pesos_chilenos)
con_arg = (peso_argentino * monto_pesos_chilenos)
con_dolar = (dolar * monto_pesos_chilenos)

#output
print(f"Los {monto_pesos_chilenos} equivalen a: ")
print(f"{con_sol} Soles ")
print(f"{con_arg} Pesos Argentinos")
print(f"{con_dolar} Dólares")