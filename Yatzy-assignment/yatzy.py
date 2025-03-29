class Yatzy:
    @staticmethod
    def chance(dice):
        return sum(dice)
    
    @staticmethod
    def yatzy(dice):
        return 50 if len(set(dice)) == 1 else 0
    
    @staticmethod
    def ones(dice):
        return dice.count(1) * 1

    @staticmethod
    def twos(dice):
        return dice.count(2) * 2

    @staticmethod
    def threes(dice):
        return dice.count(3) * 3

    @staticmethod
    def fours(dice):
        return dice.count(4) * 4

    @staticmethod
    def fives(dice):
        return dice.count(5) * 5

    @staticmethod
    def sixes(dice):
        return dice.count(6) * 6
    
    @staticmethod
    def pair(dice):
        pairs = [die for die in set(dice) if dice.count(die) >= 2]
        return max(pairs) * 2 if pairs else 0
    
    @staticmethod
    def two_pairs(dice):
        pairs = [die for die in set(dice) if dice.count(die) >= 2]
        if len(pairs) >= 2:
            return sum(sorted(pairs, reverse=True)[:2]) * 2
        return 0

    @staticmethod
    def three_of_a_kind(dice):
        for die in set(dice):
            if dice.count(die) >= 3:
                return die * 3
        return 0
    
    @staticmethod
    def four_of_a_kind(dice):
        for die in set(dice):
            if dice.count(die) >= 4:
                return die * 4
        return 0

    @staticmethod
    def small_straight(dice):
        if set([1, 2, 3, 4, 5]).issubset(dice):
            return 15
        return 0
    
    @staticmethod
    def large_straight(dice):
        if set([2, 3, 4, 5, 6]).issubset(dice):
            return 20
        return 0

    @staticmethod
    def full_house(dice):
        count = {x: dice.count(x) for x in set(dice)}
        if sorted(count.values()) == [2, 3]:
            return sum(dice)
        return 0