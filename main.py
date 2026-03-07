import pandas as pa
from datetime import date
import datetime

#add page and import file
#file name
x = pa.read_csv("./your_file.csv")
# print(x)
time = x['first_column'].str.split(' ',expand=True) #string


se = x['second_column'].astype(str).str.split(' ', expand=True) #int
# print(se[0][2])

s = {}
co = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday',
}

for i in range(len(se)):
    data = time[0][i].split('-')
    d = int(data[2])
    m = int(data[1])
    y = int(data[0])
    t = date(y,m,d)
    day = t.weekday()
    if day in co:
        day = co[day]
    if day not in s:
        s[day] = int(se[0][i])
    else:
        s[day] += int(se[0][i])

final = dict(sorted(s.items(),key=lambda x: x[1]))
print(final)
