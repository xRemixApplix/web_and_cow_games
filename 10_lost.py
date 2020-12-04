#!/bin/python
from Game import Game

# Key personnelle
player_key = '800ada5c7d918287f83fe627398fc7f1'
# Code du challenge
engine_code = 'LOST_1'


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    reponse = ''

    # ------- CODE ICI -----------
    
    tab_codes = list()
    tab_number = list()

    for code in data['codes']:
        code_with_no_spaces = code.replace(" ","")
        tab_codes.append(code_with_no_spaces)

    for code in tab_codes:
        i = 0
        number = 1
        while i<len(code):
            if i+1<len(code):
                if code[i+1] in "+-":
                    if code[i+1]=='+':
                        number *= (data['nombres'][int(code[i])-1]+data['nombres'][int(code[i+2])-1])
                    else:
                        number *= (data['nombres'][int(code[i])-1]-data['nombres'][int(code[i+2])-1])
                    i += 2
                else:
                    number *= data['nombres'][int(code[i])-1]
            else:
                number *= data['nombres'][int(code[i])-1]
            i += 1
        print(number)
        tab_number.append(number)

    reponse = sum(tab_number)

    # ----------------------------

    print(reponse)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()