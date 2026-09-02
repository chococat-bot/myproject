import streamlit as st
import pandas as pd

st.title("Hotel Booking Analysis")

# 建立資料
data = {
    "Lead Time": ["0–7 天", "8–30 天", "31–90 天", "91+ 天"],
    "City Hotel": [12.20, 30.91, 39.91, 55.74],
    "Resort Hotel": [6.52, 21.90, 32.45, 39.44]
}

# 把資料轉成 DataFrame
df = pd.DataFrame(data)

# 顯示表格
st.header("Cancellation Rate by Lead Time")

st.dataframe(
    df,
    hide_index=True
)

# 顯示長條圖
st.header("Cancellation Rate Comparison")

st.bar_chart(
    df,
    x="Lead Time",
    y=["City Hotel", "Resort Hotel"]
)

st.header("Market Segment")
st.image("./image/Cancel_Market_Segment.png", caption="Market Segment")