#find the frequency of letters

def letter_freq(word):

    word_dict = {ch:word.count(ch) for ch in word}
    print(word_dict)

letter_freq("underestimated")
