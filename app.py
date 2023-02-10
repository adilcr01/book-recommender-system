import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import NearestNeighbors

book_pivot = pickle.load(open('book_pivot.pkl','rb'))

model = pickle.load(open('model.pkl','rb'))
book_name = pd.read_csv('book_name.csv')
book_list=book_name['title'].values

book_image = pickle.load(open('book_image.pkl','rb'))

def get_ISBN(book_name):
    ISBN=[]
    for i in book_name:
        ISBN.append(book_image['ISBN'][book_image['Book-Title'] == i][0:1].values[0])
    return ISBN

def fetch_image(book_name):
    link=[]
    for i in get_ISBN(book_name):
        link.append(book_image['Image-URL-M'][book_image['ISBN'] == i][0:1].values[0])
    return link


def suggest(book_name):
    recommend_book_list = []
    recommend_book_poster = []
    book_index=np.where(book_pivot.index == book_name)[0][0]
    distances,suggestion = model.kneighbors(book_pivot.iloc[book_index, :].values.reshape(1, -1), n_neighbors=6)
    for i in range(len(suggestion)):
        recommend_book_list.append(book_pivot.index[suggestion[i]].values[1:6])
        recommend_book_poster.append(fetch_image(book_pivot.index[suggestion[i]].values[1:6]))
    return recommend_book_list,recommend_book_poster



st.title('Book Recommeder System')
selected_book_name=st.selectbox(
 'Enter your Favourite Book',
 (book_list))

if st.button('Recommend'): # Create a button name recommend
    names,poster=suggest(selected_book_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0][0])
        st.image(poster[0][0])

    with col2:
        st.header(names[0][1])
        st.image(poster[0][1])

    with col3:
        st.header(names[0][2])
        st.image(poster[0][2])
    with col4:
        st.header(names[0][3])
        st.image(poster[0][3])

    with col5:
        st.header(names[0][4])
        st.image(poster[0][4])
