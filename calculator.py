def operation(first,second,operator):

    if(operator == 1):
        return first + second
    if(operator == 2):
        return first - second
    if(operator == 3):
        return first / second
    if(operator == 4):
        return first * second

    return "invalid selection or input"  



print("Welcome to calculator.py, please enter 2 values to perform an operation")
firstValue = float(input("What is the first value? \n"))
secondValue = float(input("What is the second value? \n"))

print("Available operations")
print("1. add - add two numbers")
print("2. sub - subtract two numbers")
print("3. div - divide two numbers")
print("4. mul - multiply two numbers")

operator = int(input("What operation would you like to perform? \n"))


print(operation(firstValue,secondValue,operator))


