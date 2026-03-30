#Find longest streak of a habit performed ,true = Habit done

def longest_streak(habit):
    max_streak = 0
    current_streak = 0

    for h in habit:
        if h == True:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak
 

print(longest_streak([True,False,True,True,True,True]))


