# coding: utf-8
# license: GPLv3
from enemies import *
from random import choice
from shop import *

class Location:
    _place = None
    _location = []

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_location_list(number_of_locations):
    enemy_list= [generate_random_enemy() for i in range(number_of_locations)]
    return enemy_list
#enemy_types = [Small_shop, Average_shop, Big_shop]
enemy_types = [GreenDragon, RedDragon, BlackDragon, Small_shop, Average_shop, Big_shop]