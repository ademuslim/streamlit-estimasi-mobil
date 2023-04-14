import pickle
import streamlit as st

model = pickle.load(open('estimasi-mobil.sav', 'rb'))

# title
st.title('Estimasi Harga Mobil Bekas')

#i nput
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
