def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def dvd(a,b):
    return(a/b)

print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.division")

choose = input("choose : ")

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

if choose == '1':
    print("answer = ",add(num1,num2))
elif choose == '2':
    print("answer = ",sub(num1,num2))
elif choose == '3':
    print("answer = ",mul(num1,num2))
elif choose == '4':
    print("answer = ",dvd(num1,num2))
else :
    print("invalid option! pick: 1,2,3 or 4")

