import random

random = random.randint (1, 100)
guess = int(input("guess a number between 1 and 100 :"))
match guess :
    case _ if guess == random :
        print("you are lucky drain more money in for more wailth :)")
    case __ :
        print("every gambler has to start somewhere try again")
print(f"the correct number was : {random}")

