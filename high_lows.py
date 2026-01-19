import csv

from matplotlib import pyplot as plt

filename = 'sitka_weather_07_2014.csv'

# Get high temperatures from file.
# Open the file and store the resulting file object in f.
with open(filename) as f:
    # Call csv.reader() and pass it the file object as an argument to create areader object associated with that file.
    reader = csv.reader(f)
    # Returns the next line in the file when passed in the reader object.
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    
    print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()