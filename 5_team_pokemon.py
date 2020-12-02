#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'POKEMON_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = ''

    base = ['Eau', 'Feu', 'Herbe']
    rare = ['Air', 'Poison', 'Glace', 'Psychique', 'Insecte']

    # ------- CODE ICI -----------
    
    max_base = len(data['types'])

    for type in base:
        if max_base > data['types'].count(type):
            max_base = data['types'].count(type)

    nb_rare = 0
    for type in data['types']:
        if type in rare: nb_rare += 1

    if nb_rare>max_base:
        reponse = max_base
    else:
        reponse = nb_rare

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()