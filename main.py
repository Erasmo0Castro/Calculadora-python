import operaciones
from operaciones import suma
from operaciones import resta
from operaciones import multiplicacion
from operaciones import division
from operaciones import porcentaje


print("""
    ____________________________________________________________________
      
    █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
    █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄
      
                            ▄▄▀█▄───▄───────▄
                            ▀▀▀██──███─────███
                            ░▄██▀░█████░░░█████░░
                            ███▀▄███░███░███░███░▄
                            ▀█████▀░░░▀███▀░░░▀██▀
    ____________________________________________________________________

""")

while True: 

    print("""
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Porcentaje
        x. Salir  
    """)

    option = (input("    –––––––  Elige una opción: "))
    print("")

    match option:
        case "1":
            print(suma.sumar())
        case "2":
            print(resta.restar())
        case "3":
            print(multiplicacion.multiplicar())
        case "4":
            print(division.dividir())
        case "5":
            print(porcentaje.porcentaje())
        case "x": 
            break