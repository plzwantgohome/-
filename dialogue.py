
import streamlit as st
from ui import show_dialogue


def choose_dialogue(options, key_prefix, disabled_indices=None):
    # 선택지 표시 및 이미 선택한 질문 비활성화
    if disabled_indices is None:
        disabled_indices = []

    st.html("""
    <style>
    div[class*="st-key-dialogue_option_"] button {
        width: fit-content !important;
        max-width: 100% !important;
        height: auto !important;
        min-height: 55px !important;
        padding: 12px 20px !important;
        letter-spacing: 1px !important;
    }

    div[class*="st-key-dialogue_option_"] button p {
        white-space: normal !important;
        overflow-wrap: anywhere !important;
        line-height: 1.6 !important;
    }

    div[class*="st-key-dialogue_option_"] button:disabled {
        opacity: 0.4 !important;
        cursor: not-allowed !important;
    }
    </style>
    """)

    for i, option in enumerate(options):
        already_asked = i in disabled_indices
        label = ("✓ " if already_asked else "") + option

        with st.container(
            key=f"dialogue_option_{key_prefix}_{i}"
        ):
            if st.button(
                label,
                key=f"{key_prefix}_{i}",
                disabled=already_asked
            ):
                return i

    return None


def play_questions(entry, key_prefix, chapter, title, location):
    # 각 질문 장면의 진행 상황을 별도로 기억
    phase_key = key_prefix + "_phase"
    selected_key = key_prefix + "_selected"
    asked_key = key_prefix + "_asked"

    if phase_key not in st.session_state:
        st.session_state[phase_key] = "select"

    if selected_key not in st.session_state:
        st.session_state[selected_key] = None

    if asked_key not in st.session_state:
        st.session_state[asked_key] = []

    options = entry["choices"]
    phase = st.session_state[phase_key]
    asked = st.session_state[asked_key]

    # 1단계: 질문 선택
    if phase == "select":

        show_dialogue(
            chapter, title, location,
            "나레이션", entry["text"]
        )

        st.caption(
            f"확인한 질문: {len(asked)} / {len(options)}"
        )

        selected = choose_dialogue(
            [question for question, answer in options],
            key_prefix,
            disabled_indices=asked
        )

        if selected is not None:
            st.session_state[selected_key] = selected
            st.session_state[phase_key] = "question"
            st.rerun()

        # 모든 질문을 완료한 뒤에만 다음 장면으로 이동
        if len(asked) == len(options):

            if st.button(
                "모든 질문 확인 완료 · 다음 장면 ▶",
                key=key_prefix + "_finish",
                use_container_width=True
            ):
                return True

    # 2단계: 탐정의 질문 출력
    elif phase == "question":

        selected = st.session_state[selected_key]
        question, answer = options[selected]

        show_dialogue(
            chapter, title, location,
            "나", question
        )

        if st.button(
            "다음 ▶",
            key=key_prefix + "_question_next",
            use_container_width=True
        ):
            st.session_state[phase_key] = "answer"
            st.rerun()

    # 3단계: 상대방의 답변 출력
    elif phase == "answer":

        selected = st.session_state[selected_key]
        question, answer = options[selected]

        answer_speaker = entry.get(
            "answer_speaker",
            "나레이션"
        )

        show_dialogue(
            chapter, title, location,
            answer_speaker, answer
        )

        if st.button(
            "다음 ▶",
            key=key_prefix + "_answer_next",
            use_container_width=True
        ):
            # 이번에 질문한 번호를 기록
            if selected not in asked:
                st.session_state[asked_key] = asked + [selected]

            # 질문 목록으로 돌아가기
            st.session_state[phase_key] = "select"
            st.session_state[selected_key] = None

            # 질문이 하나뿐이면 바로 다음 장면으로 이동
            if len(options) == 1:
                return True

            st.rerun()

    return False
