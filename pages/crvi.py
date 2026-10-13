from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kalkulator Cr(VI)", layout="wide")

html = (Path(__file__).parent.parent / "crvi.html").read_text(encoding="utf-8")
components.html(html, height=2400, scrolling=True)
