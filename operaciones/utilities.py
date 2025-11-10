# Como la mayoría de operaciones requieren de dos números, esta función hace el trabajo de hacer los inputs 
# para ambos números, guardarlos y retornarlos cuando se use la función.
def number_input():
    results = []
    num1 = int(input('Ingresa el primer número: '))
    results.append(num1)
    num2 = int(input('Ingresa el segundo número: '))
    results.append(num2)
    return results