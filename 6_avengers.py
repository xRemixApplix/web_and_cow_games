#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'AVENGERS_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = ''

    # ------- CODE ICI -----------
    
    tab_force = list()
    for key, value in data.items():
        tab_force.append(int(value))

    def puissance(tab):
        return (tab[0]*3+10)+(tab[1]*4+5)+(tab[2]*3+7)+(tab[3]*4+20)

    nb_turn = 0
    while puissance(tab_force)<=tab_force[4]:
        tab_force[nb_turn%4] += 1
        nb_turn += 1

    reponse = nb_turn+1
    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()