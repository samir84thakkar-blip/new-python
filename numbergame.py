import random
number=random.randint(0,10)
try:
    guess=int(input("guess number correct"))
except ValueError:
    print("Please enter a valid number.")
    guess=None
if guess==number:
    print("You have a hero because you have guessed the number correctly!")
else:
    print("You guessed the number incorrectly!")
    

