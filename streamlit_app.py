import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ecoログ", layout="centered")
st.title("🌱 Ecoログ：節電・節水可視化アプリ")

st.write("日常の使用量を入力してください")

# --- 入力 ---
ac_time = st.slider("エアコン使用時間（時間）", 0.0, 24.0, 2.0, 0.5)
light_time = st.slider("照明使用時間（時間）", 0.0, 24.0, 5.0, 0.5)
shower_time = st.slider("シャワー使用時間（分）", 0, 60, 10)

# --- 換算 ---
ac_kwh = ac_time * 1.0
light_kwh = light_time * 0.05
total_kwh = ac_kwh + light_kwh

water_l = shower_time * 12

# --- 結果表示 ---
st.subheader("📊 今日の使用量")

st.metric("電力使用量 (kWh)", f"{total_kwh:.2f}")
st.metric("水使用量 (L)", f"{water_l}")

# --- グラフ用データ ---
df = pd.DataFrame({
    "項目": ["エアコン", "照明"],
    "消費電力(kWh)": [ac_kwh, light_kwh]
})

st.subheader("🔍 電力内訳")
st.bar_chart(df.set_index("項目"))

# --- コメント ---
st.subheader("💡 節約アドバイス")
if shower_time > 15:
    st.warning("シャワー時間を5分短縮すると約60L節水できます！")
else:
    st.success("節水できています！その調子です👍")
