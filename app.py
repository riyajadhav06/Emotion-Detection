
#imports==================
import streamlit as st
import numpy as np
import pickle
import pandas as pd


#load mode=============
model=pickle.load(open('logistic_regresion.pkl','rb'))
lb=pickle.load(open('label_encoder.pkl','rb'))
tfidf_vectorizer=pickle.load(open('tfidf_vectorizer.pkl','rb'))



#app===============
st.title("Emotions Detection App")