import random

Config = { "Turns": 10, "Rand_Min": 1, "Rand_Max": 100 }
Number = int(random.randrange(Config["Rand_Min"], Config["Rand_Max"]))
Guesses = []

def PrintMenu():
    print ("Turns Remaining: {} - Guesses: {}".format(Config["Turns"], Guesses))
    print ("Guess a number between {} and {}:".format(Config["Rand_Min"], Config["Rand_Max"]), end =" ")

def ValidateInput(UserInputData):
    if not UserInputData.isdigit():
        return False
    if int(UserInputData) not in range(Config["Rand_Min"], Config["Rand_Max"]):
        return False
    if int(UserInputData) in Guesses:
        return False
    else:
        return True

def CheckGuess(UserGuess):
    if UserGuess > Number:
        print ("Your guess is higher than the random number")
    if UserGuess > Number:
        print ("Your guess is lower than the random number") 
    if UserGuess == Number:
        return True

def main():
    while Config["Turns"] > 0:
        PrintMenu()
        UserInput = input()
        if ValidateInput(UserInput):
            Guess = int(UserInput)
            Guesses.append(Guess)
            Config["Turns"] -= 1
            if CheckGuess(Guess):
                break
        else:
            print ("Invalid Guess")

    if Config["Turns"] == 0:
        print("You ran out of turns, Game Over")

if __name__ == "__main__":
    main()