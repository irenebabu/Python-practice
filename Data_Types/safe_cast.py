"""
5. Safe Number Caster (Strings, Floats & Exceptions)

Problem: Write a function that tries to convert a string to a float. If it fails, return 0.0.


"""

def safe_cast(text):
    try:
        return float(text)
    except Exception as e:
        print(e)
        return 0.0

print(safe_cast('floating'))
print(safe_cast('3.14'))

