# Remove all digits from a string.

#using sentence with isdigit()
def remove_digits_string(string):

    result = ""
    for ch in string:
        if not ch.isdigit():
            result += ch
    print( result)

string_input = input("Enter sentence: ")
remove_digits_string(string_input)


#single word
def remove_digits(string):
    for ch in string:
        if ch.isalpha() :
            print(ch,end="")

remove_digits("3dyn7amite8")