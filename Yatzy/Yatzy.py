<<<<<<< HEAD
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
=======
class Yatzy:

    def __init__(self,*dados):
        self.dados = list(dados)

    def chance(*dados):
        chance = 0
        for lado in dados:
            chance += lado
        return chance

    def Yatzy(*dados):
        if len(list(dados)) == list(dados).count(1):
            return 50
        return 0

    def Ones(*dados):
        Ones = 0
        for lado in list(dados):
            if lado == 1:
                Ones += lado
        return Ones
    
    def Twos(*dados):
        Twos = 0
        for lado in list(dados):
            if lado == 2:
                Twos += lado
        return Twos

    def Threes(*dados):
        Threes = 0
        for lado in list(dados):
            if lado == 3:
                Threes += lado
        return Threes

    def Fours(*dados):
        Fours = 0
        for lado in list(dados):
            if lado == 4:
                Fours += lado
        return Fours

    def Fives(*dados):
        Fives = 0
        for lado in list(dados):
            if lado == 5:
                Fives += lado
        return Fives

    def Sixes(*dados):
        Sixes = 0
        for lado in list(dados):
            if lado == 6:
                Sixes += lado
        return Sixes
    
    def Pair(*dados):
        contador = 6
        while contador > 0:
            if list(dados).count(contador)>=2:
                return contador * 2
            contador -= 1
        return 0
    
    def Two_pairs(*dados):
        Two_pairs = 0
        First_pair_sano = False
        contador = 6
        while contador > 0:
            if list(dados).count(contador)>=2 and First_pair_sano == False :
                First_pair_sano = True
                Two_pairs = contador * 2
            elif list(dados).count(contador)>=2 and First_pair_sano == True :
                Two_pairs += contador * 2
                return Two_pairs
            contador -= 1
        return 0

    def Three_of_a_kind(*dados):
        for number in list(dados):
            if list(dados).count(number)>=3:
                return number * 3
        return 0

    def Four_of_a_kind(*dados):
        for number in list(dados):
            if list(dados).count(number)>=4:
                return number * 4
        return 0

    def Small_straight(*dados):
        dados = list(dados)
        if dados.count(1) >= 1 and dados.count(2) >= 1 and dados.count(3) >= 1 and dados.count(4) >= 1 and dados.count(5) >= 1:
            return 15
        return 0

    def Large_straight(*dados):
        dados = list(dados)
        if dados.count(6) >= 1 and dados.count(2) >= 1 and dados.count(3) >= 1 and dados.count(4) >= 1 and dados.count(5) >= 1:
            return 20
        return 0

    def Full_house(*dados):
        contador = 1
        three_sano = False
        pair_sano = False
        full = 0
        while contador < 7:
            if list(dados).count(contador) == 2 and not pair_sano:
                full += contador * 2
                pair_sano = True
            elif list(dados).count(contador) == 3 and not three_sano:
                full += contador * 3
                three_sano = True
            elif three_sano and pair_sano:
                return full
            contador += 1
>>>>>>> developing
        return 0
    
if __name__ == '__main__':

    #Chance

    assert Yatzy.chance(1,2,3,4,5) == 15

    assert Yatzy.chance(1,1,1,1,1) == 5

    assert Yatzy.chance(2,2,2,2,2) == 10

    assert Yatzy.chance(2,2,3,3,3) == 13

    #Yatzy

