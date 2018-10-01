import requests
from random import choice
from termcolor import colored
from pyfiglet import figlet_format

title = figlet_format("DAD JOKER 2018 :D !!!")
color_title = colored(title, color = "green")
print(color_title)

word = input("Enter a word and I may be able to provide a hilarius dad joke \n")

while word:
    url = "https://icanhazdadjoke.com/search"

    res = requests.get(
        url,
        headers = {"Accept": "application/json"},
        params = {"term":word}
    )

    data = res.json()

    total_jokes = data["total_jokes"]
    jokes = data["results"]

    if total_jokes > 0:
        print("Okay, I have have {} joke(s) that can work given {}. Here is one:".format(total_jokes,word))
        print(jokes[choice(range(0,total_jokes))]["joke"])
        print("")
        play_again = input("Want to play again? (y/n)")
        if play_again == "y":
            word = input("Enter a word and I may be able to provide a hilarius comment  \n")
        else: break

    else:
        print("I don't have a joke on the topic of: {}, try another word".format(word))
        play_again = input("Want to play again? (y/n)")
        if play_again == "y":
            word = input("Enter a word and I may be able to provide a hilarius comment  \n")
        else: break

