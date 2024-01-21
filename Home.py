import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Integer auctor at nisl et interdum. Nullam pulvinar massa tellus, sed ornare 
tellus sodales at. Suspendisse at sapien eu tellus egestas egestas in id mi. 
In purus sem, fringilla vitae nibh eget, placerat euismod odio. Vivamus a 
rhoncus erat. Mauris a posuere ligula. Vivamus hendrerit rhoncus congue. 
Suspendisse quis purus laoreet, sodales augue ac, pharetra enim.
""")

st.header("Our Team")

df = pandas.read_csv("./data.csv", sep=",")
number_of_items_in_one_column = len(df) // 3

col1, col2, col3 = st.columns(3)


def draw_employee(first_name: str, last_name: str, role: str, image_path: str) -> None:
    st.header(first_name.capitalize() + ' ' + last_name.capitalize())
    st.write(role.capitalize())
    st.image(image_path)


for index, row in df[:number_of_items_in_one_column].iterrows():
    with col1:
        draw_employee(row['first name'], row['last name'], row['role'], f'./images/{row["image"]}')

for index, row in df[number_of_items_in_one_column:number_of_items_in_one_column * 2].iterrows():
    with col2:
        draw_employee(row['first name'], row['last name'], row['role'], f'./images/{row["image"]}')

for index, row in df[number_of_items_in_one_column * 2:].iterrows():
    with col3:
        draw_employee(row['first name'], row['last name'], row['role'], f'./images/{row["image"]}')
