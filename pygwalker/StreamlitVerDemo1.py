import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import logging


logging.basicConfig(level=logging.INFO)

#streamlit run .\StreamlitVerDemo1.py 起動コマンド
st.set_page_config(page_title='YFC 汎用分析'
                   ,layout="wide")
st.title('YFC 汎用分析')
update_file = st.file_uploader("分析用CSVファイルをアップロードしてください"
                               , type=['csv']
                               ,help="ファイルをアップロードしてください")
df = pd.read_csv('../MCCMBI.csv')

# 显示下载按钮
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="テスト用ファイルをダウンロード",
    data=csv,
    file_name='MCCMBI.csv',
    mime='text/csv',
)

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    #null を　０に変換
    df['売上数'] = df['売上数'].fillna(0)
    #return StreamlitRenderer(df,spec="./demo1.json", spec_io_mode="rw")
    #sepc_io_mode="r"で読み込み専用
    return StreamlitRenderer(df,spec="./demo2.json", spec_io_mode="rw")

    #return StreamlitRenderer(df, spec_io_mode="rw")


if update_file is not None:
    #タブ画面を作成する
    tab1, tab2 = st.tabs(["ユーザー表示", "編集画面"])
    renderer  = get_pyg_renderer()
    #編集可能のモード
    with tab1:
        renderer.viewer(scrolling=True,width=1500);
    with tab2:
        renderer.explorer();


