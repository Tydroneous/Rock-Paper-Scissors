import random
from math import ceil


def get_random(choice):
    random_options = choice
    return random.choice(random_options)


def compare(human, computer, my_list):
    # win_conditions = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    #
    # lose_conditions = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
    if human == computer:
        return "There is a draw ({})".format(human), 50
    else:
        human_selection = human
        computer_selection = computer
        list_to_determine = my_list
        human_element = list_to_determine.index(human_selection)
        temp_list_left = list_to_determine[0: human_element]
        if human_element < len(list_to_determine):
            temp_list_right = list_to_determine[human_element + 1:]
        new_list = temp_list_right + temp_list_left
        computer_element = new_list.index(computer_selection)
        if computer_element < (len(new_list) // 2):
            return "Sorry, but the computer chose {}".format(computer), 0
        else:
            return "Well done. The computer chose {} and failed".format(computer), 100


def classic_selection(rating, options):
    total = rating
    command = ""
    if options == ['']:
        options = ['rock', 'paper', 'scissors']

    while command != "!exit":
        command = input()
        if command == "!rating":
            print("Your rating: {}".format(total))
        elif command in options:
            computer_selection = get_random(options)
            output, score_add = (compare(command, computer_selection, options))
            total += score_add
            print(output)
        elif command == "!exit":
            continue
        else:
            print("Invalid input")
    else:
        print("Bye!")


def start():
    name = input("Enter your name: ")

    print("Hello, {}".format(name))
    my_file = open("rating.txt", "r")

    for line in my_file:
        if name in line:
            temp = line.strip("\n").split(" ")
            rating = int(temp[1])
            break
        else:
            rating = 0

    choices = input().split(",")
    print("Okay, let's start")
    classic_selection(rating, choices)


start()
