
import random

target = random.randint(1,100)


while True:
    usr_num = int(input("Guess a Number :"))
    if usr_num == target:
        print("Success : Correct Guess !!")
        break
    elif usr_num<target:
        print("Your guessed number is too small. Guess Bigger nunber....")
    else:
        print("Your guessed number is too large. Guess Small nunber....")

print("----GAME OVER----")