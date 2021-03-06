#1)
#2)
#3)
#4) Shade in the area between high and low



import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)
    #skip the first record since the first row is just the header

#The enumerate() function returns both the index of each iteam and the value of each
# item as you loop through a list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


highs = []
lows = []
dates = []

# we call the method striptime() using the string 

#as an example
#somedate = '2017-07-01'
#converted_date = datetime.strptime(somedate,'%Y-%m-%d')
#print(converted_date)



for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

#print(highs)

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
'''
fig2, a =plt.subplots(2)
a[0].plot(dates,highs, c= 'red')
a[1].plot(dates,lows, c= 'blue')

plt.show()
'''