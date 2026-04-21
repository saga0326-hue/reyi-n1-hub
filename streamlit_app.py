import streamlit as st

# 設定網頁標籤與佈局
st.set_page_config(page_title="RIYI N1 Hub", page_icon="🏢", layout="wide")

# --- 日翊企業風格 CSS 注入 ---
st.markdown("""
    <style>
    /* 1. 全局背景：淺灰色調與頂部藍色裝飾 */
    .main {
        background-color: #f8f9fa;
        background-image: linear-gradient(180deg, #e9ecef 0%, #f8f9fa 100%);
    }

    /* 2. 標題區：使用日翊藍 (#1a73e8 類似色) */
    .header-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border-bottom: 5px solid #0056b3; /* 底部藍色粗線 */
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #0056b3; /* 企業藍 */
        margin: 0;
    }

    /* 3. 卡片設計：玻璃擬態與企業風格 */
    .stMarkdown div[data-testid="stVerticalBlock"] > div:has(div.feature-card) {
        gap: 0rem;
    }

    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #dee2e6;
        text-align: center;
        transition: all 0.3s ease;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.1);
        border-color: #0056b3;
    }

    .icon {
        font-size: 4rem;
        margin-bottom: 15px;
    }

    .card-title {
        color: #333;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .card-text {
        color: #666;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 頁面內容顯示 ---

# 頂部標題區
st.markdown("""
    <div class="header-container">
        <p class="main-title">🏢 RIYI N1 HUB</p>
        <p style="color:#555; font-size:1.1rem; margin-top:10px;">
            日翊文化行銷 · 北一課數位資訊入口網
        </p>
    </div>
""", unsafe_allow_html=True)

# 功能卡片區 - 三欄式佈局
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📦</div>
            <div class="card-title">條碼冊 APP</div>
            <p class="card-text">即時查詢、更新商品條碼資訊<br>支援手機掃描與快速輸入</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="card-title">北一課資訊</div>
            <p class="card-text">人員名單、會議記錄<br>與澎湖駐點人員看板</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📅</div>
            <div class="card-title">特休 APP</div>
            <p class="card-text">個人特休餘額查詢<br>與請假申請進度追蹤</p>
        </div>
    """, unsafe_allow_html=True)

# 底部導覽提示
st.markdown("<br>", unsafe_allow_html=True)
st.info("💡 **使用指南**：請點擊左側選單的 ◀ 按鈕展開選單，選擇您要進入的系統。")

# 頁尾
st.markdown("""
    <hr style="border:0.5px solid #ddd">
    <p style="text-align:center; color:#999; font-size:0.8rem;">
        © 2026 Re-Yi Distribution Service Co., Ltd. All Rights Reserved
    </p>
""", unsafe_allow_html=True)
