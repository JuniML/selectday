import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite day?',
     ('Fri', 'Sun', 'Tue'))

st.write('Your favorite day is ', option)