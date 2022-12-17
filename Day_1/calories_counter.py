

with open("testinput1.txt", 'r') as file:
    calories, low_cal, mid_cal, max_cal = 0,0,0,0
    for i in file:
        if i != '\n':
            calories += int(i.strip())
        else:
            if calories > max_cal:
                low_cal = mid_cal
                mid_cal = max_cal
                max_cal = calories
            elif calories > mid_cal:
                low_cal = mid_cal
                mid_cal = calories
            elif calories > low_cal:
                low_cal = calories
            calories = 0

print("total= "+str(max_cal+mid_cal+low_cal))
