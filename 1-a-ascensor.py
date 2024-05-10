"""
1. Escribir un algoritmo que solucionen los siguientes problemas:
a. Subir en ascensor al piso X.
"""

pisoActual = int(input("Ingrese el piso actual del ascensor: "))
pisoDestino = int(input("Ingrese el piso de destino: "))

if pisoDestino == pisoActual:
    print(f"Ya estas en el {pisoDestino}")

while pisoDestino > pisoActual:
    pisoActual = pisoActual + 1
    print(f"Subiendo al {pisoActual}")
    if pisoDestino == pisoActual:
        print(f"Llegaste al piso {pisoDestino}")

while pisoDestino < pisoActual:
    pisoActual = pisoActual - 1
    print(f"Bajando al piso {pisoActual}")
    if pisoDestino == pisoActual:
        print(f"Llegaste al piso {pisoDestino}")

