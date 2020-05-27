from ordered_enum import OrderedEnum
import jsons
import json


class Manner(OrderedEnum):
    close = 1
    near_close = 2
    close_mid = 3
    mid = 4
    open_mid = 5
    near_open = 6
    open = 7

class Place(OrderedEnum):
    front = 1
    central = 2
    back = 3

class Roundedness(OrderedEnum):
    unrounded = 1
    rounded = 2

class Length(OrderedEnum):
    short = 1
    long = 2


class Phonem:
    def __init__(self, manner: Manner, place: Place, symbol=None, prevalence=0):
        self.manner = manner
        self.place = place
        self.symbol = symbol
        self.prevalence = prevalence

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return jsons.dumps(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        i = 0
        selfProperties = list(self.__dict__.values())
        otherProperties = list(other.__dict__.values())
        while i < len(selfProperties) and selfProperties[i] == otherProperties[i]:
            i += 1
        return selfProperties[i] < otherProperties[i]



class Vowel(Phonem):
    def __init__(self, manner: Manner, place: Place, roundedness: Roundedness, length: Length, symbol=None, prevalence=0):
        super().__init__(manner, place, symbol, prevalence)
        self.roundedness = roundedness
        self.length = length

    def getTitle(self):
        titleDict = {
            'place': self.place._name_,
            'roundedness': self.roundedness._name_,
            'length': self.length._name_
        }
        return json.dumps(titleDict)

    # def __repr__(self):
    #     return str({
    #         'manner': str(self.manner),
    #         'place': str(self.place),
    #         'roundedness': str(self.roundedness),
    #         'length': str(self.length),
    #         'symbol': self.symbol,
    #         'prevalence': self.prevalence
    #     })

