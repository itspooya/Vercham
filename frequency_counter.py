from collections import OrderedDict
from operator import itemgetter 

class Valueboolean(Exception):
    "Value must be 0 or 1"
    pass

def word_counter(string,besorted):
    """This is a word frequency counter implemented in python3 with OrderedDict and itemgetter that return sorted
    and unsorted dictionaries, two values can be passed to this function a string and integer either (0 or 1)
     or (True or False)"""
    # Initialize a new Dictionary
    try:
        if int(besorted)==1 or int(besorted)==0:
            bool(besorted)
        else:
            raise Valueboolean
    except Valueboolean:
        print("Value should be 0 or 1")
        print()
        return
    counts = dict()
    # Split is a method that by default split words separated by whitespace
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # It is good to sort items by occurrence for better visuals
    # For sorting we can use .get or itemgetter, from timing it for large dicionaries itemgetter is
    # more efficient
    if besorted == False:
        return counts
    elif besorted == True:
        return OrderedDict(sorted(counts.items(),key=itemgetter(1),reverse=True))