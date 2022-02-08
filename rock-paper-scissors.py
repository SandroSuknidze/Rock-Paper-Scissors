import random

x = input("Would you like to play rock paper scissors?\nyes/no\n")
if x == "yes":
    p_input = input("Choose one: Rock, Paper or scissors?\n")
    y = random.randint(1, 3)
    if y == 1 and p_input == "scissors":
        print("Computer chose rock\nYou lost")
    elif y == 1 and p_input == "paper":
        print("Computer chose rock\nYou won")
    elif y == 1 and p_input == "rock":
        print("Computer chose rock\nIt's a tie")
    elif y == 2 and p_input == "scissors":
        print("Computer chose paper\nYou won")
    elif y == 2 and p_input == "paper":
        print("Computer chose paper\nIt's a tie")
    elif y == 2 and p_input == "rock":
        print("Computer chose paper\nYou lost")
    elif y == 3 and p_input == "scissors":
        print("Computer chose scissors\nIt's a tie")
    elif y == 3 and p_input == "paper":
        print("Computer chose scissors\nYou lost")
    elif y == 3 and p_input == "rock":
        print("Computer chose scissors\nYou won")
    else:
        print("mose")
else:
    print("Have a nice day!")
