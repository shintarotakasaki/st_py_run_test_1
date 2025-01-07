# -*- coding: utf-8 -*-
"""gitpy_run_test

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LfC5ZXCuoVLvzqDIYMI2nflSI9yFaRq7
"""

from openpyxl import load_workbook
from io import BytesIO
import subprocess
import os
import sys
import importlib

import streamlit as st

# GitHub リポジトリのクローン
REPO_NAME = 'st_py_run_test_1'
REPO_URL = 'https://github.com/shintarotakasaki/st_py_run_test_1.git'

if not os.path.exists(REPO_URL):
    subprocess.run(['git', 'clone', REPO_URL])

# モジュールパスを追加
sys.path.append(REPO_NAME)

# 必要なモジュールを事前にインポート
try:
    xl_des = importlib.import_module('xl_des')
    pdf_des = importlib.import_module('pdf_des')
except ImportError as e:
    st.error(f"モジュールのインポートに失敗しました: {e}")
    st.stop()

st.title("Streamlitでレポジトリ内のpyを実行")

# ファイルアップローダー
uploaded_file = st.file_uploader("ファイルをアップロードしてください")

if uploaded_file is not None:
    file_mime = uploaded_file.type

    if file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        file = BytesIO(uploaded_file.getvalue())
        wb = load_workbook(filename=file)
        sheet = wb.active
        st.write(f"シートタイトル: {sheet.title}")
        
        # xl_des モジュールの関数を実行
        if hasattr(xl_des, 'main'):
            xl_des.main(sheet)
        else:
            st.warning("xl_des モジュールに 'main' 関数が見つかりません。")

    elif file_mime == 'application/pdf':
        st.write("PDFをアップロードしました")
        
        # pdf_des モジュールの関数を実行
        if hasattr(pdf_des, 'main'):
            pdf_des.main(uploaded_file)
        else:
            st.warning("pdf_des モジュールに 'main' 関数が見つかりません。")

    else:
        st.write("エクセルファイル(.xlsx)またはPDFファイルをアップロードしてください")
