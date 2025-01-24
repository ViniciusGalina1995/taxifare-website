import streamlit as st
import requests
import pandas as pd
import numpy as np
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
datentime = st.text_input('Date and time')
pickup_long = st.text_input('Pickup longitude')
pickup_lat = st.text_input('Pickup latitude')
dropoff_long = st.text_input('Dropoff longitude')
dropoff_lat = st.text_input('Dropoff latitude')
n_passengers = st.text_input('Number of passengers')


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-1019856209529.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
params = {
    'pickup_datetime': datentime,
    'pickup_longitude': pickup_long,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_long,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': n_passengers
}

response = requests.get(url, params)
data = response.json()

st.write(data)

def get_map_data():

    return pd.DataFrame(
            [[float(pickup_lat),float(pickup_long)], [float(dropoff_lat), float(dropoff_long)]],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)


