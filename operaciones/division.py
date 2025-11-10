from operaciones import utilities

def dividir():
    nums = utilities.number_input()
    print("")
    if nums[1] == 0:
        print("No se divide entre 0, escribe otro numero")
        return "//// Operación cancelada ////" # en caso de que el usuario intente dividir entre 0, se cancela la función
    return f"//// El resultado es {nums[0] / nums[1]} ////"