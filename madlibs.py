#1.mad libs generator

import random

def mad_libs_game():
    adjectives = ['happy', 'sad', 'tall', 'short', 'loud', 'quiet']

    verbs = ['jumped', 'ran', 'swam', 'flew', 'crawled', 'danced']

    nouns = ['apple', 'banana', 'tree', 'car', 'bus', 'bike']

    adverbs = ['quickly', 'slowly', 'easily', 'carefully', 'loudly', 'quietly']

    adj=random.choice(adjectives)

    verb=random.choice(verbs)

    noun=random.choice(nouns)

    adve=random.choice(adverbs)

    story="The "+adj+ " boy "+verb+" "+adve+" when he saw a "+noun
    print(story)
mad_libs_game()