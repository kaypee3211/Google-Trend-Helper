import pandas as pa
from datetime import date
import datetime


#file name
x = pa.read_csv("./time_series_PL_20260206-2248_20260306-2248.csv")
# print(x)
time = x['Time'].str.split(' ',expand=True)


se = x['korki'].astype(str).str.split(' ', expand=True)
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
