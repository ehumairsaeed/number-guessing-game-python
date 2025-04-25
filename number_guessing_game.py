
import random

target = random.randint(1,100)


while True:
    usr_num = input("Guess a Number or Quite :")
    if usr_num == "Quite":
        break
    usr_num = int(usr_num)
    if usr_num == target:
        print("Success : Correct Guess !!")
        break
    elif usr_num<target:
        print("Your guessed number is too small. Guess Bigger nunber....")
    else:
        print("Your guessed number is too large. Guess Small nunber....")

print("----GAME OVER----")