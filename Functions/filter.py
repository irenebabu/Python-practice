def filter_words(lst):

    long_words = list(filter(lambda w: len(w) > 4,lst ))

    return long_words

print(filter_words(["Guitar","pen","Bells","Pin"]))