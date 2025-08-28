# # import streamlit as st

# # st.set_page_config(page_title="Kalkulator Modal Kopi", page_icon="☕")

# # st.title("☕ Kalkulator Modal Espresso Cup")

# # # Input
# # harga_kopi = st.number_input("Harga Biji Kopi per 1 kg (Rp)", min_value=0, value=180000, step=1000)
# # gram_per_kg = 1000
# # gram_per_cup = st.number_input("Jumlah gram per espresso cup", min_value=1.0, value=9.0, step=0.1)

# # # Hitung jumlah cup dan modal per cup
# # jumlah_cup = gram_per_kg / gram_per_cup
# # modal_per_cup = harga_kopi / jumlah_cup

# # # Output
# # st.markdown("---")
# # st.subheader("📈 Hasil Perhitungan")
# # st.write(f"Jumlah cup dari 1 kg kopi: **{jumlah_cup:.2f} cup**")
# # st.write(f"Modal per espresso cup: **Rp {modal_per_cup:,.2f}**")


# import streamlit as st

# st.set_page_config(page_title="Kalkulator HPP Kopi", page_icon="☕")

# st.title("☕ Kalkulator HPP Kopi per Cup")

# st.markdown("Masukkan informasi bahan baku di bawah ini untuk menghitung HPP kopi per cup.")

# # =====================
# # Input Harga dan Penggunaan Beans
# # =====================
# st.header("🫘 Beans (Kopi)")
# harga_beans = st.number_input("Harga Biji Kopi (Rp)", min_value=0, value=190000, step=1000)
# jumlah_total_beans = st.number_input("Jumlah berat kopi yang dibeli", min_value=1.0, value=1000.0, step=1.0)
# satuan_beans = st.selectbox("Satuan berat tersebut", ["gram", "kilogram"])
# gram_per_cup = st.number_input("Jumlah gram beans per espresso cup", min_value=0.1, value=8.0, step=0.1)

# # Konversi berat total ke gram
# total_gram_beans = jumlah_total_beans if satuan_beans == "gram" else jumlah_total_beans * 1000

# # Hitung HPP Beans per cup
# hpp_beans = (harga_beans / total_gram_beans) * gram_per_cup

# # =====================
# # Input Susu
# # =====================
# st.header("🥛 Susu")
# nama_susu = st.text_input("Merk Susu yang Digunakan", value="Diamond Fresh Milk")
# harga_susu = st.number_input("Harga Susu", min_value=0, value=24000, step=1000)
# satuan_susu_liter = st.number_input("Isi total susu (dalam liter)", min_value=0.1, value=1.0, step=0.1)
# jumlah_ml_per_cup = st.number_input("Jumlah susu yang digunakan per cup (ml)", min_value=1, value=60)

# # Hitung HPP Susu
# hpp_susu = (harga_susu / (satuan_susu_liter * 1000)) * jumlah_ml_per_cup

# # =====================
# # Input Creamer
# # =====================
# st.header("🧁 Creamer")
# nama_creamer = st.text_input("Merk Creamer yang Digunakan", value="Indomilk Krimer Bubuk")
# harga_creamer = st.number_input("Harga Creamer", min_value=0, value=33000, step=1000)
# satuan_creamer_gram = st.number_input("Total isi Creamer (gram)", min_value=1, value=1000)
# jumlah_gram_creamer_per_cup = st.number_input("Jumlah creamer per cup (gram)", min_value=0.1, value=20.0, step=0.1)

# # Hitung HPP Creamer
# hpp_creamer = (harga_creamer / satuan_creamer_gram) * jumlah_gram_creamer_per_cup

# # =====================
# # Output
# # =====================
# total_hpp = hpp_beans + hpp_susu + hpp_creamer

# st.markdown("---")
# st.subheader("📊 Hasil Perhitungan HPP per Cup")
# st.write(f"**HPP Beans:** Rp {hpp_beans:,.2f}")
# st.write(f"**HPP Susu ({nama_susu}):** Rp {hpp_susu:,.2f}")
# st.write(f"**HPP Creamer ({nama_creamer}):** Rp {hpp_creamer:,.2f}")

# st.markdown("### 💰 **Total HPP per Cup: Rp {:,.2f}**".format(total_hpp))

import streamlit as st
import pandas as pd
import os

# Set the title of the Streamlit app
st.title('Aplikasi Perhitungan HPP Kopi Kala Nanti')
st.write('---')

