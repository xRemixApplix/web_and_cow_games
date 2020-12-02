#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'CRYPTO_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()
    
    # Data du jeu
    print(data)

    reponse = ''

    # ------- CODE ICI -----------
    
    for i in range(len(data['mots'][0])):
        temp = [elt[i] for elt in data['mots']]
        reponse += sorted(temp, key=temp.count)[-1]

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()