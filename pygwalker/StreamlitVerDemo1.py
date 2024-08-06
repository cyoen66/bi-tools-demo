import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer



#streamlit run .\StreamlitVerDemo1.py 起動コマンド
st.set_page_config(page_title='YFC 汎用分析'
                   ,layout="wide")
st.title('YFC 汎用分析')
update_file = st.file_uploader("分析用CSVファイルをアップロードしてください", type=['csv'])
#縦軸
option = st.selectbox(
    "縦軸項目を選択してください",
    ("企業", "会社部門", "年月日"),
)
#横軸
option1 = st.selectbox(
    "横軸項目を選択してください",
    ("企業", "会社部門", "年月日"),
)

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv('../MCCMBI.csv')
    return StreamlitRenderer(df,spec="./demo1.json", spec_io_mode="rw")
    #return StreamlitRenderer(df, spec_io_mode="rw")

if update_file is not None:
    renderer  = get_pyg_renderer()
    renderer.explorer()