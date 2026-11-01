
import streamlit as st
from dialogue import choose_dialogue
from ui import show_dialogue


def show_chapter2_scene3():
    # SCENE 03 · 지현의 진술

    if "chapter2_scene3_step" not in st.session_state:
        st.session_state["chapter2_scene3_step"] = 0

    if "chapter2_scene3_phase" not in st.session_state:
        st.session_state["chapter2_scene3_phase"] = "question"

    if "chapter2_scene3_selected" not in st.session_state:
        st.session_state["chapter2_scene3_selected"] = None

    scene3 = [
        {
            "speaker": "나",
            "text": "사건 당일, 교무실 앞 복도를 지나갔다고 들었습니다. 맞습니까?"
        },
        {
            "speaker": "지현",
            "text": "네. 야간 자율학습을 마치고 집에 가던 길이었어요."
        },
        {
            "speaker": "나",
            "text": "그때 교무실 안으로 들어간 적은 없나요?"
        },
        {
            "speaker": "지현",
            "text": "없어요. 교무실 앞을 지나가기만 했어요. 문도 닫혀 있었고요."
        },
        {
            "speaker": "나레이션",
            "text": "지현은 잠시 생각하다가 무언가 떠올랐다는 듯 말을 이었다."
        },
        {
            "speaker": "지현",
            "text": "아, 그런데 그날 복도 끝에서 프린터 소리 같은 게 들렸어요. 인쇄실 쪽이었던 것 같아요."
        },
        {
            "speaker": "나레이션",
            "text": "나는 수첩에 인쇄실이라는 단어를 적었다. 어떤 점부터 확인하는 편이 좋을까?",
            "choices": [
                {
                    "question": "그 소리는 언제쯤 들었습니까?",
                    "answer": "정확한 시각은 기억나지 않아요. 야간 자율학습을 마치고 복도를 지나갈 때였어요. 누가 인쇄하고 있었는지는 모르겠어요."
                },
                {
                    "question": "인쇄실 근처에서 누군가를 보았습니까?",
                    "answer": "사람이 있었는지는 확실치 않아요. 소리만 들었고, 누가 인쇄하고 있었는지는 보지 못했어요."
                }
            ]
        },
        {
            "speaker": "나",
            "text": "소리가 났다는 사실만으로 시험 자료와 관련 있다고 단정할 수는 없겠군요."
        },
        {
            "speaker": "지현",
            "text": "네. 저도 무슨 종이를 인쇄했는지는 전혀 몰라요."
        },
        {
            "speaker": "나레이션",
            "text": "나는 지현의 진술을 정리했다. 교무실 앞을 지나갔다는 사실, 그리고 인쇄실 쪽에서 들렸다는 소리. 아직 확인이 필요한 이야기들이었다."
        }
    ]

    step = st.session_state["chapter2_scene3_step"]
    location = "학교 본관 · 면담실"

    if step >= len(scene3):
        st.caption("지현의 첫 번째 진술 확인 완료")
        st.info("다음 장면은 아직 작성되지 않았습니다.")
        return

    current = scene3[step]
    choices = current.get("choices")

    # 일반 대사
    if choices is None:

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            current["speaker"],
            current["text"]
        )

        if st.button(
            "다음 ▶",
            key="chapter2_scene3_next",
            use_container_width=True
        ):
            st.session_state["chapter2_scene3_step"] += 1
            st.rerun()

        return

    # 선택지가 있는 장면
    phase = st.session_state["chapter2_scene3_phase"]

    if phase == "question":

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            current["speaker"],
            current["text"]
        )

        options = [
            choice["question"] for choice in choices
        ]

        selected = choose_dialogue(
            options,
            "chapter2_scene3_choice_" + str(step)
        )

        if selected is not None:
            st.session_state["chapter2_scene3_selected"] = selected
            st.session_state["chapter2_scene3_phase"] = "player"
            st.rerun()

    # 플레이어가 선택한 대사
    elif phase == "player":

        selected = st.session_state["chapter2_scene3_selected"]

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            "나",
            choices[selected]["question"]
        )

        if st.button(
            "다음 ▶",
            key="chapter2_scene3_player_next",
            use_container_width=True
        ):
            st.session_state["chapter2_scene3_phase"] = "answer"
            st.rerun()

    # 지현의 답변
    elif phase == "answer":

        selected = st.session_state["chapter2_scene3_selected"]

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            "지현",
            choices[selected]["answer"]
        )

        if st.button(
            "다음 ▶",
            key="chapter2_scene3_answer_next",
            use_container_width=True
        ):
            st.session_state["chapter2_scene3_step"] += 1
            st.session_state["chapter2_scene3_phase"] = "question"
            st.session_state["chapter2_scene3_selected"] = None
            st.rerun()


