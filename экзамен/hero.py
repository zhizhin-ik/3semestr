# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    _name=None
    _experience=None
    _money=None
    def __init__(self, name):
        self._health = 100
        self._attack = 5000
        self._name=name
        self._experience=0
        self._money=100
    def experience(self):
        self._experience+=10
    def money(self):
        self._money+=10
    def attack(self, target):
        target._health -= self._attack


    def apple_buy(self):
        self._artifacts.append('apple')
    def apple_delete(self):
        self._artifacts.delete('apple')
    def apple_use(self):
        self._health += self.finish_health

