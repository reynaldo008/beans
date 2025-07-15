import streamlit as st

st.set_page_config(page_title="Kalkulator Modal Kopi", page_icon="☕")

st.title("☕ Kalkulator Modal Espresso Cup")

# Input
harga_kopi = st.number_input("Harga Biji Kopi per 1 kg (Rp)", min_value=0, value=180000, step=1000)
gram_per_kg = 1000
gram_per_cup = st.number_input("Jumlah gram per espresso cup", min_value=1.0, value=9.0, step=0.1)

# Hitung jumlah cup dan modal per cup
jumlah_cup = gram_per_kg / gram_per_cup
modal_per_cup = harga_kopi / jumlah_cup

# Output
st.markdown("---")
st.subheader("📈 Hasil Perhitungan")
st.write(f"Jumlah cup dari 1 kg kopi: **{jumlah_cup:.2f} cup**")
st.write(f"Modal per espresso cup: **Rp {modal_per_cup:,.2f}**")
