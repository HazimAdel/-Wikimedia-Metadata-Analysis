import matplotlib.pyplot as plt
import numpy as np


def read_col(fname, col=1, convert=int, sep=None):
    with open(fname) as fobj:
        return [convert(line.split(sep=sep)[col]) for line in fobj]


def find_index(list, search_for):
    return list.index(search_for)


def add_to_list(newlist, addstring):
    newlist.append(addstring)


allenteries = []
labels = []
sum_all_files = 0

for i in range(18, 23, 1):
    filename = '2015-12-' + str(i)
    websites = read_col(filename, col=0, convert=str, sep=None)  # Find first column of file
    website_entries = read_col(filename)  # Find second column of file
    sum_of_entries = sum(website_entries)
    index_of_web = find_index(websites, 'en.m.wikipedia.org')  # Find index of wiki
    add_to_list(allenteries,
                round((website_entries[index_of_web] / sum_of_entries) * 100, 3))  # Add entry of wiki to list
    labels.append(filename)
    sum_all_files += sum_of_entries

print(allenteries)

print(sum_all_files)
# FIRST PLOT

# x = np.arange(len(labels))
# width = 0.20
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(x, allenteries, width)
# ax.set_ylabel('English Wikipedia Percentage Axis')
# ax.set_xlabel('Days')
# ax.set_title('en.m.wikipedia.org entries over 5 days')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.set_yticks(np.arange(0, 101, 10))
# ax.legend()
#
# ax.bar_label(rects1, padding=1)
#
#
# fig.tight_layout()
#
# plt.show()


# SECOND PLOT

labels = 'en.m.wikipedia.org', 'Other websites'
wiki_ratio = (sum_of_entries/sum_all_files) * 100
other_ratio = 100 - wiki_ratio
sizes = [wiki_ratio, other_ratio]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()