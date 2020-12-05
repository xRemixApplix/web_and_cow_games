#!/bin/python
from Game import Game
from datetime import datetime

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'FUTURE'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = 0

    # ------- CODE ICI -----------
    
    month, day = [int(elt) for elt in data['anniversaire'].split('-')]
    anniversaire_1985 = datetime(1985, month, day)

    print('----------------------------')

    for saut in data['sauts']:
        year, month, day = [int(elt) for elt in saut.split('-')]
        ecart = (datetime(year, month, day)-anniversaire_1985).days//365
        ecart = ecart if ecart>0 else ecart+1
        print(saut, '---------->', ecart)

        reponse += ecart

    print('----------------------------')

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()