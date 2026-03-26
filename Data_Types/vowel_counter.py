"""
1. Vowel Counter (Strings & Integers)

Problem: Write a program that takes a string and returns the count of vowels in it.
"""

def count_vowels(word):
    VOWELS = 'aeiou'
    count = 0
    for ch in word:
        if ch in VOWELS:
            count+=1
    return count

print(count_vowels('adaptability'))
