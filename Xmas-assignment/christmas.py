def verse_header(number):
    verse_names = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
                   "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    return f"On the {verse_names[number - 1]} day of Christmas\nMy true love gave to me:"

def whole_verse(number):
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves and",
        "Three french hens",
        "Four calling birds",
        "Five golden rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
    ]
    
    verse_lines = gifts[:number][::-1]  # Reverse to start from the highest gift
    return "\n".join(verse_lines)

# print(verse_header(12) + "\n" + whole_verse(12))