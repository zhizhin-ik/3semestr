# coding: utf-8
# license: GPLv3


class Artifacts():
    def __init__(self):
        self._cost = None
        self._name= None
        self._amount= None


class Apple(Artifacts):
    _amount=0
    _name='apple'
    _cost=50

class Marker(Artifacts):
    _amount = 0
    _name = 'marker'
    _cost=60


class Shield(Artifacts):
    _amount = 0
    _name = 'shield'
    _cost =70


class Rebirth(Artifacts):
    _amount = 0
    _name = 'rebirth'
    _cost =80


class Wings(Artifacts):
    _amount = 0
    _name = 'wings'
    _cost =90


artifact_types=[Apple, Marker, Shield, Rebirth, Wings]