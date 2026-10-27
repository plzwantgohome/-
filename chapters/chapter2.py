
import streamlit as st


def show_chapter2():

    if "chapter2_line" not in st.session_state:
        st.session_state["chapter2_line"] = 0

    if "chapter2_scene2_step" not in st.session_state:
        st.session_state["chapter2_scene2_step"] = 0

    st.caption("CHAPTER 02")
    st.title("다섯 명의 증언")
    st.divider()
        # 챕터 2 선택지 버튼 크기 조절
        # 챕터 2 선택지 버튼 크기 조절
    st.html("""
    <style>
    div[class*="st-key-chapter2_choice_"] button {
        width: fit-content !important;
        max-width: min(720px, 100%) !important;
        height: auto !important;
        min-height: 55px !important;
        padding: 12px 20px !important;
        letter-spacing: 1px !important;
        line-height: 1.6 !important;
        white-space: normal !important;
        overflow-wrap: anywhere !important;
    }
    </style>
    """)

    # SCENE 01 · 면담실
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

    # SCENE 02 · 첫 번째 면담
    scene2 = [
        {
            "text": "지현은 조금 긴장한 표정으로 의자에 앉았다.",
            "choice": "시간 내주셔서 감사합니다. 몇 가지 확인할 사항이 있어서요."
        },

        {
            "text": '**지현:** "네. 그런데 제가 정말 의심받고 있는 건가요?"',
            "choice": "아직 누구도 범인이라고 단정하지 않았습니다. 사건 당일 무슨 일이 있었는지 확인하려는 겁니다."
        },

        {
            "text": '지현은 잠시 망설이다가 고개를 끄덕였다.\n\n**지현:** "알겠어요. 무엇부터 말씀드리면 될까요?"',
            "choice": None
        }
    ]

    line = st.session_state["chapter2_line"]

    # SCENE 01 진행
    if line < len(scene1):

        for i in range(line + 1):
            st.markdown(scene1[i])

        if line == len(scene1) - 1:
            if st.button("면담 시작 ▶"):
                st.session_state["chapter2_line"] += 1
                st.rerun()

        else:
            if st.button("다음 ▶"):
                st.session_state["chapter2_line"] += 1
                st.rerun()

    # SCENE 02 진행
    else:

        step = st.session_state["chapter2_scene2_step"]

        for i in range(step + 1):
            st.markdown(scene2[i]["text"])

            if i < step:
                st.markdown(
                    '**탐정:** "' + scene2[i]["choice"] + '"'
                )

        if step < len(scene2) - 1:

            if st.button(
                scene2[step]["choice"],
                key="chapter2_choice_" + str(step)
            ):
                st.session_state["chapter2_scene2_step"] += 1
                st.rerun()
