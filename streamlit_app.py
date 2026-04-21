import streamlit as st

st.set_page_config(page_title="RIYI N1 Hub", page_icon="🏢", layout="wide")

# --- 華麗 CSS 樣式注入 ---
st.markdown("""
    <style>
    /* 整體背景漸層 */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* 標題美化 */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* 卡片設計 */
    .feature-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.9);
    }
    
    .icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 頁面內容 ---
st.markdown('<p class="main-title">🏢 RIYI N1 HUB</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666;">日翊北一課 · 數位行政管理系統</p>', unsafe_allow_html=True)

st.write("---")

# 建立三欄式華麗卡片
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📦</div>
            <h3>條碼冊 APP</h3>
            <p>即時查詢、更新商品條碼資訊，支援手機掃描模式。</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📊</div>
            <h3>北一課資訊</h3>
            <p>人員名單、會議記錄與澎湖駐點即時資訊看板。</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📅</div>
            <h3>特休 APP</h3>
            <p>個人特休餘額查詢與請假進度追蹤系統。</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.info("💡 提示：請使用左側導覽列進入各項功能。")
