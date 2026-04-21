import streamlit as st

# 1. 基礎設定
st.set_page_config(page_title="RIYI N1 Hub", page_icon="🏠", layout="wide")

# 2. 注入華麗 CSS (與剛才一致)
st.markdown("""
    <style>
    .header-container {
        background: white; padding: 2rem; border-radius: 15px;
        border-bottom: 5px solid #0056b3; text-align: center; margin-bottom: 2rem;
    }
    .feature-card {
        background: white; padding: 40px 20px; border-radius: 20px;
        border: 1px solid #dee2e6; text-align: center; min-height: 280px;
        display: flex; flex-direction: column; justify-content: center;
        position: relative;
    }
    .stButton > button {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: transparent !important; color: transparent !important;
        border: none !important; z-index: 10; cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 標題
st.markdown('<div class="header-container"><h1 style="color:#0056b3;">🏢 RIYI N1 HUB</h1><p>日翊北一課 · 數位行政管理入口</p></div>', unsafe_allow_html=True)

# 4. 關鍵位置：定義欄位 (注意這裡是 col1, col2, col3，不是 coll)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card"><h1>📦</h1><h3>條碼冊 APP</h3><p>查詢與更新商品條碼</p></div>', unsafe_allow_html=True)
    # 確保路徑與你 GitHub pages 資料夾下的檔名一致
    if st.button("goto1", key="b1"):
        st.switch_page("pages/barcode_app.py")

with col2:
    st.markdown('<div class="feature-card"><h1>📊</h1><h3>北一課資訊</h3><p>人員名單與會議記錄</p></div>', unsafe_allow_html=True)
    if st.button("goto2", key="b2"):
        st.switch_page("pages/info_app.py")

with col3:
    st.markdown('<div class="feature-card"><h1>📅</h1><h3>特休 APP</h3><p>查詢特休餘額(開發中)</p></div>', unsafe_allow_html=True)
    if st.button("goto3", key="b3"):
        st.info("系統開發中，敬請期待")
