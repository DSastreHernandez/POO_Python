from pips import Pips

class Yatzy:

    @staticmethod
    def chance(*dices):
        score = sum(dices)
        return score

    @staticmethod
    def yatzy(*dices):
        score = 0
        YATZY = 5
        for number in dices:
            if dices.count(number) >= YATZY:
                score = 50
                return score
        return score

    @staticmethod
    def ones(*dices):
        ONE = Pips.ONE.value
        score = dices.count(ONE) * ONE
        return score
    
    @staticmethod
    def twos(*dices):
        TWO = Pips.TWO.value
        score = dices.count(TWO) * TWO
        return score

    @staticmethod
    def threes(*dices):
        THREE = Pips.THREE.value
        score = dices.count(THREE) * THREE
        return score

    @staticmethod
    def fours(*dices):
        FOUR = Pips.FOUR.value
        score = dices.count(FOUR) * FOUR
        return score

    @staticmethod
    def fives(*dices):
        FIVE = Pips.FIVE.value
        score = dices.count(FIVE) * FIVE
        return score

    @staticmethod
    def sixes(*dices):
        SIX = Pips.SIX.value
        score = dices.count(SIX) * SIX
        return score
    
    @classmethod
    def __search_repeated_dices(cls,dices,number_of_repeats):
        PAIR = 2
        pairs = list(filter(lambda pip: dices.count(pip) >= PAIR, Pips.reversed_values()))
        return sum(pairs[:number_of_repeats]) * PAIR if len(pairs) >= number_of_repeats else 0

    @classmethod
    def pair(cls,*dices):
        number_of_repeats = 1
        return cls.__search_repeated_dices(dices, number_of_repeats)        
    
    @classmethod
    def two_pairs(cls,*dices):
        number_of_repeats = 2
        return cls.__search_repeated_dices(dices, number_of_repeats)
        
    @classmethod
    def __quantity_of_a_kind(cls, dices, quantity):
        for pip in Pips.reversed_values():
            if dices.count(pip) >= quantity:
                return pip * quantity
        return 0

    @classmethod
    def three_of_a_kind(cls,*dices):
        quantity = 3
        return cls.__quantity_of_a_kind(dices,quantity)

    @classmethod
    def four_of_a_kind(cls, *dices):
        quantity = 4
        return cls.__quantity_of_a_kind(dices,quantity)

    @classmethod
    def small_straight(cls,*dices):
        ONE = Pips.ONE.value
        FIVE = Pips.FIVE.value
        return cls.chance(*dices) if list(range(ONE, FIVE + 1)) == sorted(dices) else 0

    @classmethod
    def large_straight(cls, *dices):
        TWO = Pips.TWO.value
        SIX = Pips.SIX.value
        return cls.chance(*dices) if list(range(TWO, SIX + 1)) == sorted(dices) else 0

    @classmethod
    def full_house(cls, *dices):
        if cls.two_of_a_kind(*dices) and cls.three_of_a_kind(*dices):
            return cls.chance(*dices)
        else:
            return 0
    
    @staticmethod
    def two_of_a_kind(*dices):
        PAIR = 2
        for dice in dices:
            if dices.count(dice) == PAIR:
                return dice * PAIR
        return 0
    
if __name__ == '__main__':

    #Chance

    assert Yatzy.chance(1,2,3,4,5) == 15

    assert Yatzy.chance(1,1,1,1,1) == 5

    assert Yatzy.chance(2,2,2,2,2) == 10

    assert Yatzy.chance(2,2,3,3,3) == 13

    #Yatzy

    assert Yatzy.yatzy(1,2,3,4,5) == 0

    assert Yatzy.yatzy(1,1,1,1,1) == 50

    assert Yatzy.yatzy(2,2,2,2,2) == 50

    assert Yatzy.yatzy(1,1,1,1,2) == 0

    #Ones

    assert Yatzy.ones(1,2,2,2,2) == 1

    assert Yatzy.ones(2,2,2,2,2) == 0

    assert Yatzy.ones(1,1,2,2,2) == 2

    assert Yatzy.ones(1,1,1,2,2) == 3

    assert Yatzy.ones(1,1,1,1,2) == 4

    assert Yatzy.ones(1,1,1,1,1) == 5

    assert Yatzy.ones(1,1,1,1,1,1,1,1,1) == 9

    #Twos 

    assert Yatzy.twos(2,1,1,1,1) == 2

    assert Yatzy.twos(2,2,1,1,1) == 4

    assert Yatzy.twos(2,2,2,1,1) == 6

    assert Yatzy.twos(2,2,2,2,1) == 8

    assert Yatzy.twos(2,2,2,2,2) == 10

    assert Yatzy.twos(1,1,1,1,1) == 0

    assert Yatzy.twos(2,2,2,2,2,2,2,2,2) == 18

    #Threes

    assert Yatzy.threes(3,1,1,1,1) == 3

    assert Yatzy.threes(3,3,1,1,1) == 6

    assert Yatzy.threes(1,1,1,1,1) == 0

    #Fours

    assert Yatzy.fours(4,4,4,1,1) == 12

    assert Yatzy.fours(4,4,4,4,4) == 20

    assert Yatzy.fours(1,1,1,1,1) == 0

    #Pair

    assert Yatzy.pair(2,2,1,1,1) == 4

    assert Yatzy.pair(2,2,2,2,2) == 4 

    assert Yatzy.pair(2,2,2,6,6) == 12 

    assert Yatzy.pair(1,2,3,4,5) == 0

    #Two_pairs

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)

    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)

    #Three_of_a_kind

    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    
    assert 12 == Yatzy.three_of_a_kind(1, 4, 4, 4, 5)

    #Four_of_a_kind

    assert 20 == Yatzy.four_of_a_kind(2, 5, 5, 5, 5)
    
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    
    assert 4 == Yatzy.four_of_a_kind(1, 1, 1, 1, 5)

    #Small_straight

    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)

    #Large_straight

    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)
    
    assert 0 == Yatzy.large_straight(1, 3, 4, 5, 5)
    
    assert 0 == Yatzy.large_straight(6, 6, 6, 6, 6)
    
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 6)

    #Full_house

    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    
    assert 0 == Yatzy.full_house(2, 2, 3, 3, 4)
    
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)