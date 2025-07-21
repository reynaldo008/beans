# import streamlit as st

# st.set_page_config(page_title="Kalkulator Modal Kopi", page_icon="☕")

# st.title("☕ Kalkulator Modal Espresso Cup")

# # Input
# harga_kopi = st.number_input("Harga Biji Kopi per 1 kg (Rp)", min_value=0, value=180000, step=1000)
# gram_per_kg = 1000
# gram_per_cup = st.number_input("Jumlah gram per espresso cup", min_value=1.0, value=9.0, step=0.1)

# # Hitung jumlah cup dan modal per cup
# jumlah_cup = gram_per_kg / gram_per_cup
# modal_per_cup = harga_kopi / jumlah_cup

# # Output
# st.markdown("---")
# st.subheader("📈 Hasil Perhitungan")
# st.write(f"Jumlah cup dari 1 kg kopi: **{jumlah_cup:.2f} cup**")
# st.write(f"Modal per espresso cup: **Rp {modal_per_cup:,.2f}**")


import streamlit as st

st.set_page_config(page_title="Kalkulator HPP Kopi", page_icon="☕")

st.title("☕ Kalkulator HPP Kopi per Cup")

st.markdown("Masukkan informasi bahan baku di bawah ini untuk menghitung HPP kopi per cup.")

# =====================
# Input Harga dan Penggunaan Beans
# =====================
st.header("🫘 Beans (Kopi)")
harga_beans = st.number_input("Harga Biji Kopi (Rp)", min_value=0, value=190000, step=1000)
jumlah_total_beans = st.number_input("Jumlah berat kopi yang dibeli", min_value=1.0, value=1000.0, step=1.0)
satuan_beans = st.selectbox("Satuan berat tersebut", ["gram", "kilogram"])
gram_per_cup = st.number_input("Jumlah gram beans per espresso cup", min_value=0.1, value=8.0, step=0.1)

# Konversi berat total ke gram
total_gram_beans = jumlah_total_beans if satuan_beans == "gram" else jumlah_total_beans * 1000

# Hitung HPP Beans per cup
hpp_beans = (harga_beans / total_gram_beans) * gram_per_cup

# =====================
# Input Susu
# =====================
st.header("🥛 Susu")
nama_susu = st.text_input("Merk Susu yang Digunakan", value="Diamond Fresh Milk")
harga_susu = st.number_input("Harga Susu", min_value=0, value=24000, step=1000)
satuan_susu_liter = st.number_input("Isi total susu (dalam liter)", min_value=0.1, value=1.0, step=0.1)
jumlah_ml_per_cup = st.number_input("Jumlah susu yang digunakan per cup (ml)", min_value=1, value=60)

# Hitung HPP Susu
hpp_susu = (harga_susu / (satuan_susu_liter * 1000)) * jumlah_ml_per_cup

# =====================
# Input Creamer
# =====================
st.header("🧁 Creamer")
nama_creamer = st.text_input("Merk Creamer yang Digunakan", value="Indomilk Krimer Bubuk")
harga_creamer = st.number_input("Harga Creamer", min_value=0, value=33000, step=1000)
satuan_creamer_gram = st.number_input("Total isi Creamer (gram)", min_value=1, value=1000)
jumlah_gram_creamer_per_cup = st.number_input("Jumlah creamer per cup (gram)", min_value=0.1, value=20.0, step=0.1)

# Hitung HPP Creamer
hpp_creamer = (harga_creamer / satuan_creamer_gram) * jumlah_gram_creamer_per_cup

# =====================
# Output
# =====================
total_hpp = hpp_beans + hpp_susu + hpp_creamer

st.markdown("---")
st.subheader("📊 Hasil Perhitungan HPP per Cup")
st.write(f"**HPP Beans:** Rp {hpp_beans:,.2f}")
st.write(f"**HPP Susu ({nama_susu}):** Rp {hpp_susu:,.2f}")
st.write(f"**HPP Creamer ({nama_creamer}):** Rp {hpp_creamer:,.2f}")

st.markdown("### 💰 **Total HPP per Cup: Rp {:,.2f}**".format(total_hpp))
