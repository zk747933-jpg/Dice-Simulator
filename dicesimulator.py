import random

def roll_dice():
    number = random.randint(1,6)
    print(f"\n you rolled a {number}!\n")

print("welcome to dice simulator")
while True:
    input("press enter to roll the dice")
    roll_dice()

    again = input("roll again (y/n):").lower()
    if again != 'y':
        print("thanks for playiing")
        break




