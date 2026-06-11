def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def dev(a,b):
    return a / b

print("select opreation")
print("1: Addition")
print("2: Substraction")
print("3: Multyplication")
print("4: Devision")

user_choice = input("select choice (1/2/3/4)   ")

num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))

if user_choice == "1":
    print(add(num1,num2))
elif user_choice == "2":
    print(sub(num1,num2))
elif user_choice == "3":
    print(mult(num1,num2))
elif user_choice == "4":
    print(dev(num1,num2))
else:
    print("invalid input")
