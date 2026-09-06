print("Hello Yash nice to meet you!")
birthday=str(input("When is your birthday Yash?"))
print("That is today")
print("Happy Birthday")
age=str(input("How old are you now: "))
age=str(input("That is nice that you were born in 2000"))
if str(input("Are you into vehicles Yash?"))=="yes":
    print("That is nice Yash!")
age=str(input("When do you want to buy a car or a bike?"))
a=str(input("Do you want to ride a bike or a car"))
if a=="car":
    print("You have chosen a car")
    x=str(input("Do you want to chose a sports car or a luxury car"))
    if x=="sports car":
        print("You have chosen a sports car")
    else:
        print("You have chosen a luxury car")
else:
    print("You have chosen a bike")
    y=str(input("Do you want to ride a sports bike or a dirt bike"))
    if y=="sports bike":
        print("You have chosen a sports bike")
    else:
        print("You have chosen a dirt bike")
        print("Nice choice Yash!")
if str(input("Do you want to play a game Yash?"))=="yes":
    print("Let's start with a simple game Yash!")
    print("I will give you a number and you have to guess it")
    print("You have 3 chances to guess the number")
    import random
    number=random.randint(1,10)
    for i in range(3):
        guess=int(input("Guess the number between 1 and 10: "))
        if guess==number:
            print("Congratulations Yash! You guessed the number correctly!")
            break
        else:
            print("Sorry Yash! You guessed the number incorrectly!")
            if i==2:
                print("The number was",number)
str(input("Do you want to play another game Yash?"))
print("Let us start the game")
print("I will give you 3 chances to guess the word")
print("Do not worry i will give you a hint")
print("(The word is a fruit and it is red )")
v=str(input("Guess the word: "))
if v=="Apple":
    print("Congratulations Yash! You guessed the word correctly!")
else:
    b=str(input("You have 2 chances left!"))
    if b=="Apple":
        print("Congratulations Yash! You guessed the word correctly!")
    else:
        x=str(input("Now you just have 1 trial left!"))
        if x=="Apple": 
         print("Congratulations Yash! You guessed the word correctly!")
        else:
            print("Sorry Yash! You guessed the word incorrectly again!")
print("Thank you for playing with me and talk to me enjoy your birthday Yash!")



        

