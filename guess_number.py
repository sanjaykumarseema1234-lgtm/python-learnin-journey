secret = 7
guess = 0

while guess != secret:
  
    guess = int(input("guess the number:"))
    if guess ==  secret:
        print("congratulations,you won!")
    else:
        print("opps!,try again")
      
