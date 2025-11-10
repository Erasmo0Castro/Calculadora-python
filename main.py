import operaciones
from operaciones import suma


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

while True: #git fetch origin
#git merge origin/main

    print("""
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        x. Salir  
    """)

    option = (input("    –––––––  Elige una opción: "))
    print("")

    match option:
        case "1":
            print(suma.sumar())
        case "x": 
            break