import random

Config = { "Turns": 10, "Rand_Min": 1, "Rand_Max": 100 }
Number = int(random.randrange(Config["Rand_Min"], Config["Rand_Max"]))
Guesses = []

while Config["Turns"] > 0:
    print ("Turns Remaining: {} - Guesses: {}".format(Config["Turns"], Guesses))
    UserInput = input("Guess a number between {} and {}: ".format(Config["Rand_Min"], Config["Rand_Max"]))
    if not UserInput.isdigit():
        print ("Invalid Guess")
        continue
    Guess = int(UserInput)
    
    if Guess in range(Config["Rand_Min"], Config["Rand_Max"]) and Guess not in Guesses:
        Guesses.append(Guess)
        Config["Turns"] -= 1
        if Guess == Number:
            print ("You guessed the Number! Congratulations")
            break
        elif Guess > Number:
            print ("Your guess is higher than the random number")
        elif Guess < Number:
            print ("Your guess is lower than the random number") 
    else:
        print ("Invalid Guess")

if Config["Turns"] == 0:
    print("You ran out of turns, Game Over")