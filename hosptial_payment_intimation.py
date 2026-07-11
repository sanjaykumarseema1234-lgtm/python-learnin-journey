name = input("enter the name:")
age = int(input("enter the age:"))
gender = input("enter you gender:")

print("welcome to \"XYZ hospital\" ")

if gender == 'male':
  print("hello", "MR", name )
else:
  print("hello", "miss", name)
  
print("you have ordered surgirical items from our hospital\n")
print("so,please collect the items now!\n")
print("you have to pay $765 ")

print("please select mode of your payment\n")
print("1.cash")
print("2.card")
print("3.cheque")

choose = int(input("choose:"))

print("thank you!\n")
print("we will make you inform when it is ready.")
