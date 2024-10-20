import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# write
# Basic element pertama yang akan kita bahas ialah write. Ia merupakan elemen streamlit yang digunakan untuk menampilkan sebuah output.  Untuk menggunakan element ini, kita hanya perlu memanggil function write() dan diikuti inputan yang ingin ditampilkan.
st.write(
    pd.DataFrame(
        {
            "c1": [1, 2, 3, 4],
            "c2": [10, 20, 30, 40],
        }
    )
)

# text
# Elemen lain yang ada dalam streamlit ialah text (dokumentasi: text). Sesuai dengan namanya, ia merupakan elemen yang digunakan untuk menampilkan sebuah output berupa text. Elemen ini memiliki banyak function yang bisa digunakan sesuai kebutuhan. Berikut merupakan beberapa pilihan yang tersedia saat ini.

# 1. Markdown: Function ini digunakan untuk menampilkan output dari argument markdown.
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# 2. Title: Ini merupakan function yang digunakan untuk menampilkan teks dalam format judul.
st.title("Belajar Analisis Data")

# 3. Header: Function ini digunakan untuk menampilkan output teks sebagai format header.
st.header("Pengembangan Dashboard")

# 4. Subheader: Ini merupakan function yang digunakan untuk menampilkan output teks sebagai format subheader.
st.subheader("Pengembangan Dashboard")

# 5. Caption: Function berikutnya ialah caption(). Ia merupakan function yang digunakan untuk menampilkan output teks dalam ukuran kecil.
st.caption("Copyright (c) 2023")

# 6. Code: Pada beberapa case, kita harus menampilkan potongan kode ke dalam streamlit app (web app yang dibuat menggunakan streamlit). Untuk menjawab hal ini, streamlit telah menyediakan sebuah function bernama code().
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language="python")

# 7. text: Function selanjutnya ialah text(). Function ini digunakan untuk menampilkan sebuah normal teks.
st.text("Halo, calon praktisi data masa depan.")

# 8. latex: Function terakhir yang dapat digunakan untuk menampilkan elemen teks ialah latex(). Sesuai namanya, function tersebut digunakan untuk menampilkan mathematical expression yang ditulis dalam format LaTeX.
st.latex(
    r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
"""
)

# Data display
# 1. Dataframe: Function pertama yang bisa kita gunakan untuk menampilkan data ke dalam streamlit app ialah dataframe(). Ia merupakan function yang digunakan untuk menampilkan DataFrame sebagai sebuah tabel interaktif. Pada function ini, kita bisa mengatur ukuran dari table yang ingin ditampilkan menggunakan parameter width dan height.

df = pd.DataFrame(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

st.dataframe(data=df, width=500, height=150)

# 2. Table: Selain dataframe(), kita juga bisa menggunakan function table()untuk menampilkan data ke dalam streamlit app. Ia dapat digunakan untuk menampilkan data dalam bentuk static table.
st.table(data=df)

# 3. metric: Ketika membuat dashboard, terkadang kita perlu menampilkan sebuah metrik tertentu. Untuk melakukan hal ini, kita bisa memanfaatkan function metric(). Function ini dapat membantu kita untuk menampilkan sebuah metrik tertentu beserta detailnya seperti label, value serta besar perubahan nilainya.
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# 4. json: Selain bentuk DataFrame atau tabel, terkadang kita juga perlu menampilkan data dalam format JSON. Streamlit telah menyediakan function json() untuk menampilkan data dalam format JSON.
st.json(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

# Chart
# Function pyplot() dapat digunakan untuk menampilkan grafik visualisasi data yang dibuat menggunakan matplotlib.
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
