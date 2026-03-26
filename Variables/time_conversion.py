"""
Seconds to Time Format
Convert total seconds into hours, minutes, seconds.

👉 Example: 3665 → 1 hr 1 min 5 sec
"""
def time(seconds):
    hours = seconds//3600  #hours = 3665//3600 ,1 hr
    print(hours,"hr")

    remaining = seconds % 3600      #3665 % 3600 = remain 65
    minutes = remaining//60          #65//60 = 1
    print(minutes,"min")
    
    seconds = remaining % 60        #65%60 = 5      
    print(seconds,"sec")
    return hours,minutes,seconds

print(time(3665))
print(time(4682))
