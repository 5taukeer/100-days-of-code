def add (x , y):
     return x+y
def sub (x , y):
    return x - y
def mul (x , y):
    return x * y
def div (x , y):
    return x / y
print ("select operation")
print ("+")
print ("-")
print ("*")
print ("/")
choice = input ("enter choice:")
op1 = int(input("Enter num1 : "))
op2 = int(input("Enter num2 : "))
if choice == '+':
    print(op1,"+",op2,"=", add(op1,op2))
elif choice == '-':
   print(op1,"-",op2,"=", sub(op1,op2))
elif choice == '*':
   print(op1,"*",op2,"=", mul(op1,op2))
elif choice == '/':
   print(op1,"/",op2,"=", div(op1,op2))
else:
   print("invalid input")

