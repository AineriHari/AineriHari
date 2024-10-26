from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50]

plt.hist(ages, bins=bins, edgecolor="black", label="Number of Respondents")

median_age = 29
color = "#fc4f30"

plt.axvline(median_age, color=color, label="Age Median", linewidth=2)


plt.xlabel("Ages")
plt.ylabel("Total Respondents")
plt.title("Ages of Respondents")

plt.tight_layout()

plt.legend()
plt.show()
