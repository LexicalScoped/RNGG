from PyRNGGClass import Game

def main():
    game = Game(10, 1, 100)
    while game.get_turns > 0:
        game.print_menu()
        UserInput = input()
        if game.validate_input(UserInput):
            game.add_guess(int(UserInput))
            game.decrement_turns()
            if game.check_guess(int(UserInput)):
                break
        else:
            print ("Invalid Guess")

    if game.get_turns() == 0:
        print("You ran out of turns, Game Over")

if __name__ == "__main__":
    main()