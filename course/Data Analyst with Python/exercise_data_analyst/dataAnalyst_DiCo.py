# import library
import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)
import matplotlib.pyplot as plt
import seaborn as sns

# read data csv
customers_df = pd.read_csv("exercise_data_analyst/customers.csv")
orders_df = pd.read_csv("exercise_data_analyst/orders.csv")
product_df = pd.read_csv("exercise_data_analyst/products.csv")
sales_df = pd.read_csv("exercise_data_analyst/sales.csv")

# asseting data
# menilai kualitas dari seluruh data yang akan digunakan

# melihat kualitas data
# print(customers_df.info())
# print(orders_df.info())
# print(product_df.info())
# print(sales_df.info())

# melihat jumlah data yang missing value
# print(customers_df.isna().sum())
# print(sales_df.isna().sum())

# melihat duplikat data
# print(customers_df.duplicated().sum())
# print(f"jumlah duplikasi: {orders_df.duplicated().sum()}")
# print(f"jumlah duplikasi: {product_df.duplicated().sum()}")
# print(f"jumlah duplikasi: {sales_df.duplicated().sum()}")

# gunakan method describe(). Method tersebut akan menampilkan ringkasan parameter statistik (mean, median, dll.) dari kolom numerik pada sebuah DataFrame.
# print(customers_df.describe())
# print(orders_df.describe())
# print(product_df.describe())
# print(sales_df.describe())

# cleaning data

# menghapus duplikasi
customers_df.drop_duplicates(inplace=True)
# print(customers_df.duplicated().sum())

# menangani missing value

# menampilkan data yang memiliki missing value
# print(customers_df[customers_df.gender.isna()])

# mengganti data missing value dengan data yang dominan
# print(customers_df.gender.value_counts())
customers_df.fillna(value="Prefer not to say", inplace=True)
# print(customers_df.isna().sum())

# menangani inaccurate file
# filer
# print(customers_df[customers_df.age == customers_df.age.max()])

# replace
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)

# print(customers_df.describe())

# replace tipe data order
date_order = ["order_date", "delivery_date"]

for kolom in date_order:
    orders_df[kolom] = pd.to_datetime(orders_df[kolom])

# print(orders_df.info())

# menghapus duplikasi data product
product_df.drop_duplicates(inplace=True)
# print(product_df.duplicated().sum())

# menangani missing value data sales
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]
# print(sales_df.isna().sum())

# =================================================================

# start exploratory data

# exploratory customers
# print(customers_df.groupby(by="gender").agg(
#     {
#         "customer_id": "nunique",
#         "age": ["max", "min", "mean", "std"]
#     }
# ))

# print(customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False))
# print(customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False))

# exploratory order
# transform delivery time
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time/86400)

# mencari status pelanggan
customer_id_in_orders_df = orders_df.customer_id.tolist()
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "active" if x in customer_id_in_orders_df else "non active")

# menggabungkan tabel order dan customer
orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)

# melihat jumlah order
# print(orders_customers_df.groupby(by="gender").order_id.nunique().sort_values(ascending=False).reset_index().head(10))

# berdasarkan umur
orders_customers_df["age_group"] = orders_customers_df.age.apply(lambda x: "youth" if x <= 24 else ("senior" if x > 64 else "adults"))
# print(orders_customers_df.groupby(by="age_group").order_id.nunique().sort_values(ascending=False))

# eksplorasi data sales dan produk
# print(product_df.describe())
# print(sales_df.describe())
# print(product_df.sort_values(by="price", ascending=False))

# print(product_df.groupby("product_type").agg(
#     {
#         "product_id": "nunique",
#         "quantity": "sum",
#         "price": ["min", "max"]
#     }
# ))
# print(product_df.groupby("product_name").agg(
#     {
#         "product_id": "nunique",
#         "quantity": "sum",
#         "price": ["min", "max"]
#     }
# ))

sales_product_df = pd.merge(
    left= sales_df,
    right= product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)

# print(sales_product_df.groupby(by="product_name").agg({
#     "sales_id": "nunique",
#     "quantity_x": "sum",
#     "total_price": "sum"
# }).sort_values(by="total_price", ascending=False))

# menggabungkan 4 tabel

# print(all_df.groupby(by=["state", "product_type"]).agg({
#     "quantity_x": "sum",
#     "total_price": "sum"
# }))

# print(all_df.groupby(by=["gender", "product_type"]).agg({
#     "quantity_x": "sum",
#     "total_price": "sum"
# }))
all_df = pd.merge(
    left=sales_product_df,
    right=orders_customers_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)

# ====================================================================

# Data Visualization
# pertanyaan 1: Bagaimana performa penjualan dan revenue perusahaan dalam beberapa bulan terakhir?

# mengubah frekuensi data untuk memperoleh informasi terkait jumlah order dan total revenue yang diperoleh setiap bulannya.

