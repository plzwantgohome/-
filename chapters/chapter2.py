
import streamlit as st


def show_chapter2():

    if "chapter2_line" not in st.session_state:
        st.session_state["chapter2_line"] = 0

    st.caption("CHAPTER 02")
    st.title("다섯 명의 증언")
    st.divider()
    st.caption("SCENE 01 · 면담실")

    scene1 = [
        "복도를 따라 걸어가자 작은 면담실이 나타났다.",

        "문을 열자 낡은 책상 하나와 마주 보는 의자 두 개가 눈에 들어왔다.",

        "책상 위에는 학교에서 전달받은 사건 기록과 다섯 명의 학생 명단이 놓여 있었다.",

        "지현, 혜린, 예주, 유주, 다인.\n\n모두 이번 사건의 조사 대상자들이었다.",

        "나는 명단을 다시 한번 살펴보았다.\n\n*'다섯 명의 말이 모두 사실일까.'*",

        "그때 문밖에서 가벼운 노크 소리가 들렸다.\n\n**똑, 똑.**",

        '"들어오세요."\n\n문이 열리고 한 여학생이 조심스럽게 안으로 들어왔다.',

        '"안녕하세요. 지현이라고 합니다."'
    ]

    for i in range(st.session_state["chapter2_line"] + 1):
        st.markdown(scene1[i])

    if st.session_state["chapter2_line"] < len(scene1) - 1:
        if st.button("다음 ▶", key="chapter2_next"):
            st.session_state["chapter2_line"] += 1
            st.rerun()
