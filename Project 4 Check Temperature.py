def check_temp(temp):
    if temp > 28:
        return "HOT"
    
    elif temp >= 18 and temp <= 28:
        return "Warm"
    
    else:
        return "Cold"
    

temp = int(input("Enter Temperature : "))

print(check_temp(temp))