# --- Data Loading and Preprocessing ---
@st.cache_data
def load_and_process_all_sheets():
    """
    Loads all necessary data from the single Excel file with correct headers by dynamically finding them.
    This function expects the file to be in the same directory.
    """
    excel_file = 'HPP_Kopi Kala Nanti.xlsx'
    
    if not os.path.exists(excel_file):
        st.error(f"Error: The file '{excel_file}' was not found in the current directory.")
        return None, None, None, None

    try:
        # Load main data sheets with header on row 1 (index 0)
        df_baku = pd.read_excel(excel_file, sheet_name='Komponen Baku')
        df_baku['Bahan'] = df_baku['Jenis barang'].fillna(df_baku['Brand']).fillna(df_baku['Vendor'])
        df_baku = df_baku.set_index('Bahan')

        df_buatan = pd.read_excel(excel_file, sheet_name='Komponen Buatan')
        df_buatan = df_buatan.set_index('Jenis barang')

        df_list_menu = pd.read_excel(excel_file, sheet_name='List Menu')

        # Dictionary to store menu and component recipes
        recipes = {}
        recipe_sheets = ['Komponen 1', 'Komponen 2', 'Menu 1', 'Menu 2', 'Menu 3', 'Menu 4']
        
        for sheet_name in recipe_sheets:
            try:
                # Read the sheet to find the header row dynamically
                temp_df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
                
                # Find the row index that contains the string 'Bahan'
                header_row_index = temp_df[temp_df.eq('Bahan').any(axis=1)].index.tolist()
                
                if not header_row_index:
                    st.warning(f"Skipping sheet '{sheet_name}': Could not find the 'Bahan' column.")
                    continue
                
                # Get the header index (0-based)
                header_index = header_row_index[0]
                
                # Read the sheet again, this time with the correct header
                df = pd.read_excel(excel_file, sheet_name=sheet_name, header=header_index)

                # Get the name from the first row, second column
                name = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, nrows=1).iloc[0, 1]
                
                recipes[name] = df

            except Exception as e:
                st.warning(f"Could not load sheet '{sheet_name}'. Error: {e}")
        
        return df_baku, df_buatan, df_list_menu, recipes

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses file: {e}")
        return None, None, None, None

df_baku, df_buatan, df_list_menu, recipes = load_and_process_all_sheets()

# --- HPP Calculation Function ---
def calculate_hpp(menu_name, recipes, df_baku, df_buatan):
    """
    Calculates the HPP for a given menu item by summing up the costs of its ingredients.
    """
    if menu_name not in recipes:
        return None, "Menu not found."

    df_recipe = recipes[menu_name]
    total_hpp = 0
    breakdown = []
    
    required_cols = ['Bahan', 'Takaran pemakaian']
    if not all(col in df_recipe.columns for col in required_cols):
         st.error(f"Kolom yang diperlukan tidak ditemukan dalam resep '{menu_name}'. Kolom yang tersedia: {list(df_recipe.columns)}")
         return None, "Kolom tidak lengkap."

    # Iterate through each ingredient
    for index, row in df_recipe.iterrows():
        ingredient = row['Bahan']
        usage_quantity = row['Takaran pemakaian']
        
        if pd.isna(ingredient) or pd.isna(usage_quantity):
            continue

        cost_per_unit = 0
        
        if ingredient in df_buatan.index:
            try:
                comp_hpp = df_buatan.loc[ingredient, 'Harga (IDR)']
                comp_qty = df_buatan.loc[ingredient, 'Quantity']
                cost_per_unit = comp_hpp / comp_qty
            except KeyError:
                st.warning(f"Warning: HPP untuk komponen buatan '{ingredient}' tidak ditemukan.")
        elif ingredient in df_baku.index:
            try:
                raw_price = df_baku.loc[ingredient, 'Harga (IDR)']
                raw_quantity = df_baku.loc[ingredient, 'Quantity']
                cost_per_unit = raw_price / raw_quantity
            except KeyError:
                st.warning(f"Warning: HPP untuk bahan baku '{ingredient}' tidak ditemukan.")
        elif 'Harga (IDR)' in row and not pd.isna(row['Harga (IDR)']):
             cost_per_unit = row['Harga (IDR)'] / row['Takaran pemakaian'] if row['Takaran pemakaian'] != 0 else 0
        
        ingredient_cost = usage_quantity * cost_per_unit
        total_hpp += ingredient_cost
        breakdown.append({'Bahan': ingredient, 'Takaran Pemakaian': usage_quantity, 'Harga per Takaran': ingredient_cost})
    
    return total_hpp, pd.DataFrame(breakdown)

# --- Streamlit App Layout ---
if df_list_menu is not None and recipes is not None:
    menu_options = df_list_menu['Nama Menu'].tolist()
    selected_menu = st.selectbox('Pilih Menu', menu_options)
    
    if selected_menu:
        menu_file_name = None
        for key in recipes:
            if selected_menu == key:
                menu_file_name = key
                break
        
        if menu_file_name:
            st.write(f'### Rincian Perhitungan HPP untuk "{selected_menu}"')
            hpp, breakdown_df = calculate_hpp(menu_file_name, recipes, df_baku, df_buatan)
            
            if hpp is not None:
                st.metric(label="Total HPP", value=f'Rp {hpp:,.2f}')
                st.write('#### Rincian Bahan:')
                st.dataframe(breakdown_df)
            else:
                st.error("Gagal menghitung HPP. Mohon periksa file data.")
        else:
            st.warning("Data resep untuk menu yang dipilih tidak ditemukan.")
