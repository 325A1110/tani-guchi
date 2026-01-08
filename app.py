import streamlit as st

import random

st.title(" 数字当てゲーム（High & Low）")

# ランダムな正解の数値をセッションに保存
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.count = 0

st.write("1〜100 の中から当たりの数字をあてろ！")

# ユーザー入力
guess = st.number_input("数字を入力", min_value=1, max_value=100, step=1)
clicked = st.button("判定！")

if clicked:
    st.session_state.count += 1

    if guess < st.session_state.answer:
        st.warning("もっと大きい数字だよ！⬆")
    elif guess > st.session_state.answer:
        st.warning("もっと小さい数字だよ！⬇")
    else:
        st.success(f"🎉 正解！ {st.session_state.count} 回目で当てた！")
        if st.button("もう一回遊ぶ"):
            st.session_state.answer = random.randint(1, 100)
            st.session_state.count = 0
            st.experimental_rerun()