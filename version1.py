def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        print("divison cannot be calculated")

num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))

print(f"addition:{add(num1,num2)}")
print(f"subtraction:{sub(num1,num2)}")
print(f"multiplication:{mul(num1,num2)}")
print(f"division:{div(num1,num2)}")
