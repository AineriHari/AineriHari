import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
# plt.xkcd()

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# x_indexes = np.arange(len(ages_x))
# width = 0.25

# py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# plt.bar(x_indexes - width, py_dev_y, width=width, color="#5a7d9a", linewidth=3, label="Python")

# js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# plt.bar(
#     x_indexes, js_dev_y, width=width, color="#adad3b", linewidth=3, label="JavaScript"
# )

# dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# plt.bar(x_indexes + width, dev_y, width=width, color="#444444", label="All Devs")

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.xlabel("Ages")
# plt.ylabel("Median salary (USD)")
# plt.title("Median salary (USD) by Age")

# plt.legend()

# plt.grid(True)

# plt.tight_layout()

# plt.savefig("plot.png")

# plt.show()

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

languages = ["Python", "JavaScript", "c++", "CSharp", "Ruby", "Go", "Java"]
popularity = [1000, 2000, 500, 400, 600, 300, 1500]

data = zip(languages, popularity)

sorted_data = sorted(list(data), key=lambda x: x[1], reverse=True)

print(sorted_data)

languages = []
popularity = []

for item in sorted_data:
    languages.append(item[0])
    popularity.append(item[1])


# plt.bar(languages, popularity)
plt.barh(languages, popularity)  # vertical bar (bar hedge method)

plt.grid(True)

plt.title("Most Popular Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number Of People Who Use")

plt.tight_layout()

plt.show()
