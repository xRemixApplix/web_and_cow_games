#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'SAC_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = ""

    # ------- CODE ICI -----------
    
    tab_object = list()
    poids_actuel = 0

    for key, poids in data['objets'].items():
        tab_object.append(poids)

    plus_lourd = sorted(tab_object, reverse=True)[:10]
    plus_leger = sorted(tab_object)[:10]

    for poid in plus_lourd:
        if poids_actuel+int(poid)<=int(data["sac"]):
            poids_actuel += int(poid)
        else:
            break

    for poid in plus_leger:
        if poids_actuel+int(poid)<=int(data["sac"]):
            poids_actuel += int(poid)
        else:
            break

    reponse = poids_actuel

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()