<<<<<<< HEAD
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
=======
    assert Yatzy.Yatzy(1,2,3,4,5) == 0

    assert Yatzy.Yatzy(1,1,1,1,1) == 50

    assert Yatzy.Yatzy(2,2,2,2,2) == 0

    assert Yatzy.Yatzy(1,1,1,1,2) == 0

    #Ones

    assert Yatzy.Ones(1,2,2,2,2) == 1

    assert Yatzy.Ones(2,2,2,2,2) == 0

    assert Yatzy.Ones(1,1,2,2,2) == 2

    assert Yatzy.Ones(1,1,1,2,2) == 3

    assert Yatzy.Ones(1,1,1,1,2) == 4

    assert Yatzy.Ones(1,1,1,1,1) == 5

    assert Yatzy.Ones(1,1,1,1,1,1,1,1,1) == 9

    #Twos 

    assert Yatzy.Twos(2,1,1,1,1) == 2

    assert Yatzy.Twos(2,2,1,1,1) == 4

    assert Yatzy.Twos(2,2,2,1,1) == 6

    assert Yatzy.Twos(2,2,2,2,1) == 8

    assert Yatzy.Twos(2,2,2,2,2) == 10

    assert Yatzy.Twos(1,1,1,1,1) == 0

    assert Yatzy.Twos(2,2,2,2,2,2,2,2,2) == 18

    #Threes

    assert Yatzy.Threes(3,1,1,1,1) == 3

    assert Yatzy.Threes(3,3,1,1,1) == 6

    assert Yatzy.Threes(1,1,1,1,1) == 0

    #Fours

    assert Yatzy.Fours(4,4,4,1,1) == 12

    assert Yatzy.Fours(4,4,4,4,4) == 20

    assert Yatzy.Fours(1,1,1,1,1) == 0

    #Pair

    assert Yatzy.Pair(2,2,1,1,1) == 4

    assert Yatzy.Pair(2,2,2,2,2) == 4 

    assert Yatzy.Pair(2,2,2,6,6) == 12 

    assert Yatzy.Pair(1,2,3,4,5) == 0

    #Two_pairs

    assert 8 == Yatzy.Two_pairs(1, 1, 2, 3, 3)

    assert 0 == Yatzy.Two_pairs(1, 1, 2, 3, 4)
    
    assert 6 == Yatzy.Two_pairs(1, 1, 2, 2, 2)
    
    assert 0 == Yatzy.Two_pairs(1, 2, 3, 4, 5)

    #Three_of_a_kind

    assert 9 == Yatzy.Three_of_a_kind(3, 3, 3, 4, 5)
    
    assert 0 == Yatzy.Three_of_a_kind(3, 3, 4, 5, 6)
    
    assert 9 == Yatzy.Three_of_a_kind(3, 3, 3, 3, 1)
    
    assert 12 == Yatzy.Three_of_a_kind(1, 4, 4, 4, 5)

    #Four_of_a_kind

    assert 20 == Yatzy.Four_of_a_kind(2, 5, 5, 5, 5)
    
    assert 0 == Yatzy.Four_of_a_kind(2, 2, 2, 5, 5)
    
    assert 8 == Yatzy.Four_of_a_kind(2, 2, 2, 2, 2)
    
    assert 4 == Yatzy.Four_of_a_kind(1, 1, 1, 1, 5)

    #Small_straight

    assert 15 == Yatzy.Small_straight(1, 2, 3, 4, 5)
    
    assert 0 == Yatzy.Small_straight(2, 3, 4, 5, 6)
    
    assert 0 == Yatzy.Small_straight(1, 3, 4, 5, 5)
    
    assert 0 == Yatzy.Small_straight(6, 6, 6, 6, 6)
    
    assert 0 == Yatzy.Small_straight(1, 2, 3, 4, 6)

    #Large_straight

    assert 20 == Yatzy.Large_straight(2, 3, 4, 5, 6)
    
    assert 0 == Yatzy.Large_straight(1, 2, 3, 4, 5)
    
    assert 0 == Yatzy.Large_straight(1, 3, 4, 5, 5)
    
    assert 0 == Yatzy.Large_straight(6, 6, 6, 6, 6)
    
    assert 0 == Yatzy.Large_straight(1, 2, 3, 4, 6)

    #Full_house

    assert 8 == Yatzy.Full_house(1, 1, 2, 2, 2)
    
    assert 0 == Yatzy.Full_house(2, 2, 3, 3, 4)
    
    assert 0 == Yatzy.Full_house(4, 4, 4, 4, 4)
>>>>>>> developing
