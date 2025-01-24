import streamlit as st
import requests
import pandas as pd
'''
# TaxiFareModel front
'''

datentime = st.text_input('Date and time', '2014-07-06 19:18:00')
pickup_long = st.text_input('Pickup longitude', -73.950655)
pickup_lat = st.text_input('Pickup latitude', 40.783282)
dropoff_long = st.text_input('Dropoff longitude', -73.984365)
dropoff_lat = st.text_input('Dropoff latitude', 40.769802)
n_passengers = st.text_input('Number of passengers', 2)


url = 'https://taxifare-1019856209529.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {
    'pickup_datetime': datentime,
    'pickup_longitude': pickup_long,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_long,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': n_passengers
}

response = requests.get(url, params)
data = response.json()['fare']

st.write(f'### The price of your ride is estimated in: {round(data,2)}U$')

def get_map_data():

    return pd.DataFrame(
            [[float(pickup_lat),float(pickup_long)], [float(dropoff_lat), float(dropoff_long)]],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)
