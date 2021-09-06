import random

class Game:
    def __init__(self, Turns=10, rMin=1, rMax=100):
        self.Turns = Turns
        self.Rand_Min = rMin
        self.Rand_Max = rMax
        self.Number = int(random.randrange(rMin,rMax))
        self.Guesses = []
    def get_turns(self):
        return self.Turns
    def decrement_turns(self):
        self.Turns -= 1
    def get_guesses(self):
        return self.Guesses
    def add_guess(self, Guess):
        self.Guesses.append(Guess)

    def check_guess(self, UserGuess):
        if UserGuess > self.Number:
            print ("Your guess is higher than the random number")
            return False
        elif UserGuess < self.Number:
            print ("Your guess is lower than the random number") 
            return False
        elif UserGuess == self.Number:
            print ("Congratulations, you guessed the number!") 
            return True

    def print_menu(self):
        print ("Turns Remaining: {} - Guesses: {}".format(self.Turns, self.Guesses))
        print ("Guess a number between {} and {}:".format(self.Rand_Min, self.Rand_Max), end =" ")

    def validate_input(self, UserInputData):
        if (
            UserInputData.isdigit()
            and int(UserInputData) in range(self.Rand_Min, self.Rand_Max)
            and int(UserInputData) not in self.Guesses ):
            return True
        else:
            return False