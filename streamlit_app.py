import streamlit as st
import pandas as pd
from data_manager import MovieDatabase
from filters import *


# Configure page
st.set_page_config(page_title="Movie Database", page_icon="🎬", layout="wide")

 
# Initialize database
@st.cache_resource
def load_database():
    return MovieDatabase("data/movies_shows.xlsx")

db = load_database()
 
# Title
st.title("🎬 Movie & TV Show Database")
 
# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose an option:", [
    "View All Entries",
    "Filter by Class",
    "Filter by Genre",
    "Search by Name",
    "Add New Entry"
])
 
# Helper function to display data
def display_data(df, title):
    if df.empty:
        st.warning("No results found!")
        return
   
    st.subheader(title)
    st.dataframe(df, use_container_width=True)
    st.info(f"Found {len(df)} results")
 
# Page content
if page == "View All Entries":
    display_data(db.get_all_data(), "All Entries")
 
elif page == "Filter by Class":
    class_type = st.selectbox("Select type:", ["Movie", "TV Show"])
    result = filter_by_class(db.get_all_data(), class_type)
    display_data(result, f"{class_type} Results")
 
elif page == "Filter by Genre":
    genre = st.text_input("Enter genre:")
    if genre:
        result = filter_by_genre(db.get_all_data(), genre)
        display_data(result, f"{genre} Results")
 
elif page == "Search by Name":
    name = st.text_input("Enter name:")
    if name:
        result = search_by_name(db.get_all_data(), name)
        display_data(result, f"Search: {name}")
 
elif page == "Add New Entry":
    st.subheader("Add New Entry")
   
    with st.form("add_entry"):
        name = st.text_input("Name:")
        class_type = st.selectbox("Class:", ["Movie", "TV Show"])
        genre = st.text_input("Genre:")
        length = st.text_input("Length:")
        status = st.selectbox("Status:", ["To Watch", "Watching", "Watched", "Completed"])
        rating = st.number_input("Rating:", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
       
        if st.form_submit_button("Add Entry"):
            if name:
                db.add_entry(name, class_type, genre, length, status, rating)
                db.save_data("data/movies_shows.xlsx")
                st.success(f"Added '{name}' to database!")
                st.rerun()