# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from shop import *
from location import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer

def game_tournament(hero, dragon_list):
    for mesto in dragon_list._location:
        if mesto._color:
            dragon = mesto
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')
            hero.experience()
            hero.money()
            print('Ваш накопленный опыт:', hero._experience)
            print('Ваши накопленные деньги:', hero._money)
        else:
            shop=mesto
            shop.info()
            shop.assortment()
            shop.buy(hero,apple)


    if hero.is_alive():
        print('Поздравляем! Вы победили!')

    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = Location()
        dragon_list.generate_dragon_list(dragon_number)
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
