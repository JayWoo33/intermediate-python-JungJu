def get_days_in_month(moth, year):
    if (((year%4==0) and (year%100!=0))and(moth==2)) or ((year%400==0)and moth==2) :
        return 29
    
    if moth==2:
         return 28
    elif moth== 4 or moth==6 or moth==9 or moth==11:
        return 30
    else:
        return 31
