"""
Break Amount into Notes 💰
Given an amount, display number of:

2000 notes

500 notes

200 notes

100 notes

👉 Example: ₹3800 → 1×2000, 3×500, ...
"""
def money(amount):
                    
    
    two_thousand = amount//2000
    print("two-thousand rupee notes = ",two_thousand,"x 2000")
    amount = amount%2000

    
    five_hundred = amount//500
    print("five hundred rupee notes =",five_hundred,"x 500")
    amount = amount%500
    
    
    two_hundred = amount//200
    print("two hundred rupee notes =",two_hundred,"x 200")
    amount = amount%200
    

    hundred = amount//100
    print("hundred rupee notes =",hundred,"x 100")

money(5600)
print("\t")
money(3700)





