# Replace every space with a hyphen -
# replace method

def replace_space(sentence):
    result = sentence.replace(" ","-")
    print(result)
    
replace_space("Everyday is a new day.")

#or join method

sentence = "My name is lee"
result = "-".join(sentence.split(" "))
print(result)

#or ,unpacking and separator

sentence = "My name is lee"
print(*sentence.split(), sep="-")