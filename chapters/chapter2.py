import streamlit as st
from dialogue import choose_dialogue


def show_chapter2_dialogue(location, speaker, words):
    # 챕터 1과 같은 화면 크기 및 배치
    st.caption("CHAPTER 02")
    st.title("다섯 명의 증언")

    with st.container(border=True):
        # 향후 배경과 캐릭터 이미지를 넣을 자리
        with st.container(height=280, border=False):
            st.caption(location)
            st.caption("배경 및 캐릭터 이미지 영역")

        # 고정된 위치에 현재 대사 하나만 출력
        with st.container(height=140, border=True):
            st.markdown("**" + speaker + "**")
            st.write(words)


def show_chapter2():
    # 기존 진행 상태 변수 유지
    if "chapter2_line" not in st.session_state:
        st.session_state["chapter2_line"] = 0

    if "chapter2_scene2_step" not in st.session_state:
        st.session_state["chapter2_scene2_step"] = 0

    # 선택한 탐정의 대사를 한 화면에 보여 주기 위한 변수
    if "chapter2_selected_reply" not in st.session_state:
        st.session_state["chapter2_selected_reply"] = None

    # SCENE 01 · 면담실 (화자와 대사를 구분)
    scene1 = [
        ("나레이션", "복도를 따라 걸어가자 작은 면담실이 나타났다."),
        ("나레이션", "문을 열자 낡은 책상 하나와 마주 보는 의자 두 개가 눈에 들어왔다."),
        ("나레이션", "책상 위에는 학교에서 전달받은 사건 기록과 다섯 명의 학생 명단이 놓여 있었다."),
        ("나레이션", "지현, 혜린, 예주, 유주, 다인.\n\n모두 이번 사건의 조사 대상자들이었다."),
        ("나레이션", "나는 명단을 다시 한번 살펴보았다.\n\n*'다섯 명의 말이 모두 사실일까.'*"),
        ("나레이션", "그때 문밖에서 가벼운 노크 소리가 들렸다.\n\n**똑, 똑.**"),
        ("나", '"들어오세요."'),
        ("나레이션", "문이 열리고 한 여학생이 조심스럽게 안으로 들어왔다."),
        ("지현", '"안녕하세요. 지현이라고 합니다."'),
    ]

    # SCENE 02 · 첫 번째 면담 (선택형 대화)
    scene2 = [
        {
            "speaker": "나레이션",
            "text": "지현은 조금 긴장한 표정으로 의자에 앉았다.",
            "choice": "시간 내주셔서 감사합니다. 몇 가지 확인할 사항이 있어서요.",
        },
        {
            "speaker": "지현",
            "text": '"네. 그런데 제가 정말 의심받고 있는 건가요?"',
            "choice": "아직 누구도 범인이라고 단정하지 않았습니다. 사건 당일 무슨 일이 있었는지 확인하려는 겁니다.",
        },
        {
            "speaker": "나레이션",
            "text": "지현은 잠시 망설이다가 고개를 끄덕였다.",
            "choice": None,
        },
        {
            "speaker": "지현",
            "text": '"알겠어요. 무엇부터 말씀드리면 될까요?"',
            "choice": None,
        },
    ]

    location = "학교 본관 · 면담실"
    line = st.session_state["chapter2_line"]

    # SCENE 01 · 대사가 아래에 누적되지 않도록 하나만 출력
    if line < len(scene1):
        speaker, words = scene1[line]
        show_chapter2_dialogue(location, speaker, words)

        button_text = "면담 시작 ▶" if line == len(scene1) - 1 else "다음 ▶"
        if st.button(button_text, key="chapter2_next", use_container_width=True):
            st.session_state["chapter2_line"] += 1
            st.rerun()
        return

    # SCENE 02 · 선택한 탐정의 답변을 별도 화면에 표시
    reply = st.session_state["chapter2_selected_reply"]
    if reply is not None:
        show_chapter2_dialogue(location, "나", reply)
        if st.button("다음 ▶", key="chapter2_reply_next", use_container_width=True):
            st.session_state["chapter2_selected_reply"] = None
            st.session_state["chapter2_scene2_step"] += 1
            st.rerun()
        return

    step = st.session_state["chapter2_scene2_step"]
    if step >= len(scene2):
        st.info("현재 작성된 챕터 2 스토리는 여기까지입니다.")
        return

    current = scene2[step]
    show_chapter2_dialogue(location, current["speaker"], current["text"])

    if current["choice"] is not None:
        # choose_dialogue()는 대사 문자열이 아니라 선택한 보기의 번호를 반환함
        options = [current["choice"]]
        selected = choose_dialogue(
            options,
            "chapter2_choice_" + str(step),
        )
        if selected is not None:
            st.session_state["chapter2_selected_reply"] = options[selected]
            st.rerun()
    elif step < len(scene2) - 1:
        if st.button("다음 ▶", key="chapter2_scene2_next", use_container_width=True):
            st.session_state["chapter2_scene2_step"] += 1
            st.rerun()
    else:
        st.caption("이후 장면은 아직 작성되지 않았습니다.")