def show_chapter2():

    # 기존 진행 상태 변수
    if "chapter2_line" not in st.session_state:
        st.session_state["chapter2_line"] = 0

    if "chapter2_scene2_step" not in st.session_state:
        st.session_state["chapter2_scene2_step"] = 0

    if "chapter2_selected_reply" not in st.session_state:
        st.session_state["chapter2_selected_reply"] = None

    # SCENE 01 · 면담실
    scene1 = [
        (
            "나레이션",
            "복도를 따라 걸어가자 작은 면담실이 나타났다."
        ),
        (
            "나레이션",
            "문을 열자 낡은 책상 하나와 마주 보는 의자 두 개가 눈에 들어왔다."
        ),
        (
            "나레이션",
            "책상 위에는 학교에서 전달받은 사건 기록과 다섯 명의 학생 명단이 놓여 있었다."
        ),
        (
            "나레이션",
            "지현, 혜린, 예주, 유주, 다인.\n\n모두 이번 사건의 조사 대상자들이었다."
        ),
        (
            "나레이션",
            "나는 명단을 다시 한번 살펴보았다.\n\n*'다섯 명의 말이 모두 사실일까.'*"
        ),
        (
            "나레이션",
            "그때 문밖에서 가벼운 노크 소리가 들렸다.\n\n**똑, 똑.**"
        ),
        (
            "나",
            '"들어오세요."'
        ),
        (
            "나레이션",
            "문이 열리고 한 여학생이 조심스럽게 안으로 들어왔다."
        ),
        (
            "지현",
            '"안녕하세요. 지현이라고 합니다."'
        )
    ]

    # SCENE 02 · 첫 번째 면담
    scene2 = [
        {
            "speaker": "나레이션",
            "text": "지현은 조금 긴장한 표정으로 의자에 앉았다.",
            "choice": "시간 내주셔서 감사합니다. 몇 가지 확인할 사항이 있어서요."
        },
        {
            "speaker": "지현",
            "text": '"네. 그런데 제가 정말 의심받고 있는 건가요?"',
            "choice": "아직 누구도 범인이라고 단정하지 않았습니다. 사건 당일 무슨 일이 있었는지 확인하려는 겁니다."
        },
        {
            "speaker": "나레이션",
            "text": "지현은 잠시 망설이다가 고개를 끄덕였다.",
            "choice": None
        },
        {
            "speaker": "지현",
            "text": '"알겠어요. 무엇부터 말씀드리면 될까요?"',
            "choice": None
        }
    ]

    location = "학교 본관 · 면담실"
    line = st.session_state["chapter2_line"]

    # SCENE 01 진행
    if line < len(scene1):

        speaker, words = scene1[line]

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            speaker,
            words
        )

        if line == len(scene1) - 1:
            button_text = "면담 시작 ▶"
        else:
            button_text = "다음 ▶"

        if st.button(
            button_text,
            key="chapter2_next",
            use_container_width=True
        ):
            st.session_state["chapter2_line"] += 1
            st.rerun()

        return

    # 선택한 탐정의 대사 표시
    reply = st.session_state["chapter2_selected_reply"]

    if reply is not None:

        show_dialogue(
            "CHAPTER 02",
            "다섯 명의 증언",
            location,
            "나",
            reply
        )

        if st.button(
            "다음 ▶",
            key="chapter2_reply_next",
            use_container_width=True
        ):
            st.session_state["chapter2_selected_reply"] = None
            st.session_state["chapter2_scene2_step"] += 1
            st.rerun()

        return

    # SCENE 02 진행
    step = st.session_state["chapter2_scene2_step"]

    if step >= len(scene2):
        show_chapter2_scene3()
        return

    current = scene2[step]

    show_dialogue(
        "CHAPTER 02",
        "다섯 명의 증언",
        location,
        current["speaker"],
        current["text"]
    )

    if current["choice"] is not None:

        options = [current["choice"]]

        selected = choose_dialogue(
            options,
            "chapter2_choice_" + str(step)
        )

        if selected is not None:
            st.session_state["chapter2_selected_reply"] = options[selected]
            st.rerun()

    elif step < len(scene2) - 1:

        if st.button(
            "다음 ▶",
            key="chapter2_scene2_next",
            use_container_width=True
        ):
            st.session_state["chapter2_scene2_step"] += 1
            st.rerun()

    else:

        if st.button(
            "지현의 진술 듣기 ▶",
            key="chapter2_to_scene3",
            use_container_width=True
        ):
            st.session_state["chapter2_scene2_step"] += 1
            st.rerun()
