import streamlit as st
import pandas as pd
# To create a scatter plot
import altair as alt
import numpy as np
import math
import json

def app():
    # Utility functions
    def round_up(n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    # Session state - to save the values users has entered
    if "x_index" not in st.session_state:
        st.session_state.x_index = 1
    if "y_index" not in st.session_state:
        st.session_state.y_index = 0
    # this is for the range of values selection for subsr_count & view_count
    if "subscribers_count_scale" not in st.session_state:
        st.session_state.subscribers_count_scale = (0, 0)
    if "view_count_scale" not in st.session_state:
        st.session_state.view_count_scale = (0, 0)

    st.title('📺 YouTube Channel Data Analytics')
    st.text('\n')

    # Reading the JSON data
    with open('j_lbc22u8v26q3b0ourv.json',encoding="utf8") as f:
        json_data = json.load(f)

    # Data Wrangling/ Filtering
    df = pd.DataFrame(json_data[1:]) # taking the k:v pairs from 1:
    df.drop(['input', 'query'], inplace=True, axis=1) # drop query and input column for each channel Id
    df.insert(0, 'channel_id', df.pop('channel_id')) # insert a new column channel_id
    df = df[df.subscribers_count.str.isnumeric()]
    df.subscribers_count = pd.to_numeric(df.subscribers_count)
    df.view_count = pd.to_numeric(df.view_count)

    # Selectbox with different options
    col1, col2 = st.columns(2)
    options = ['subscribers_count', 'video_count', 'view_count']
    selected_x = col1.selectbox('Choose a variable for the X-axis', options, index=st.session_state.x_index)
    selected_y = col2.selectbox('Choose a variable for the Y-axis', options, index=st.session_state.y_index)

    if (selected_x == 'subscribers_count') or (selected_y == 'subscribers_count'):
        variable_min = 0
        variable_max = max(df.subscribers_count)
        st.session_state.subscribers_count_scale = st.slider('Select the range values for subscriber_count',
                                                             variable_min, variable_max, (variable_min, variable_max))
        ## Trim the DataFrame according to the selected range values
        # df = df[df.subscribers_count<st.session_state.subscribers_count_scale[1]]
        df = df[df.subscribers_count < round_up(st.session_state.subscribers_count_scale[1], -7)]
        df = df[df.subscribers_count > st.session_state.subscribers_count_scale[0]]

    if (selected_x == 'view_count') or (selected_y == 'view_count'):
        variable_min = 0
        variable_max = int(round_up(max(df.view_count), -8))
        # st.session_state.view_count_scale = st.slider('Select the range values for view_count', variable_min, variable_max, (variable_min, variable_max))
        # st.session_state.view_count_scale = st.slider('Select the range values for view_count', 0, 7000000000, (0, 7000000000))
        st.session_state.view_count_scale = st.slider('Select the range values for view_count (in billions)', 0.0, 7.0,
                                                      (0.0, 7.0), step=0.01)
        # st.session_state.view_count_scale = (0,7000000000)
        ## Trim the DataFrame according to the selected range values
        df = df[df.view_count < st.session_state.view_count_scale[1] * 1000000000]
        df = df[df.view_count > st.session_state.view_count_scale[0] * 1000000000]

    # Creating the scatter plot
    # E74C3C
    chart = alt.Chart(df).mark_circle(color='Blue').encode(
        x=selected_x,
        y=selected_y,
        # x = alt.X(selected_x, scale = xscale),
        # y = alt.Y(selected_y, scale = yscale),
        tooltip=['channel_id', 'subscribers_count', 'video_count', 'view_count']
    )

    st.altair_chart(chart, use_container_width=True)

    # Expandable dataframe
    with st.expander('Show DataFrame'):
        st.write(df)