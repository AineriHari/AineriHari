import random
import pandas as pd
from matplotlib import pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation


plt.style.use("fivethirtyeight")

x_vals = []
y_vals = []

index = count()


def animate(i):
    file = pd.read_csv("data_gen.csv")
    x = file["x_value"]
    y1 = file["total_1"]
    y2 = file["total_2"]

    plt.cla()
    plt.plot(x, y1, label="channel 1")
    plt.plot(x, y2, label="channel 2")

    plt.legend(loc="upper left")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# plt.plot(x_vals, y_vals)


plt.tight_layout()
plt.show()
