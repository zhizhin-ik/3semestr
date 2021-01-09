# coding: utf-8
# license: GPLv3
from hero import *
from artifacts import *
from random import randint, choice

def generate_artifacts():
    enemy_list = [artifact_types[i] for i in range(len(artifact_types))]
    return enemy_list
spisok=generate_artifacts()

class Shop():
    _assortment = []
    _color= None
    _artifacts= spisok
    _place='мирное'


    def generate(self, ot, do):
        mass=[]
        for i in range(randint(ot,do)):
            mass.append(self._artifacts[randint(0,4)])
        self._assortment=mass


    def balance(self):
        print(hero._money)

    def buy(self,hero,name):
        for i in range(len(self._assortment)):
            if self._assortment[i] == name:
                if hero._money > name._cost:
                    name._amount +=1
                    print('Вы купили {}'.format(name._name))
                    return
        print('{} нет в наличии'.format(name._name))
    def assortment(self):
        print('Ассортимент:',end='')
        for i in range(len(self._assortment)):
            print(self._assortment[i]._name, end=', ')
        print()



class Small_shop(Shop):
    def __init__(self):
        self.generate(1, 1)
    def info(self):
        print('В этом магазине вы можете продать свои вещи и купить 1 артефакт')


class Average_shop(Shop):
    def __init__(self):
        self.generate(1, 3)
    def info(self):
        print('В этом магазине вы можете продать свои вещи и купить от 1 до 3 артефактов')


class Big_shop(Shop):
    def __init__(self):
        self.generate(3, 5)
    def info(self):
        print('В этом магазине вы можете продать свои вещи и купить от 3 до 5 артефактов')




#     print('Вы посетили магазин. На вашем счету {} денег'.format(hero._money))
#     print('Ваш инвентарь:')
#     artifacts= generate_artifacts()
#     for artifact in artifacts:
#         print(artifact._name, artifact._amount)
#     while True:
#         print('Если хотите что-то продать, то введите 1, если хотите перейти к покупкам, нажмите 0')
#         number = check_number_1()
#         if number==0:
#             break
#         else:
#             print('Выберите номер артефакта, который хотите продать')
#             number = check_number_2()
#             if artifacts[number - 1]._amount !=0:
#                 hero._money+=artifacts[number-1]._cost
#                 artifacts[number - 1]._amount -= 1
#                 print('Вы продали {}. Теперь на вашем счету {} денег'.format(artifacts[number - 1]._name,hero._money))
#             else:
#                 print('Вы не можете продать этот предмет, так как у вас его нет')
#
#     print('Вы можете купить:')
#     for nomer, artifact in enumerate(artifacts):
#         print('{}.{} за {}'.format(nomer + 1, artifact._name, artifact._cost))
#     while True:
#         print('Выберите номер артефакта, который хотите приобрести или 0, если хотите покинуть магазин.')
#         number=check_number_3()
#         if number==0:
#             print('Выхожу из магазина')
#             break
#         else:
#             if hero._money>=artifacts[number-1]._cost:
#                 artifacts[number - 1]._amount+=1
#                 hero._money-=artifacts[number-1]._cost
#                 print('Вы купили {}'.format(artifacts[number-1]._name))
#             else:
#                 print('У вас не хватает денег на этот артефакт')
#
# def check_number_1():
#     number = None
#     correct_numbers = [0, 1]
#     while number == None:
#         try:
#             number = int(input())
#             for i in correct_numbers:
#                 if i==number:
#                     return number
#             print('Артефакта с таким номером нет')
#             number = None
#         except ValueError:
#             print('Вы ввели недопустимые символы')
#
#
#
# def check_number_2():
#     number = None
#     correct_numbers = [1, 2, 3, 4, 5]
#     while number == None:
#         try:
#             number = int(input())
#             for i in correct_numbers:
#                 if i == number:
#                     return number
#             print('Артефакта с таким номером нет')
#             number = None
#         except ValueError:
#             print('Вы ввели недопустимые символы')
#     return number
#
#
#
# def check_number_3():
#     number = None
#     correct_numbers = [0, 1, 2, 3, 4, 5]
#     while number == None:
#         try:
#             number = int(input())
#             for i in correct_numbers:
#                 if i == number:
#                     return number
#             print('Артефакта с таким номером нет')
#             number = None
#         except ValueError:
#             print('Вы ввели недопустимые символы')
#     return number
#
#
#
