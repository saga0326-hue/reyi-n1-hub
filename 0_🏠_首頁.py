import streamlit as st

# 1. 網頁基礎設定
st.set_page_config(
    page_title="RIYI N1 Hub", 
    page_icon="🏢", 
    layout="wide" # 導覽頁使用寬螢幕佈局
)

# 2. 華麗企業風格 CSS 注入 (日翊藍 #0056b3)
st.markdown("""
    <style>
    /* 全局背景 */
    .main { background-color: #f8f9fa; }

    /* 標題區 */
    .header-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border-bottom: 5px solid #0056b3;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0056b3;
        margin: 0;
    }

    /* 3. 華麗卡片設計 (純外觀) */
    .feature-card {
        background: white;
        padding: 40px 20px;
        border-radius: 20px;
        border: 1px solid #dee2e6;
        text-align: center;
        transition: all 0.3s ease;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        position: relative; /* 為了讓按鈕疊在上面 */
        z-index: 1;
    }

    .icon { font-size: 5rem; margin-bottom: 15px; }
    .card-title { color: #333; font-size: 1.8rem; font-weight: 700; margin-bottom: 10px; }
    .card-text { color: #666; line-height: 1.6; font-size: 1rem; }

    /* 4. 讓卡片在滑鼠移上去時浮起 (視覺效果) */
    .stMarkdown:has(div.feature-card):hover {
        transform: translateY(-10px);
    }

    /* 5. 把 Streamlit 的按鈕變透明並蓋住整張卡片 */
    .stButton > button {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: transparent !important; /* 透明背景 */
        color: transparent !important; /* 透明文字 */
        border: none !important;
        box-shadow: none !important;
        z-index: 10; /* 確保按鈕在最上層 */
        cursor: pointer;
    }
    
    /* 去除按鈕點擊時的藍色外框 */
    .stButton > button:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 頁面內容顯示 ---

# 頂部標題區
st.markdown("""
    <div class="header-container">
        <p class="main-title">🏢 RIYI N1 HUB</p>
        <p style="color:#555; font-size:1.2rem; margin-top:10px;">
            日翊文化行銷 · 北一課數位資訊入口網
        </p>
    </div>
""", unsafe_allow_html=True)

# 功能卡片區 - 三欄式佈局
col1, col2, col3 = st.columns(3)

# 📦 條碼冊 APP
with col1:
    # 這是華麗的卡片外觀
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📦</div>
            <div class="card-title">條碼冊 APP</div>
            <p class="card-text">即時查詢、更新商品條碼資訊<br>支援手機掃描與快速輸入</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 這是蓋在上面的透明按鈕 (負責官方跳轉)
    # ⚠️ 這裡的路徑必須跟你的 GitHub 檔案路徑完全一致！
    if st.button("goto_barcode", key="btn_barcode"):
        st.switch_page("pages/1_📦_條碼冊APP.py")

# 📊 北一課資訊
with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="card-title">北一課資訊</div>
            <p class="card-text">人員名單、會議記錄<br>與澎湖駐點人員看板</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("goto_info", key="btn_info"):
        # 你可以先導向條碼頁，或者你可以建立一個 pages/2_📊_北一課資訊.py
        st.switch_page("pages/1_📦_條碼冊APP.py")

# 📅 特休 APP (預留)
with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📅</div>
            <div class="card-title">特休 APP</div>
            <p class="card-text">個人特休餘額查詢<br>與請假申請進度追蹤</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("goto_leave", key="btn_leave"):
        st.warning("🚧 特休系統正在開發中...")
