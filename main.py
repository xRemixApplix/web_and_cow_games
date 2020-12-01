#!/bin/python
from Game import Game

# Key personnelle
player_key = ''
# Code du challenge
engine_code = ''


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------

    reponse = ''

    # Permet d'envoyer la reponse du challenge
    # game.push({'reponse': reponse})


main()