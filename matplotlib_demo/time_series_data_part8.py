from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


plt.style.use("fivethirtyeight")

dates = [
    datetime(2024, 6, 1),
    datetime(2024, 6, 2),
    datetime(2024, 6, 3),
    datetime(2024, 6, 4),
    datetime(2024, 6, 5),
    datetime(2024, 6, 6),
    datetime(2024, 6, 7),
]

y = [0, 1, 3, 4, 6, 5, 7]


plt.plot_date(dates, y, linestyle="solid")

plt.gcf().autofmt_xdate()

date_formater = mpl_dates.DateFormatter("%b, %d %Y")

plt.gca().xaxis.set_major_formatter(date_formater)

plt.tight_layout()

plt.show()
