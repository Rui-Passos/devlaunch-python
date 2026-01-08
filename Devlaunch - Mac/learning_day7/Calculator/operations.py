def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b

    
def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Not possible to divide by 0")
    return a / b