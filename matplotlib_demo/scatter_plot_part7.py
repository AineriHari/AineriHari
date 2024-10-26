from matplotlib import pyplot as plt


plt.style.use("seaborn-v0_8")
# print(plt.style.available)


x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
colors = [7, 5, 9, 7]

plt.scatter(
    x, y, s=100, c=colors, cmap="Greens", edgecolor="black", linewidth=1, alpha=0.75
)

# plt.xscale("log")
# plt.yscale("log")

cbar = plt.colorbar()
cbar.set_label("Satisfaction")


plt.tight_layout()
plt.show()
