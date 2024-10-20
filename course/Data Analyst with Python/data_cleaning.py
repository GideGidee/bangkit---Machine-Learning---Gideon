# drop
# Metode pertama yang paling mudah ialah men-drop atau menghapus seluruh baris yang mengandung outlier. Metode ini mampu mencegah outlier mempengaruhi hasil analisis yang kita buat.
import pandas as pd

df = pd.read_csv("data.csv")

Q1 = (df["TotalCharges"]).quantile(0.25)
Q3 = (df["TotalCharges"]).quantile(0.75)
IQR = Q3 - Q1

maximum = Q3 + (1.5 * IQR)
minimum = Q1 - (1.5 * IQR)

kondisi_lower_than = df["TotalCharges"] < minimum
kondisi_more_than = df["TotalCharges"] > maximum

df.drop(df[kondisi_lower_than].index, inplace=True)
df.drop(df[kondisi_more_than].index, inplace=True)

# =========================================================

# imputation
# Metode lain yang bisa Anda gunakan untuk menangani outlier ialah imputation. Konsepnya mirip seperti sebelumnya yaitu mengganti outlier dengan nilai tertentu. Nilai yang bisa kita gunakan ialah mean, median, dan mode. Selain itu, tidak jarang juga kita mengganti outlier dengan boundary value.

# Untuk menerapkan metode ini, kita bisa menggunakan method mask() yang disediakan oleh library pandas. Method tersebut menerima parameter cond sebagai kondisi untuk memfilter nilai outlier. Berikut merupakan contoh kode untuk melakukannya.

df = pd.read_csv("data.csv")

Q1 = (df['TotalCharges']).quantile(0.25)
Q3 = (df['TotalCharges']).quantile(0.75)
IQR = Q3 - Q1

maximum = Q3 + (1.5*IQR)
minimum = Q1 - (1.5*IQR)

kondisi_lower_than = df['TotalCharges'] < minimum
kondisi_more_than = df['TotalCharges'] > maximum

df.mask(cond=kondisi_more_than, other=maximum, axis=1, inplace=True)
df.mask(cond=kondisi_lower_than, other=minimum, axis=1, inplace=True)

# =======================================================================

# mengatasi duplikat data

df = pd.read_csv("data.csv")
df.drop_duplicates(inplace=True)