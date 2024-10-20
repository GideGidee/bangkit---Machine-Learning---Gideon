import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame yang Anda miliki
bike_df = pd.DataFrame(
    {
        "workingday": [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        "cnt": [
            985,
            801,
            1349,
            1562,
            1600,
            1606,
            959,
            822,
            1321,
            1263,
            1162,
            1406,
            1406,
        ],
    }
)

# Hitung agregasi (sum dan mean)
avg_rental_by_workingday = bike_df.groupby(by="workingday").agg(
    {  
        "cnt": ["sum", "mean"],
    }
)

# Reset multi-index agar kolom lebih sederhana
avg_rental_by_workingday.columns = ["total_count", "avg_count"]
avg_rental_by_workingday = avg_rental_by_workingday.reset_index()

print(avg_rental_by_workingday)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3"]

sns.barplot(x="workingday", y="total_count", data=avg_rental_by_workingday, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Rata-rata penyewa berdasarkan workingday", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="workingday", y="total_count", data=avg_rental_by_workingday, palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Rata-rata penyewa berdasarkan workingday", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

plt.suptitle("Jumlah dan rata-rata penyewa berdasarkan workingday", fontsize=20)
plt.show()

# Visualisasi dengan seaborn
# sns.barplot(
#     data=avg_rental_by_workingday,
#     x="workingday",
#     y="avg_count",
#     hue="total_days",
#     errorbar=None,
# )

# # Tambahkan label untuk sumbu
# plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan")
# plt.xlabel("Hari (0: Akhir Pekan, 1: Hari Kerja)")
# plt.ylabel("Rata-rata Penyewaan Sepeda")
# plt.show()