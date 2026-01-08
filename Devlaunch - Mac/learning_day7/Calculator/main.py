import operations

calc_operations = {
    "+": operations.sum,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.division
}

op = input("Operation (+, -, *, /): ")

if op not in calc_operations:
    print("Invalid operation")
    exit()

a = float(input("Value of a: "))
b = float(input("Value of b: "))

try:
    result = calc_operations[op](a, b)
    print("Result: ", result)
except ValueError as e:
    print(e)


