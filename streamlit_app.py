import streamlit as st

# 1. 網頁基礎設定
st.set_page_config(
    page_title="RIYI N1 Hub", 
    page_icon="🏢", 
    layout="centered" # 導覽頁使用置中佈局較美觀
)

# 2. 企業視覺美化 (CSS)
st.markdown("""
    <style>
    /* 標題與副標題樣式 */
    .main-title {
        color: #0056b3;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-title {
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* 讓按鈕變大、變華麗 */
    div.stButton > button {
        width: 100%;
        height: 120px;
        border-radius: 15px;
        border: 1px solid #dee2e6;
        background-color: white;
        transition: all 0.3s ease;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        border-color: #0056b3;
        color: #0056b3;
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 頁面標題
st.markdown('<p class="main-title">🏢 RIYI N1 HUB</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">日翊北一課 · 數位行政中心</p>', unsafe_allow_html=True)

st.divider()

# 4. 官方推薦的跳轉按鈕區域
# 我們使用 columns 建立三格網格
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📦")
    if st.button("條碼冊\nAPP", key="nav_barcode"):
        st.switch_page("pages/1_📦_條碼冊APP.py")

with col2:
    st.markdown("### 📊")
    if st.button("北一課\n資訊", key="nav_info"):
        st.switch_page("pages/2_📊_北一課資訊.py")

with col3:
    st.markdown("### 📅")
    if st.button("特休\nAPP", key="nav_leave"):
        # 如果你還沒做這頁，可以先導向資訊頁或給個提示
        st.switch_page("pages/2_📊_北一課資訊.py") 

# 5. 底部資訊
st.write("")
st.write("")
st.info("💡 **小撇步**：點擊上方大按鈕可快速進入系統，或使用左側邊欄進行切換。")

st.markdown("""
    <p style="text-align:center; color:#999; font-size:0.8rem; margin-top:50px;">
        © 2026 Re-Yi Distribution Service Co., Ltd.
    </p>
""", unsafe_allow_html=True)
