from yatzy import Yatzy

def test_chance():
    assert Yatzy.chance([1, 1, 3, 3, 6]) == 14
    assert Yatzy.chance([4, 5, 5, 6, 1]) == 21
    
def test_yatzy():
    assert Yatzy.yatzy([1, 1, 1, 1, 1]) == 50
    assert Yatzy.yatzy([5, 5, 5, 5, 5]) == 50
    assert Yatzy.yatzy([1, 5, 5, 3, 5]) == 0
    
def test_ones():
    assert Yatzy.ones([1, 1, 2, 4, 4]) == 2
    assert Yatzy.ones([3, 3, 3, 4, 5]) == 0
    
def test_twos():
    assert Yatzy.twos([1, 1, 2, 4, 4]) == 2
    assert Yatzy.twos([3, 3, 3, 4, 5]) == 0

def test_threes():
    assert Yatzy.threes([1, 1, 2, 4, 4]) == 0
    assert Yatzy.threes([3, 3, 3, 4, 5]) == 9

def test_fours():
    assert Yatzy.fours([1, 1, 2, 4, 4]) == 8
    assert Yatzy.fours([3, 3, 3, 2, 5]) == 0

def test_fives():
    assert Yatzy.fives([1, 1, 2, 4, 4]) == 0
    assert Yatzy.fives([3, 3, 3, 5, 5]) == 10

def test_sixes():
    assert Yatzy.sixes([1, 1, 2, 4, 4]) == 0
    assert Yatzy.sixes([3, 3, 6, 6, 6]) == 18
    
def test_pair():
    assert Yatzy.pair([3, 3, 3, 4, 4]) == 8
    assert Yatzy.pair([1, 1, 6, 2, 6]) == 12
    assert Yatzy.pair([3, 5, 2, 4, 1]) == 0
    
def test_two_pairs():
    assert Yatzy.two_pairs([1, 1, 2, 3, 3]) == 8
    assert Yatzy.two_pairs([1, 1, 2, 3, 4]) == 0
    assert Yatzy.two_pairs([1, 1, 2, 2, 2]) == 6

def test_three_of_a_kind():
    assert Yatzy.three_of_a_kind([3, 3, 2, 4, 5]) == 0
    assert Yatzy.three_of_a_kind([3, 3, 4, 5, 6]) == 0
    assert Yatzy.three_of_a_kind([3, 3, 3, 3, 1]) == 9
    
def test_four_of_a_kind():
    assert Yatzy.four_of_a_kind([2, 2, 2, 2, 5]) == 8
    assert Yatzy.four_of_a_kind([2, 2, 2, 5, 5]) == 0
    assert Yatzy.four_of_a_kind([5, 5, 5, 5, 5]) == 20

def test_small_straight():
    assert Yatzy.small_straight([1, 2, 3, 4, 5]) == 15
    assert Yatzy.small_straight([2, 3, 4, 5, 6]) == 0
    
def test_large_straight():
    assert Yatzy.large_straight([2, 3, 4, 5, 6]) == 20
    assert Yatzy.large_straight([1, 2, 3, 4, 5]) == 0

def test_full_house():
    assert Yatzy.full_house([1, 1, 2, 2, 2]) == 8
    assert Yatzy.full_house([2, 2, 3, 3, 4]) == 0
    assert Yatzy.full_house([4, 4, 4, 4, 4]) == 0