num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))

add=num1+num2
sub=num1-num2
mul=num1*num2

if num2!=0:
    div=num1/num2
else:
    print("div cannot be calculated")

print(f"addition:{add}")
print(f"subtraction:{sub}")
print(f"multiplication:{mul}")
print(f"division:{div}")
