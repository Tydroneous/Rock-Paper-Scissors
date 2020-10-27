import random


def get_random():
    random_options = ["rock", "paper", "scissors"]
    return random.choice(random_options)


def compare(human, computer):
    win_conditions = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

    lose_conditions = {"rock": "paper", "scissors": "rock", "paper": "scissors"}

    if win_conditions[human] == computer:
        return "Well done. The computer chose {} and failed".format(computer)
    elif lose_conditions[human] == computer:
        return "Sorry, but the computer chose {}".format(computer)
    else:
        return "There is a draw ({})".format(human)


def start():
    options = ["rock", "paper", "scissors"]
    selection = ""
    while selection != "!exit":
        selection = input("Please enter an option\n")
        if selection in options:
            computer_selection = get_random()
            print(compare(selection, computer_selection))
        elif selection == "!exit":
            continue
        else:
            print("Invalid input")
    else:
        print("Bye!")


start()
