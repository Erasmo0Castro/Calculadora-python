from operaciones import utilities

def porcentaje():
    nums = utilities.number_input()
    print("")
    if nums[1] == 0:
        print("Elige otro numero final ya que porcentaje no puede ser 0")
        return "//// Operación cancelada ////"
    return f'''
    ======================
    El resultado es {(nums[0] / nums[1]) * 100} 
    ====================== '''