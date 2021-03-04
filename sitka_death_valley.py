import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")
csv_file2 = csv.reader(open_file2, delimiter = ",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

for index, column_header in enumerate(header_row):
    if column_header == 'TMAX':
        max_temp_index = index
    if column_header == 'TMIN':
        min_temp_index = index
    if column_header == 'NAME':
        name_index = index

for index2, column_header2 in enumerate(header_row2):
    if column_header2 == 'TMAX':
        max_temp_index2 = index
    if column_header2 == 'TMIN':
        min_temp_index2 = index
    if column_header2 == 'NAME':
        name_index2 = index

highs = []
highs2 = []
lows = []
lows2 = []
dates = []
dates2 = []


for row in csv_file:
    try:
        high = int(row[max_temp_index])
        low = int(row[min_temp_index])
        title = row[name_index]
        converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs.append(int(row[max_temp_index]))
        lows.append(int(row[min_temp_index]))
        dates.append(converted_date)

for row in csv_file2:
    try:
        high2 = int(row[max_temp_index2])
        low2 = int(row[min_temp_index2])
        title2 = row[name_index2]
        converted_date2 = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {converted_date2}")
    else:
        highs2.append(int(row[max_temp_index2]))
        lows2.append(int(row[min_temp_index2]))
        dates2.append(converted_date2)

import matplotlib.pyplot as plt

fig = plt.figure()



fig,ax = plt.subplots(2)

ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")

ax[0].fill_between(dates, highs, lows, facecolor='blue',alpha=.1)

ax[0].title(title, fontsize=16)
ax[0].xlabel("", fontsize=12)
ax[0].ylabel("Temperature (F)", fontsize=12)
ax[0].tick_params(axis="both", labelsize=12)


ax[1].plot(dates2, highs2, c="red")
ax[1].plot(dates2, lows2, c="blue")

ax[1].fill_between(dates2, highs2, lows2, facecolor='blue',alpha=.1)

ax[1].title(title2, fontsize=16)
ax[1].xlabel("", fontsize=12)
ax[1].ylabel("Temperature (F)", fontsize=12)
ax[1].tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()


