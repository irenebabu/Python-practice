"""
Nested datatypes

Access the value 50 from:

data = {"a": [10, 20, {"b": 50}]}
"""

data = {"a": [10, 20, {"b": 50}]}
print(data['a'][2]['b'])
    
