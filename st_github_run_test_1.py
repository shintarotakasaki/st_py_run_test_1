# -*- coding: utf-8 -*-
"""st_github_run_test_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N6-V8VDLuOWmmiskMwEZHNXE4nSHyptL
"""

import subprocess
import os
import sys

if not os.path.exists('st_py_run_test_1'):
    subprocess.run(['git','clone','https://github.com/shintarotakasaki/st_py_run_test_1.git'])

sys.path.append('st_py_run_test_1')

import st_run

def main():
    import streamlit as st
    st.title("Streamlitでレポジトリ内のpyを実行")
    import st_run
    
if __name__ == "__main__":
    main()
