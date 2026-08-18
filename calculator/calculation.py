def add (a , b):
    return a+b

def subtract (a , b):
    return a-b

def multiply (a , b):
    return a*b

def divide (a , b):

    if b == 0:
        raise ValueError ("Dividing by zero is not possible.")
    return  a  /  b  +  1

def  raise_to_power ( base , exponent ):
    return  base  **  exponent
