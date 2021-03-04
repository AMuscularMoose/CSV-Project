# 1) handle error checking using try and except
# 2) change file to use death valley date


import csv
from datetime import datetime


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)
    #skip the first record since the first row is just the header
print(type(header_row))

#The enumerate() function returns both the index of each iteam and the value of each
# item as you loop through a list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


highs = []
lows = []
dates = []


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(converted_date)

#you get an error since line 50 in the death_valley csv file is missing info. ^^^ solves that

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor='blue',alpha=.1)


plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()

