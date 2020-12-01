#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'WALL_E'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------
    force = int(data['force'])
    speed = int(data['vitesse'])
    battery = int(data['batterie'])

    for trash in data['dechets']:
        if battery<20:
            if battery>speed:
                battery = 100 - speed
                print("Recharge : {}".format(battery))
            else:
                battery = "KO"
                print("KO")
                break

        print("Dechet : {} =======> ".format(trash), end='')
        if trash<=force:
            battery -= 1
            print('Easy : -1% -> {}'.format(battery))
        else:
            batt_need = (trash-force)*2
            if batt_need>battery/2:
                battery -= 2
                print("Pas assez de batterie pour force : -2% -> {}".format(battery))
            else:
                battery -= batt_need
                print("Augmentation : -{}% -> {}".format(batt_need, battery))

    reponse = battery

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()