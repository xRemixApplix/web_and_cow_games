#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'FORREST_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = 0

    # ------- CODE ICI -----------
    
    reponse += data['stop']

    for i in range(len(data['kms'])):
        kms = (data['stop']-data['kms'][i])*data['runners'][i]
        reponse += kms
    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()