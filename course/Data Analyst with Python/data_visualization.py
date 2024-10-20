import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

cities = (
    "Bogor",
    "Bandung",
    "Jakarta",
    "Semarang",
    "Yogyakarta",
    "Surakarta",
    "Surabaya",
    "Medan",
    "Makassar",
)

populations = (
    45076704,
    11626410,
    212162757,
    19109629,
    50819826,
    17579085,
    3481,
    287750,
    785409,
)

df = pd.DataFrame(
    {
        "Cities": cities,
        "Populations": populations
    }
)

df.sort_values(by="Populations", inplace=True)

# bar chart

# plt.bar(x=cities, height=populations)
# plt.xticks(rotation=45)

# plt.barh(y=cities, width=populations)

# plt.barh(y=df["Cities"], width=df["Populations"])
# sns.barplot(y=df["Cities"], x=df["Populations"], orient="h", color="blue")
# plt.xlabel("Populations (millions)")
# plt.ylabel("Population of cities in indonesia")
# plt.show()

# ============================================================================

# pie chart
# x: menampung data yang akan divisualisasikan.
# explode: menampung array atau list yang mengatur posisi tiap irisan lingkaran.
# labels: sekumpulan string yang digunakan untuk memberi label pada tiap irisan lingkaran.
# colors: sekumpulan warna yang akan digunakan pada tiap irisan lingkaran.
# autopct: string yang digunakan untuk memberi numerik label pada tiap irisan lingkaran.

# flavors = ("Chocolate", "Vanilla", "Macha", "Others")
# votes = (50, 20, 30, 10)
# colors = ("#8B4513", "#FFF8DC", "#93C572", "#E67F0D")
# explode = (0.1, 0, 0, 0)

# plt.pie(
#     x=votes,
#     labels=flavors,
#     autopct='%1.1f%%',
#     colors=colors,
#     explode=explode
# )
# plt.show()

# =======================================================================

# histogram

# x = np.random.normal(15, 5, 250)

# plt.hist(x=x, bins=15)
# sns.histplot(x=x, bins=15, kde=True)
# plt.show()

# Pada contoh kode di atas, kita menggunakan function random.normal() yang disediakan oleh library numpy untuk menghasilkan sampel data acak yang memiliki distribusi normal. Sample data random tersebut memiliki jumlah 250 titik data dengan nilai mean sebesar 15 dan standard deviation sebesar 5.

# ============================================================================

# box plot
# sns.boxplot(x)
# plt.show()

# =============================================================================

# scatter plot

# lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 9.96, 7.21, 10.04, 10.2, 11.06]
# lemon_weight = [
#     112.05,
#     114.58,
#     116.71,
#     117.4,
#     128.93,
#     132.93,
#     138.92,
#     145.98,
#     148.44,
#     152.81,
# ]

# sns.scatter(x=lemon_diameter, y=lemon_weight)
# sns.scatterplot(x=lemon_diameter, y=lemon_weight)
# sns.regplot(x=lemon_diameter, y=lemon_weight)
# plt.show()

# =====================================================

# line chart
# plt.plot(lemon_diameter, lemon_weight)
# plt.show()

# url = "https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true"

# df = pd.read_csv(url)
# df["Date"] = pd.to_datetime(df["Date"])

# plt.figure(figsize=(12, 5))
# plt.plot(df["Date"], df["Close"], color="red")
# plt.xlabel("Date", size=15)
# plt.ylabel("Price", size=15)
# plt.show()

# =============================================================

# Clustered Bar Chart

# penguins = sns.load_dataset("penguins")

# sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)
# sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species", style="species")
# plt.show()
