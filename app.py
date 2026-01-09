import streamlit as st
import random

st.title(" 2分の1を当て続けろ！")

# ボタンを大きくする
st.markdown("""
<style>
div.stButton > button {
    width: 600%;
    height: 150px;
    font-size: 40px;
}
</style>
""", unsafe_allow_html=True)

# 初期化
if "win_streak" not in st.session_state:
    st.session_state.win_streak = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "choice" not in st.session_state:
    st.session_state.choice = None

st.write("右 か 左 のどちらかを選んでください")

if not st.session_state.game_over:
    col1, col2 = st.columns(2)

    if col1.button("左"):
        st.session_state.choice = 0
    if col2.button("右"):
        st.session_state.choice = 1

    if st.session_state.choice is not None:
        answer = random.randint(0, 1)

        if st.session_state.choice == answer:
            st.session_state.win_streak += 1
            st.success("正解！🎉")
        else:
            st.error("不正解…💀")
            st.session_state.game_over = True

        # 次の入力に備えてリセット
        st.session_state.choice = None

# 結果表示
win = st.session_state.win_streak
st.write(f"現在の連勝数：{win}")

probability = (1 / 2) ** win
prob_percent = probability * 100
st.write(f" ここまで当て続けている確率：**{prob_percent:.4f}%**")

# リスタート
if st.session_state.game_over:
    if st.button("もう一度遊ぶ"):
        st.session_state.win_streak = 0
        st.session_state.game_over = False
        st.session_state.choice = None










