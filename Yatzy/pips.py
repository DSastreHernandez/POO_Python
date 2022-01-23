from enum import Enum


class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4 
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]
    
    @classmethod
    def reversed_values(cls):
        return reversed(cls.values())

if __name__ == '__main__':

    assert [1,2,3,4,5,6] == Pips.values()

    assert [6,5,4,3,2,1] == Pips.reversed_values()