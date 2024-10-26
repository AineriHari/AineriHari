import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

# fig, ax = plt.subplots()

# ax.plot(ages, py_salaries, label="Python")
# ax.plot(ages, js_salaries, label="JavaScript")

# ax.plot(ages, dev_salaries, color="#444444", linestyle="--", label="All Devs")

# ax.legend()

# ax.set_title("Median salary (USD) by age")
# ax.set_xlabel("Ages")
# ax.set_ylabel("Median salary (USD)")

# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color="#444444", linestyle="--", label="All Devs")

ax2.plot(ages, py_salaries, label="Python")
ax2.plot(ages, js_salaries, label="JavaScript")

ax1.legend()

ax1.set_title("Median salary (USD) by age")
ax1.set_xlabel("Ages")
ax1.set_ylabel("Median salary (USD)")

ax2.legend()

ax2.set_title("Median salary (USD) by age")
ax2.set_xlabel("Ages")
ax2.set_ylabel("Median salary (USD)")

plt.tight_layout()
plt.show()
