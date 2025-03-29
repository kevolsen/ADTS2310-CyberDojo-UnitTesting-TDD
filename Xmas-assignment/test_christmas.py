from christmas import verse_header, whole_verse

def test_first_two_lines_of_first_verse():
    header = verse_header(1)
    assert header == """\
On the first day of Christmas
My true love gave to me:"""
    
def test_first_two_lines_of_first_verse():
    header = verse_header(2)
    assert header == """\
On the second day of Christmas
My true love gave to me:"""
    
def test_whole_first_verse():
    lyrics = verse_header(1) + "\n" + whole_verse(1)
    assert lyrics == """\
On the first day of Christmas
My true love gave to me:
A partridge in a pear tree."""
    
def test_whole_second_verse():
    lyrics = verse_header(2) + "\n" + whole_verse(2)
    assert lyrics == """\
On the second day of Christmas
My true love gave to me:
Two turtle doves and
A partridge in a pear tree."""
    
def test_whole_twelfth_verse():
    lyrics = verse_header(12) + "\n" + whole_verse(12)
    assert lyrics == """\
On the twelfth day of Christmas
My true love gave to me:
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree."""