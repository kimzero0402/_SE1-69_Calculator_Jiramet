### version 1.0(jiramet)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

#-------Main function to run the calculator-------#
print("Simple calculator by Jiramet :")
num1 = float(input("กรุณากรอกตัวเลขที่ 1: "))
num2 = float(input("กรุณากรอกตัวเลขที่ 2: "))

print("_"*25)
print("Addition (+):", add(num1,num2)) 