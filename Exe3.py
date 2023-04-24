mynum = 25
num1 = int(input("Enter number : \n"))
i = 1
while(i<6):

    if num1 == mynum:
                     print("Your Won.")
                     print("You take Number of guess is ", i);
                     break
    elif num1 > mynum:
                      print("Please enter samller number")
                      print("Your number of guess remming " ,5-i)
    elif num1 < mynum:
                      print("Please enter big number")
                      print("Your number of guess remming ", 5 - i)
    num1  = int(input("Enter number : \n"))
    i= i+1
    if i == 6:
              print("Game Over. Please try again")







