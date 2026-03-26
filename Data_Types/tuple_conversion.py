"""
Tuple to Dictionary (Tuples & Dictionaries)

Problem: Convert a tuple of key-value pairs into a dictionary.
"""
def tuple_convert(fruits_tuple):
    fruits_dict = dict(fruits_tuple)
    return fruits_dict

print(tuple_convert((('apple','orange'),('blueberry','strawberry',))))
