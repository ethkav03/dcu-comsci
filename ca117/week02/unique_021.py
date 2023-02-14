#!/usr/bin/env python3

import string
import sys

def remove_punctuation(s):
    for char in s:
        if char in string.punctuation:
            s = s.replace(char, "")
    return s

def word_count(s):
    a = s.split()
    for word in a:
        if word in unique_words:
            d[word] = 1


unique_words = ['1863', '19', 'a', 'above', 'abraham', 'add', 'advanced', 'ago', 'all', 'altogether', 'and', 'any', 'are', 'as', 'battle-field', 'be', 'before', 'birth', 'brave', 'brought', 'but', 'by', 'can', 'cause', 'civil', 'come', 'conceived', 'consecrate', 'consecrated', 'continent', 'created', 'dead', 'dedicate', 'dedicated', 'detract', 'devotion', 'did', 'died', 'do', 'earth', 'endure', 'engaged', 'equal', 'far', 'fathers', 'field', 'final', 'fitting', 'for', 'forget', 'forth', 'fought', 'four', 'freedom', 'from', 'full', 'gave', 'god', 'government', 'great', 'ground', 'hallow', 'have', 'here', 'highly', 'honored', 'in', 'increased', 'is', 'it', 'larger', 'last', 'liberty', 'lincoln', 'little', 'live', 'lives', 'living', 'long', 'measure', 'men', 'met', 'might', 'nation', 'never', 'new', 'nobly', 'nor', 'not', 'note', 'november', 'now', 'of', 'on', 'or', 'our', 'people', 'perish', 'place', 'poor', 'portion', 'power', 'proper', 'proposition', 'rather', 'remaining', 'remember', 'resolve', 'resting', 'say', 'score', 'sense', 'seven', 'shall', 'should', 'so', 'struggled', 'take', 'task', 'testing', 'that', 'the', 'their', 'these', 'they', 'this', 'those', 'thus', 'to', 'under', 'unfinished', 'us', 'vain', 'war', 'we', 'what', 'whether', 'which', 'who', 'will', 'work', 'world', 'years']
unique = 0
d = {}

for line in sys.stdin:
    line = line.strip().lower()
    s = remove_punctuation(line)
    word_count(s)

print(len(d) + 1)
