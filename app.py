import streamlit as st
import requests

def main():
    st.set_page_config(
        page_title="即時案件",
        page_icon=":clipboard:",
        layout="wide"
    )
    
    url = "https://gis.fdkc.gov.tw/rescue/getnowcase/json?getalls=1"
    headers = {
        'Referer': 'https://gis.fdkc.gov.tw/rescue/'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        st.write('請求資料失敗')
        return
    json_data = response.json()
    
    st.table(json_data)  # 使用Streamlit的table函数显示JSON数据

if __name__ == "__main__":
    main()