import pickle
import streamlit as st

model = pickle.load(open('estimasi-mobil.sav', 'rb'))

# sidebar
st.sidebar.header('Tugas Akhir Data Mining')
st.sidebar.write('Ade Muslim 312010147')
st.sidebar.write('Esya Mulyana Tarmedi 312010163')
st.sidebar.write('Diki Perliansyah 312010228')
st.sidebar.write('TI.20.D.2')

# title
st.title('Estimasi Harga Mobil Bekas Hyundai')

# input
year = st.number_input('Masukan Tahun Mobil')
mileage = st.number_input('Masukan Km Mobil')
tax = st.number_input('Masukan Pajak Mobil')
mpg = st.number_input('Masukan Konsumsi BBM Mobil')
engineSize = st.number_input('Masukan Engine Size')

# predict
predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict * 19000)
