#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'DBZ_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = 0

    # ------- CODE ICI -----------
    
    def recup_strenght(adv_force):
        return int((adv_force*10)//100)

    niveau = int(data['niveau'])
    puissance = int(data['vegeta'])

    for ennemi in data['ennemis']:
        while (puissance*niveau)<int(ennemi):
            niveau += 1

        puissance += recup_strenght(ennemi)

    reponse = str(puissance) + " " + str(niveau)

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()