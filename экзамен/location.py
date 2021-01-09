# coding: utf-8
# license: GPLv3
from enemies import *
from random import randint, choice
from shop import *

class Location:
    _location = []

    def generate_random_enemy(self):
        RandomEnemyType = choice(enemy_types)
        enemy = RandomEnemyType()
        return enemy


    def generate_dragon_list(self,enemy_number):
        enemy_list= [self.generate_random_enemy() for i in range(enemy_number)]
        self._location=enemy_list
        return enemy_list
enemy_types = [small_shop]
#enemy_types = [GreenDragon, RedDragon, BlackDragon, small_shop, average_shop, big_shop]