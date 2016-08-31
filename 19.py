days = [1, 2, 3, 4, 5, 6, 7] # 7 = Sunday

sundays = 0
def nbDaysForMonth(month, year):
    nbDays = 31
    if month in [4, 6, 9, 11]:
        nbDays = 30
    elif month == 2:
        if year % 4 == 0:
            nbDays = 29
        else:
            nbDays = 28
    return nbDays

i = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        nbDays = nbDaysForMonth(month, year)
        for day in range(1, nbDays + 1):
            if days[i] == 7 and year > 1900 and day == 1:
                print year, month, day
                sundays += 1
            i += 1
            if i > 6:
                i = 0

print sundays