import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)
    #skip the first record since the first row is just the header

#The enumerate() function returns both the index of each iteam and the value of each
# item as you loop through a list

for index, column_header in enumerate(header_row):
    #print("Index:", index, "Column Name:", column_header)
    if column_header == 'TMAX':
        max_temp_index = index
    if column_header == 'NAME':
        name_index = index

highs = []

for row in csv_file:
    highs.append(int(row[max_temp_index]))
    title = row[name_index]
print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title(title, fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
