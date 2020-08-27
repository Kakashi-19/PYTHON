eggs = 10
def good():
    global eggs # to define eggs as a global variable
    eggs = 20 # assignment makes it a local variable unless its is assigned as a global
    print(eggs)
good()
print(eggs) # since eggs is defined as a global variable its value will be changed after good() is called   
