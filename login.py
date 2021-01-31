import time

username="Swapnadeep"
password="doggo369"
turn = 3
while (turn > 0):
    var=input("Enter the username: ")
    char=input("Enter the Password: ")

    if(var != username and char != password):
        print("Wrong username and password ")
        turn -= 1
        print("you have", turn ,"attempts left")
        
    elif(var == username and char != password):
        print("Wrong Password ")
        turn -= 1
        print("you have", turn ,"attempts left")
        
    elif(var != username and char == password):
        print("Wrong Username ")
        turn -= 1
        print("you have", turn ,"attempts left")
        
    else:
        print(" Access Granted ")
        time.sleep(3)
        print("...........loading.......Please wait!.......")
        time.sleep(5)
        print("Transfering to the main page ")
        break

if(turn == 0):
    print("You have made several wrong attempts, Come after some time!")