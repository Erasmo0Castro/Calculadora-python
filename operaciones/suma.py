from operaciones import utilities

def sumar():
    nums = utilities.number_input()
    print("")
    return f'''
    ======================
    El resultado es {nums[0] + nums[1]} 
    ====================== '''
