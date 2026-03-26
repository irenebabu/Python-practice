def check_letter(string, letter):
    for ch in string:
        
        if letter == ch:
            return True
            
            
    return False

print(check_letter("alloy",'y'))
