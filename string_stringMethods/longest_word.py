# Find the longest word in a sentence.
def longest(sentence):
    longest_word = ""
    for w in sentence.split(" "):
        if len(w)>len(longest_word):
            longest_word = w
    return longest_word
        
print(longest("The sun and the moon are friends"))