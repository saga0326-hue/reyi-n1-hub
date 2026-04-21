import streamlit as st

st.set_page_config(page_title="日翊北一課 N1 Hub", page_icon="🏢")

st.title("🚀 日翊北一課 - 數位行政中心")
st.markdown("請從左側選單選擇您要使用的功能：")

col1, col2 = st.columns(2)
with col1:
    st.info("📦 **條碼冊 APP**\n\n快速查詢商品條碼、新增商品資訊。")
with col2:
    st.success("🏖️ **特休 APP**\n\n查詢個人特休餘額與申請進度。")

st.divider()
st.subheader("📢 北一課最新資訊")
st.write("1. 4月份排班表已更新\n2. 倉庫整理標準流程說明")
