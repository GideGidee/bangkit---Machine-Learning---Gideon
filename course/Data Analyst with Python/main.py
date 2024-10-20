import numpy as np
import pandas as pd
import scipy
from scipy import stats

# numpy
# array_1 = np.array([2, 3, 6, 5])
# print(array_1)

# pandas
# data = {
#     'Name': ['Lulu', 'Lala', 'Lili'], 
#     'Age': [23, 45, 46]
# }

# df = pd.DataFrame(data)
# print(df)

# scipy
# print(scipy.__version__)

# modus

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]

# print(mode_jumlah_kucing)

# range

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# range = jumlah_kucing.max() - jumlah_kucing.min()
# print(range)


# Interquartile Range
# Interquartile Range atau sering disingkat IQR merupakan parameter statistik yang menggambarkan selisih antara kuartil ketiga (Q3) dan kuartil pertama (Q1).

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
# print(iqr)


# Variance
# parameter yang digunakan untuk menggambarkan besar simpangan suatu titik data dari nilai mean-nya. 

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_kucing_series = pd.Series(jumlah_kucing)
# print(jumlah_kucing_series.var())


# Standard Deviation

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_kucing_series = pd.Series(jumlah_kucing)
# print(jumlah_kucing_series.std())


# distribusi data

# import matplotlib.pyplot as plt
# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# plt.hist(jumlah_kucing, bins=4)
# plt.show()


# skewness

# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_kucing_series = pd.Series(jumlah_kucing)
# print(jumlah_kucing_series.skew())


# korelasi
# Parameter ini digunakan untuk mengidentifikasi korelasi atau hubungan dari dua feature numerik dalam sebuah data

# sample_data = {
#     'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
#     'age': [24, 22, 23, 25, 28],  
#     'communication_skill_score': [85, 70, 75, 90, 90],
#     'quantitative_skill_score': [80, 90, 80, 75, 70]
# }

# df = pd.DataFrame(sample_data)

# print(df.corr(numeric_only=True))


# Covariance
# menggunakan parameter covariance untuk mengidentifikasi hubungan antar dua feature dalam sebuah dataset

# sample_data = {
#     'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
#     'age': [24, 22, 23, 25, 28],  
#     'communication_skill_score': [85, 70, 75, 90, 90],
#     'quantitative_skill_score': [80, 90, 80, 75, 70]
# }

# df = pd.DataFrame(sample_data)

# print(df.cov(numeric_only=True))

