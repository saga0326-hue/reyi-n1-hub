# --- 1. 條碼冊卡片區域 ---
with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📦</div>
            <div class="card-title">條碼冊 APP</div>
            <p class="card-text">即時查詢、更新商品條碼資訊</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 修改這裡：路徑改成改名後的樣子
    if st.button(" ", key="btn_barcode"):
        st.switch_page("pages/barcode_app.py")

# --- 2. 北一課資訊區域 ---
with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="card-title">北一課資訊</div>
            <p class="card-text">人員名單、會議記錄</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 修改這裡
    if st.button("  ", key="btn_info"):
        st.switch_page("pages/info_app.py")
