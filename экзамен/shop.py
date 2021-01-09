# coding: utf-8
# license: GPLv3
from hero import *
from artifacts import *

def shop(hero):
    money = hero._money
    print('Вы посетили магазин. На вашем счету {} денег'.format(money))
    print('Ваш инвентарь:')
    artifacts= generate_artifacts()
    for artifact in artifacts:
        print(artifact._name, artifact._amount)
    while True:
        print('Если хотите что-то продать, то введите 1, если хотите перейти к покупкам, нажмите 0')
        number = check_number_1()
        if number==0:
            break
        else:
            print('Выберите номер артефакта, который хотите продать')
            number = check_number_2(hero)


    while True:
        print('Вы можете купить:')
        for nomer, artifact in enumerate(artifacts):
            print('{}.{} за {}'.format(nomer+1,artifact._name, artifact._cost))
        print('Выберите номер артефакта, который хотите приобрести или 0, если хотите покинуть магазин.')
        number=check_number_3()
        if number==0:
            print('Выхожу из магазина')
            break
        else:
            if hero._money>=artifacts[number-1]._cost:
                artifacts[number - 1]._amount+=1
                hero._money-=artifacts[number-1]._cost
                print('Вы купили {}'.format(artifacts[number-1]._name))
            else:
                print('У вас не хватает денег на этот артефакт')

def check_number_1():
    number = None
    correct_numbers = [0, 1]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i==number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')



def check_number_3():
    number = None
    correct_numbers = [1, 2, 3, 4, 5]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i == number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')
    return number



def check_number_3():
    number = None
    correct_numbers = [0, 1, 2, 3, 4, 5]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i == number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')
    return number
