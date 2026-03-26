# Find the all non-repeating characters.
def non_repeating(string):
    for ch in string:
        if string.count(ch) == 1:
            print(ch,end =" ")
    print()

non_repeating("elemental")
non_repeating("banana")
non_repeating("minimum")
