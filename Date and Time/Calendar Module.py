import calendar
day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
lst=input().split (" ")
month,date,year=int(lst[0]),int(lst[1]),int(lst[2])
print (day[calendar.weekday(year, month, date)].upper())
