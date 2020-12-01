#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'PIERRE_FEUILLE_CISEAUX'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data['coups'])

    reponse = ''

    # ------- CODE ICI -----------
    for coup in data['coups']:
        if coup == 'P':
            reponse += 'F'
        elif coup == 'F':
            reponse += 'C'
        elif coup == 'C':
            reponse += 'P'
    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()