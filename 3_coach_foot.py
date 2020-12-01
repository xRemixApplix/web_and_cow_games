#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'FOOTBALL_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)
    dict_reponse = dict()

    # ------- CODE ICI -----------
    
    i = 0
    for joueur in data['joueurs']:
        dict_reponse[i] = joueur
        i += 1

    dict_sorted = sorted(dict_reponse.items(), key=lambda t: t[1], reverse=True)

    # ----------------------------

    reponse = '-'.join([str(elt[0]) for elt in dict_sorted[:11]])
    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()