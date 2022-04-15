
import streamlit as st
import pandas as pd
import plotly.express as px
import math
#import turicreate as tc

import numpy as np
from PIL import Image

def func_eda():
    st.title("EXPLORATORY DATA ANALYSIS")
    image1 = Image.open('gender.png')
    st.header("Distribution of Customers by Sex")
    st.image(image1)



    image2=Image.open('segment.png')
    st.header("Number of Customers in each Segment")
    st.image(image2)

    image3=Image.open('actindex.png')
    st.header("Activity Index of Customers")
    st.image(image3)

    image4=Image.open("channel.png")
    st.header("Number of Customers joined through different channels")
    st.image(image4)

    image5=Image.open('findex.png')
    st.header("Foreign Index")
    st.image(image5)

    image6=Image.open('pop.png')
    st.header("Popularity of products by Activity Index and Sex")
    st.image(image6)

    Image7=Image.open('distbyseg.png')
    st.header("Products purchased by customer in each Segment")
    st.image(Image7)

    Image8=Image.open('prodinc.png')
    st.header("Distribution of products by Income Group")
    st.image(Image8)

    Image9=Image.open('prodage.png')
    st.header("Distribution of product by Age Group")
    st.image(Image9)



def main():
    st.title("DASHBOARD")
    menu = ["EDA"]
    choice = st.sidebar.selectbox("Options", menu)

    if choice=='EDA':
        func_eda()

    # if choice=='Product Recommendation':


if __name__ == '__main__':
    main()