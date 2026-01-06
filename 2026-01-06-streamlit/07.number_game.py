import streamlit as st
import random
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎯")

st.title("🎯 숫자 맞추기 게임")
st.write("1부터 N까지의 숫자 중 컴퓨터가 고른 숫자를 맞춰보세요.")

# 사이드바: 게임 설정
max_val = st.sidebar.slider("최대 숫자 (N)", min_value=10, max_value=1000, value=100, step=10)
show_hints = st.sidebar.checkbox("힌트 표시(더 큽니다/더 작습니다)", value=True)

# 세션 상태 초기화 또는 범위 변경 시 재시작
if 'target' not in st.session_state or st.session_state.get('max_val') != max_val:
    st.session_state.target = random.randint(1, max_val)
    st.session_state.guesses = []
    st.session_state.attempts = 0
    st.session_state.won = False
    st.session_state.max_val = max_val

col1, col2 = st.columns([3,1])
with col1:
    guess = st.number_input("예상 숫자 입력", min_value=1, max_value=max_val, value=1, step=1)
with col2:
    submit = st.button("추측하기")

if submit and not st.session_state.won:
    st.session_state.attempts += 1
    st.session_state.guesses.append({'guess': int(guess), 'time': datetime.now()})

    if guess < st.session_state.target:
        if show_hints:
            st.info('더 큽니다')
        else:
            st.info('틀렸습니다')
    elif guess > st.session_state.target:
        if show_hints:
            st.warning('더 작습니다')
        else:
            st.info('틀렸습니다')
    else:
        st.success(f'정답입니다! 🎉 {st.session_state.attempts}번 만에 맞추셨습니다.')
        st.balloons()
        st.session_state.won = True

st.write('---')

# 게임 상태와 기록 표시
st.write(f"시도: {st.session_state.attempts} | 범위: 1 - {max_val}")

if st.session_state.guesses:
    df = pd.DataFrame(st.session_state.guesses)
    df['time'] = df['time'].dt.strftime('%H:%M:%S')
    df.index += 1
    st.table(df.rename(columns={'guess': '예측값', 'time': '시간'}))

col3, col4 = st.columns(2)
with col3:
    if st.button('다시 시작'):
        st.session_state.target = random.randint(1, max_val)
        st.session_state.guesses = []
        st.session_state.attempts = 0
        st.session_state.won = False
with col4:
    if st.button('정답 공개'):
        st.info(f"정답은 {st.session_state.target} 입니다")