monthly_orders_df = all_df.resample(rule="M", on="order_date").agg({
    "order_id": "nunique",
    "total_price": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime("%Y-%m")
monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)

# plt.figure(figsize=(10, 5))
# plt.plot(
#     monthly_orders_df["order_date"],
#     monthly_orders_df["order_count"],
#     marker="o",
#     linewidth=2,
#     color="#72BCD4",
# )
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.show()

# pertanyaan 2: Produk apa yang paling banyak dan paling sedikit terjual?

# membuat df untun menampung data total penjualan produk
sum_order_items_df = all_df.groupby(by="product_name").quantity_x.sum().sort_values(ascending=False).reset_index()

# menampilkan data dengan diagram batang
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# sns.barplot(x="product_name", y="quantity_x", hue="product_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
# ax[0].set_ylabel(None)
# ax[0].set_xlabel(None)
# ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
# ax[0].tick_params(axis="y", labelsize=12)

# sns.barplot(x="product_name", y="quantity_x", hue="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
# ax[1].set_ylabel(None)
# ax[1].set_xlabel(None)
# ax[1].invert_xaxis()
# ax[1].yaxis.set_label_position("right")
# ax[1].yaxis.tick_right()
# ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
# ax[1].tick_params(axis="y", labelsize=12)

# plt.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)
# plt.show()

# pertanyaan 3: Bagaimana demografi pelanggan yang kita miliki?
# Untuk menjawab hal ini, tentunya kita bisa membuat DataFrame baru untuk menampung informasi terkait jumlah pelanggan untuk demografi tertentu seperti gender, state, dll.

# 1. berdasarkan gender
# membuat dataframe gender

bygender_df = all_df.groupby(by="gender").customer_id.nunique().reset_index()
bygender_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

# plt.figure(figsize=(10, 5))

# sns.barplot(
#     y = "customer_count",
#     x = "gender",
#     hue = "gender",
#     data = bygender_df.sort_values(by="customer_count", ascending=False),
#     palette=colors
# )
# plt.title("Number of Customer by Gender", loc="center", fontsize=15)
# plt.xlabel(None)
# plt.ylabel(None)
# plt.tick_params(axis='x', labelsize=12)
# plt.show()

# 2. berdasarkan usia

byage_df = all_df.groupby(by="age_group").customer_id.nunique().reset_index()
byage_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
byage_df["age_group"] = pd.Categorical(byage_df["age_group"], ["youth", "adults", "senior"])
# plt.figure(figsize=(10, 5))
# colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# sns.barplot(
#     y = "customer_count",
#     x = "age_group",
#     hue = "age_group",
#     data = byage_df.sort_values(by="age_group", ascending=False),
#     palette = colors_
# )
# plt.title("Number of Customer by Age", loc="center", fontsize=15)
# plt.ylabel(None)
# plt.xlabel(None)
# plt.tick_params(axis="x", labelsize=12)
# plt.show()

# berdasarkan state

bystate_df = all_df.groupby(by="state").customer_id.nunique().reset_index()
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
bystate_df
# plt.figure(figsize=(10, 5))
# colors_ = [
#     "#72BCD4",
#     "#D3D3D3",
#     "#D3D3D3",
#     "#D3D3D3",
#     "#D3D3D3",
#     "#D3D3D3",
#     "#D3D3D3",
#     "#D3D3D3",
# ]
# sns.barplot(
#     x="state",
#     y="customer_count",
#     data=bystate_df.sort_values(by="customer_count", ascending=False),
#     palette=colors_,
# )
# plt.title("Number of Customer by States", loc="center", fontsize=15)
# plt.ylabel(None)
# plt.xlabel(None)
# plt.xticks(rotation=15)
# plt.tick_params(axis="y", labelsize=12)
# plt.show()

# RFM Analyst: RFM analysis merupakan salah satu metode yang umum digunakan untuk melakukan segmentasi pelanggan (mengelompokkan pelanggan ke dalam beberapa kategori) berdasarkan tiga parameter, yaitu recency, frequency, dan monetary.
# Recency: parameter yang digunakan untuk melihat kapan terakhir seorang pelanggan melakukan transaksi.
# Frequency: parameter ini digunakan untuk mengidentifikasi seberapa sering seorang pelanggan melakukan transaksi.
# Monetary: parameter terakhir ini digunakan untuk mengidentifikasi seberapa besar revenue yang berasal dari pelanggan tersebut.

rfm_df = all_df.groupby(by="customer_id", as_index=False).agg(
    {
        "order_date": "max",  # mengambil tanggal order terakhir
        "order_id": "nunique",  # menghitung jumlah order
        "total_price": "sum",  # menghitung jumlah revenue yang dihasilkan
    }
)

rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]

# menghitung kapan terakhir pelanggan melakukan transaksi (hari)
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
recent_date = orders_df["order_date"].dt.date.max()
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
# print(rfm_df.head(15))

# visualisasi rfm
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(
    y="recency",
    x="customer_id",
    data=rfm_df.sort_values(by="recency", ascending=True).head(5),
    palette=colors,
    ax=ax[0],
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis="x", labelsize=15)

sns.barplot(
    y="frequency",
    x="customer_id",
    data=rfm_df.sort_values(by="frequency", ascending=False).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis="x", labelsize=15)

sns.barplot(
    y="monetary",
    x="customer_id",
    data=rfm_df.sort_values(by="monetary", ascending=False).head(5),
    palette=colors,
    ax=ax[2]
)
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis="x", labelsize=15)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)
plt.show()

