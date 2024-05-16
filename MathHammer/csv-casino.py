import csv


results = []
with open("casinoresults.csv", mode="r") as file:
    data = csv.reader(file)
    for result in data:
        results.append(result)

    del results[0]

#convert
good_results = []
for dumblistobject in results:
    good_results.append(int(dumblistobject[0]))

print(good_results)

streaks = []
run = []
droughts = []
wins = []
results = []
for spin in good_results:
    results.append(spin)
    if spin == 0:
        run.append(spin)
    else:
        wins.append(spin)
        run.append(spin)
        streaks.append(run)
        run = []

import copy


print(streaks)
droughts = copy.deepcopy(streaks)
for streak in droughts:
    if streak[-1] != 0:
        del streak[-1]

print(streaks)
print(droughts)
drought_lengths = [len(x) for x in droughts]
print(drought_lengths)
print(sum(drought_lengths) / len(drought_lengths))
print(max(drought_lengths))
drought_lengths.sort()
from collections import Counter
drought_counts = Counter(drought_lengths)
print(drought_counts)
print(drought_counts.keys())
print(drought_counts.values())
drought_freqs = []
for thing in drought_counts.values():
    # print(thing)
    drought_freqs.append(thing)


drought_values = []
for thingy in drought_counts.keys():
    print(thingy)
    drought_values.append(int(thingy))

print(drought_values)
print(drought_freqs)

import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Drought Length":drought_values,
    "Quantity":drought_freqs
}
df = pd.DataFrame(data)
plt.bar(df["Drought Length"],df["Quantity"])
plt.show()

cool_data = zip(drought_values, drought_freqs)
# print(list(cool_data))
total_streaks = sum(drought_freqs)
funny_percentages = []
for qty,freq in cool_data:
    funny_percentages.append(round(freq / total_streaks * 100, 1))
    print(f"{qty}: {freq} ({round(freq/total_streaks*100,1)}% - {sum(funny_percentages)}%)")


print(funny_percentages[0:8])
print(sum(funny_percentages[0:8]))
cumsum = []
for percent in funny_percentages:
    cumsum.append(percent)

wins.sort()
print(wins)
wincounts = Counter(wins)
print(wincounts)
print(sum(wincounts.values()))
box = []
for bingus in wincounts:
    print(bingus, wincounts[bingus])
    print((wincounts[bingus] / sum(wincounts.values()))*100)
    box.append(bingus * wincounts[bingus])

print(sum(box) / sum(wincounts.values()))


spincounts = Counter(results)
print(spincounts)
print(spincounts[0] / (sum(spincounts.values())))

print("-"*50)
streak_lengths = [len(x) for x in streaks]
streak_num = len(streak_lengths)
print(sum(streak_lengths) / streak_num)