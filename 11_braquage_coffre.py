#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'CRYPTO_2'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = int(data['depart'])

    # ------- CODE ICI -----------
    
    for operation in data['chemin']:
        if '+' in operation:
            reponse += 10**(len(operation)-1)
        else:
            reponse -= 10**(len(operation)-1)


    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()