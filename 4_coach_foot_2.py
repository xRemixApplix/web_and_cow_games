#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'FOOTBALL_2'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)
    postes = "GDMA"
    nb_poste = dict()
    nb_poste['G'] = 1
    nb_poste['D'], nb_poste['M'], nb_poste['A'] = [elt for elt in data['dispositif'].split('-')]
    tab_reponse = list()

    # ------- CODE ICI -----------
    
    for poste in postes:
        dict_reponse = dict()
        tab_temp = list()
        for i in range(len(data['forces'])):
            if data['postes'][i] == poste: tab_temp.append(int(data['forces'][i]))
            else: tab_temp.append(0)

        i = 0
        for joueur in tab_temp:
            dict_reponse[i] = joueur
            i += 1

        dict_sorted = sorted(dict_reponse.items(), key=lambda t: t[1], reverse=True)
        tab_reponse += [elt for elt in dict_sorted[:int(nb_poste[poste])]]

    reponse_sorted = sorted(tab_reponse, key=lambda t: t[1], reverse=True)

    # ----------------------------

    reponse = '-'.join([str(elt[0]) for elt in reponse_sorted])
    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()