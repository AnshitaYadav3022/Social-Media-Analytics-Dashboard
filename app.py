
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Social Media Analytics Dashboard", layout="wide")

st.title("📊 Social Media Analytics Dashboard")

uploaded_file = st.file_uploader("Upload your social media data CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Basic Information")
    st.write(df.head())

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    with st.expander("📈 Engagement Over Time"):
        if 'Likes' in df.columns and 'Date' in df.columns:
            likes_by_date = df.groupby(df['Date'].dt.date)['Likes'].sum()
            st.line_chart(likes_by_date)

    with st.expander("🔥 Top Posts"):
        if 'Likes' in df.columns and 'Caption' in df.columns:
            top_posts = df.sort_values(by='Likes', ascending=False).head(5)
            st.write(top_posts[['Caption', 'Likes']])
