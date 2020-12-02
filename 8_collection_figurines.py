#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'COLLECTION_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = ''

    # ------- CODE ICI -----------
    
    achat = vente = 0
    for exemplaire, cote in zip(data['exemplaires'], data['cotes']):
        prix_achat = 30 if exemplaire<2000 else 15
        achat += prix_achat
        vente += prix_achat*cote

    reponse = int(vente-achat)

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()