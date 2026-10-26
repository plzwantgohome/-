
import streamlit as st


def show_chapter2():

    st.caption("CHAPTER 02")
    st.title("다섯 명의 증언")
    st.divider()

    with st.container(border=True):
        st.markdown(
            "교장실을 나온 나는 복도를 바라보았다.\n\n"
            "이제 사건과 관련된 다섯 명의 학생을 "
            "직접 만나볼 차례였다."
        )
