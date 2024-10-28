import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company of All Time!")

content = """
Ex velit minim aliquip excepteur cupidatat Lorem tempor et velit. Incididunt velit ut esse in. Magna ad incididunt duis qui labore nisi tempor culpa consequat tempor magna.

Anim commodo sunt irure nostrud sit incididunt non dolor irure duis et do et qui. Consectetur aute proident voluptate nulla. Fugiat laborum eu ad consectetur veniam aliquip officia aute mollit. Amet incididunt nulla exercitation commodo et culpa ad ullamco aliquip officia occaecat tempor fugiat. Qui fugiat proident aute quis laborum quis. Aliquip irure laboris ea do do occaecat. Consectetur cillum aute nulla qui dolore aliquip in velit excepteur irure consectetur.

In sit non reprehenderit cillum laborum occaecat cillum veniam fugiat laboris labore eiusmod. Ea quis dolore proident cillum voluptate sint ipsum. Est anim tempor esse dolore Lorem do minim adipisicing. Dolore pariatur sit pariatur occaecat irure id velit. Fugiat ad esse eiusmod occaecat nisi sit incididunt ad nulla tempor est. Fugiat est aliquip aliquip incididunt tempor laborum do consectetur eiusmod reprehenderit id exercitation commodo ullamco. Adipisicing commodo sunt consectetur sunt laborum.
"""
st.write(content)

st.title("Meet The Crew!")

workers = pd.read_csv("bonus/companyWebSite/datasource/data.csv")
left, mid, right = st.columns(3)

with left:
    for i, worker in workers.iterrows():
        if i % 3 == 0:
            firstName = str(worker["first name"]).title()
            lastName = str(worker["last name"]).upper()
            fullName = f"{firstName} {lastName}"
            role = worker["role"]
            img = "bonus/companyWebSite/datasource/images/" + worker["image"]
            st.subheader(fullName)
            st.text(role)
            st.image(img)

with mid:
    for i, worker in workers.iterrows():
        if (i - 1) % 3 == 0:
            firstName = str(worker["first name"]).title()
            lastName = str(worker["last name"]).upper()
            fullName = f"{firstName} {lastName}"
            role = worker["role"]
            img = "bonus/companyWebSite/datasource/images/" + worker["image"]
            st.subheader(fullName)
            st.text(role)
            st.image(img)

with right:
    for i, worker in workers.iterrows():
        if (i - 2) % 3 == 0:
            firstName = str(worker["first name"]).title()
            lastName = str(worker["last name"]).upper()
            fullName = f"{firstName} {lastName}"
            role = worker["role"]
            img = "bonus/companyWebSite/datasource/images/" + worker["image"]
            st.subheader(fullName)
            st.text(role)
            st.image(img)
