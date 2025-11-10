# Como la mayoría de operaciones requieren de dos números, esta función hace el trabajo de hacer los inputs 
# para ambos números, guardarlos y retornarlos cuando se use la función.
def number_input():
    while True:

        try:
            num1 = int(input('Ingresa el primer número: '))
            num2 = int(input('Ingresa el segundo número: '))
            return [num1, num2]

        except ValueError:
            print("Error: solo puede calcular con numeros, no letras, intente otra vez.\n")