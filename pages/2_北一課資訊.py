import streamlit as st
import pandas as pd

st.set_page_config(page_title="北一課資訊", page_icon="📋")

@st.cache_data(ttl=60)
def load_data(url):
    try:
        # 讀取 CSV
        return pd.read_csv(url)
    except:
        return None

# 從 Secrets 讀取不同的分頁網址
# 你需要在 Streamlit Secrets 增加這些網址
staff_list_url = st.secrets.get("staff_list_url", "")
meeting_log_url = st.secrets.get("meeting_log_url", "")
penghu_staff_url = st.secrets.get("penghu_staff_url", "")

st.title("📋 北一課 資訊查詢中心")

# 使用標籤頁 (Tabs) 分類
tab1, tab2, tab3 = st.tabs(["👥 人員名單", "📝 會議記錄", "🌊 澎湖人員"])

with tab1:
    st.subheader("人員名單")
    if staff_list_url:
        df = load_data(staff_list_url)
        if df is not None:
            st.dataframe(df, use_container_width=True)
        else: st.error("讀取失敗，請檢查 CSV 網址")
    else: st.info("請在 Secrets 設定 staff_list_url")
        
# 在人員名單分頁中加入這個
col1, col2 = st.columns(2)
col1.metric(label="北一課總人數", value="45 人", delta="▲ 2")
col2.metric(label="澎湖駐點人數", value="3 人", delta="持平")

with tab2:
    st.subheader("近期會議記錄")
    if meeting_log_url:
        df = load_data(meeting_log_url)
        if df is not None:
            st.table(df) # 會議記錄用 table 顯示比較清楚
        else: st.error("讀取失敗")
    else: st.info("請在 Secrets 設定 meeting_log_url")

with tab3:
    st.subheader("澎湖駐點人員")
    if penghu_staff_url:
        df = load_data(penghu_staff_url)
        if df is not None:
            st.dataframe(df, use_container_width=True)
        else: st.error("讀取失敗")
    else: st.info("請在 Secrets 設定 penghu_staff_url")
