def time(hr,min,zone):
    if zone == "am":
        if hr<12 and min<60:
            return(f"{hr:02}{min:02}")
        elif hr == 12 and min<60:
            return(f"{0:02}{min:02}")
        elif hr>12 or min>60:
            return "Wrong time"
    elif zone == "pm":
        if hr<12 and min<60:
            return(f"{hr+12:02}{min:02} ")
        elif hr == 12 and min<60:
            return(f"{hr}{min:02}")
        elif hr>12 or min>60:
            return "Wrong time" 
    else:
        print("Invalid")

print(time(2,45,"pm"))