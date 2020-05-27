import json
import difflib


def searchWord(word):
    word = word.lower()
    with open("data.json") as jsondatafile:
        datadict = json.load(jsondatafile)
        if word in datadict:
            for meaning in datadict[word]:
                print(meaning)
        elif word.title() in datadict:
            for meaning in datadict[word.title()]:
                print(meaning)
        elif len(difflib.get_close_matches(word, datadict.keys(), cutoff=0.5)) > 0:
            suggestion = difflib.get_close_matches(word, datadict.keys(), cutoff=0.5)[0]
            print("The word '{user_word}' doesnt exist. Did you mean '{suggest}'?".format(user_word=word.capitalize(), suggest=suggestion.capitalize()))
            user_choice = input("Enter your choice(Y/N): ")
            user_choice = user_choice.upper()
            if user_choice == "Y":
                for meaning in datadict[suggestion]:
                    print(meaning)
            elif user_choice == "N":
                user_choice2 = input("Do you like to enter the word again?? (Y/N): ")
                user_choice2 = user_choice2.upper()
                if user_choice2 == "Y":
                    main_prog()
                else:
                    print("Thanks for using the program. Existing")
            else:
                print("Not a valid input. Exiting. Thank you!!")
        else:
            print("Word doesnt exist. Please re-enter")


def main_prog():
    user_word = input("Enter the word: ")
    searchWord(user_word)


main_prog()
