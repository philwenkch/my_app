import streamlit as st

import numpy as np
import pandas as pd


## absolut path of this file 
# /Users/philipp/Library/CloudStorage/OneDrive-Persönlich/Dokumente/Digital/Python_Code/plotly_dash/stock_analysis_with_dash/first_test_streamlit.py
#
# .. is for use of -> streamlit run ...
#


#######################################################################
#creating a title of the app
st.title('First App: Uber pickups in NYC')


#fetching data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(20000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done! (using st.cache)')


#######################################################################
# inspect the data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


#######################################################################
#draw histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#######################################################################
#map
st.subheader('Map of all pickups')
st.map(data)

#hour_to_filter = 17
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data, 8, False)



#######################################################################
#
st.subheader('generate random number line graph:')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.subheader('want to know squared numbers from 0..100 ? :')

x = st.slider('x')
st.write(x, 'squared is ', x*x) 