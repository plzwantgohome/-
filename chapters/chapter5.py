
import streamlit as st
from dialogue import choose_dialogue
from ui import show_dialogue


CHAPTER = "CHAPTER 05"
TITLE = "종이 한 장의 행방"


INTRO_LINES = [
    ("나레이션", "유출 사진 속 파란 별 모양 스티커는 공용 인쇄실 책상에 붙어 있었다."),
    ("나", '"사진이 이곳에서 찍혔다면, 시험지는 어떻게 인쇄실까지 나온 걸까?"'),
    ("나레이션", "나는 학교 측에 사건 당일 공용 프린터의 출력 기록을 요청했다."),
    ("나레이션", "잠시 뒤, 사용 시각과 계정, 출력 문서명이 정리된 기록을 전달받았다."),
    ("나", '"누가 시험지보다 먼저 출력했고, 누가 그다음에 출력했는지 확인해 보자."'),
]


# 각 기록은 원하는 순서로 열어 보고 다시 확인할 수 있다.
RECORDS = {
    "담당 교사": {
        "location": "공용 인쇄실 · 프린터 기록",
        "lines": [
            ("나레이션", "20시 41분, 시험 담당 교사의 계정으로 문서 한 건을 출력한 기록이 있었다."),
            ("나레이션", "파일명은 '2학년 중간고사 최종본.pdf'였다."),
            ("나", '"시험지가 교무실 밖으로 나온 순간이 여기였어."'),
            ("나레이션", "기록에는 출력한 문서의 이름이 남아 있었지만, 모든 종이가 수거되었는지는 표시되어 있지 않았다."),
        ],
    },
    "다인": {
        "location": "공용 인쇄실 · 프린터 기록",
        "lines": [
            ("나레이션", "20시 30분, 다인의 계정으로 발표 자료를 출력한 기록이 남아 있었다."),
            ("나", '"다인이 말한 출력 시각과 일치해."'),
            ("나레이션", "다인은 면담에서 인쇄를 마친 뒤 1층에서 유주를 만나 20시 40분쯤 함께 귀가했다고 말했다."),
        ],
    },
    "혜린": {
        "location": "공용 인쇄실 · 프린터 기록",
        "lines": [
            ("나레이션", "21시 07분에 남겨진 출력 기록을 확인했다."),
            ("나레이션", "사용 계정은 혜린, 파일명은 '수행평가_발표자료.pdf'였다."),
            ("나", '"혜린의 계정이 사용됐다고?"'),
            ("나레이션", "계정 기록만으로 실제 프린터 앞에 있었던 사람이 누구인지 단정할 수는 없었다."),
            ("나", '"하지만 확인할 필요가 있는 기록이 생겼어."'),
        ],
    },
}


# 출력 순서를 맞힌 후 시험 담당 교사를 찾아가는 장면
TEACHER_LINES = [
    ("나레이션", "출력 기록을 시간순으로 정리하자 사건의 흐름이 조금씩 드러났다."),
    ("나", '"다인은 시험지 출력 전에 인쇄실을 이용했어. 그리고 시험지가 출력된 뒤에는 혜린의 기록이 남아 있지."'),
    ("나", '"그렇다면 시험지를 출력했던 선생님께 직접 확인해 봐야겠어."'),
    ("나레이션", "나는 시험 담당 교사를 찾아가 사건 당일의 상황을 물었다."),
    ("나", '"선생님, 사건 당일 20시 41분에 공용 인쇄실에서 시험지를 출력하셨습니까?"'),
    ("교사", '"네, 맞습니다. 그날 저녁 시험지를 출력했어요."'),
    ("나", '"출력하신 시험지는 모두 가져오셨나요?"'),
    ("교사", '"바로 챙겨 오긴 했는데, 종이 수까지 일일이 확인하지는 않았어요."'),
    ("나", '"그렇다면 시험지 한 장이 인쇄실에 남아 있었을 가능성도 있겠군요."'),
    ("교사", '"확실하지는 않지만, 그럴 가능성도 있겠네요."'),
    ("나레이션", "선생님과의 대화를 마친 나는 지금까지의 기록을 다시 살펴보았다."),
]


# 챕터 5 마지막 장면
ENDING_LINES = [
    ("나레이션", "나는 지금까지 확인한 출력 기록과 선생님의 증언을 정리했다."),
    ("나", '"다인은 시험지가 출력되기 전에 인쇄실을 이용했어."'),
    ("나", '"20시 41분에는 시험지가 출력됐고, 21시 07분에는 혜린 계정의 사용 기록이 남아 있지."'),
    ("나레이션", "선생님은 출력한 시험지를 모두 챙겼는지 확신하지 못했다."),
    ("나", '"만약 시험지 한 장이 인쇄실에 남아 있었다면, 그 뒤에 인쇄실을 이용한 사람이 발견했을 수도 있어."'),
    ("나레이션", "나는 챕터 2에서 기록해 둔 학생들의 증언을 다시 펼쳤다."),
    ("나", '"이제 실제 기록과 학생들의 말이 일치하는지 확인해야겠어."'),
]


# 챕터 마지막 조사 기록 요약
CASE_NOTES = {
    "다인 출력 기록": "20:30 다인 계정으로 발표 자료 출력. 시험지는 20:41에 출력되므로 다인의 출력은 그보다 앞선다.",
    "시험지 출력 기록": "20:41 시험 담당 교사가 '2학년 중간고사 최종본.pdf'를 출력했다.",
    "혜린 출력 기록": "21:07 혜린 계정으로 '수행평가_발표자료.pdf'를 출력한 기록이 남았다. 실제 사용자는 추가 확인이 필요하다.",
    "시험 담당 교사 확인": "교사는 시험지 출력을 인정했지만 출력물의 장수를 정확히 확인하지는 않았다. 종이 한 장이 남았을 가능성은 미확정이다.",
}


def show_lines(lines, line_key, location, skip_target=None):
    """기존 대화 UI를 이용하고 스킵 기능을 적용한다."""
    if line_key not in st.session_state:
        st.session_state[line_key] = 0

    index = st.session_state[line_key]

    if index >= len(lines):
        return True

    speaker, words = lines[index]

    if skip_target is None:
        show_dialogue(CHAPTER, TITLE, location, speaker, words)
    else:
        show_dialogue(
            CHAPTER, TITLE, location, speaker, words,
            skip_key=line_key + "_skip_button",
            skip_changes={"chapter5_phase": skip_target},
        )

    if st.button(
        "다음 ▶",
        key=line_key + "_next",
        use_container_width=True
    ):
        st.session_state[line_key] += 1
        st.rerun()

    return False


def show_records():
    """세 가지 출력 기록을 자유롭게 조사한다."""
    selected = st.session_state["chapter5_selected_record"]
    checked = st.session_state["chapter5_checked_records"]

    if selected is None:
        show_dialogue(
            CHAPTER, TITLE, "공용 인쇄실 · 기록 조사",
            "나레이션", "어떤 기록부터 확인할까?"
        )

        st.caption(f"확인한 기록: {len(checked)} / {len(RECORDS)}")

        names = list(RECORDS)
        labels = [
            ("✓ " if name in checked else "") + name
            for name in names
        ]

        choice = choose_dialogue(
            labels,
            key_prefix="chapter5_record_choice"
        )

        if choice is not None:
            st.session_state["chapter5_selected_record"] = names[choice]
            st.session_state["chapter5_record_line"] = 0
            st.rerun()

        if len(checked) == len(RECORDS):
            if st.button(
                "기록의 순서 정리하기 ▶",
                key="chapter5_to_timeline",
                use_container_width=True
            ):
                st.session_state["chapter5_phase"] = "timeline"
                st.rerun()

        return

    record = RECORDS[selected]

    if show_lines(
        record["lines"],
        "chapter5_record_line",
        record["location"]
    ):
        if selected not in checked:
            st.session_state["chapter5_checked_records"] = checked + [selected]

        st.session_state["chapter5_selected_record"] = None
        st.rerun()


def show_timeline():
    """출력 기록에 나타난 세 계정의 사용 순서를 추리한다."""
    show_dialogue(
        CHAPTER, TITLE, "공용 인쇄실 · 사건 기록",
        "나", '"세 건의 출력 기록을 시간순으로 놓으면 어떤 순서가 될까?"'
    )

    options = [
        "담당 교사 → 다인 → 혜린",
        "다인 → 담당 교사 → 혜린",
        "혜린 → 담당 교사 → 다인",
    ]

    choice = choose_dialogue(
        options,
        key_prefix="chapter5_timeline_choice"
    )

    if choice is not None:
        if choice == 1:
            st.session_state["chapter5_wrong_order"] = False
            st.session_state["chapter5_phase"] = "teacher"
        else:
            st.session_state["chapter5_wrong_order"] = True

        st.rerun()

    if st.session_state["chapter5_wrong_order"]:
        st.warning(
            "출력 시각을 다시 확인해 보자. "
            "기록 목록으로 돌아가 다시 열람할 수 있다."
        )

    if st.button(
        "출력 기록 다시 보기",
        key="chapter5_back_to_records",
        use_container_width=True
    ):
        st.session_state["chapter5_phase"] = "records"
        st.rerun()


def show_chapter5():
    """챕터 5의 장면 전환을 관리한다."""
    if "chapter5_phase" not in st.session_state:
        st.session_state["chapter5_phase"] = "intro"

    if "chapter5_checked_records" not in st.session_state:
        st.session_state["chapter5_checked_records"] = []

    if "chapter5_selected_record" not in st.session_state:
        st.session_state["chapter5_selected_record"] = None

    if "chapter5_wrong_order" not in st.session_state:
        st.session_state["chapter5_wrong_order"] = False

    phase = st.session_state["chapter5_phase"]

    # SCENE 01 · 도입
    if phase == "intro":
        if show_lines(
            INTRO_LINES,
            "chapter5_intro_line",
            "공용 인쇄실",
            skip_target="records"
        ):
            st.session_state["chapter5_phase"] = "records"
            st.rerun()
        return

    # SCENE 02 · 출력 기록 조사
    if phase == "records":
        show_records()
        return

    # SCENE 03 · 출력 순서 추리
    if phase == "timeline":
        show_timeline()
        return

    # SCENE 04 · 시험 담당 교사 확인
    if phase == "teacher":
        if show_lines(
            TEACHER_LINES,
            "chapter5_teacher_line",
            "학교 본관 · 교무실",
            skip_target="finished"
        ):
            st.session_state["chapter5_phase"] = "ending"
            st.rerun()
        return

    # SCENE 05 · 마지막 장면
    if phase == "ending":
        if show_lines(
            ENDING_LINES,
            "chapter5_ending_line",
            "학교 본관 · 자료 열람실",
            skip_target="finished"
        ):
            st.session_state["chapter5_phase"] = "finished"
            st.rerun()
        return

    # 챕터 5 조사 기록 정리
    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")

    name = st.selectbox(
        "확인할 기록",
        list(CASE_NOTES),
        key="chapter5_notes_record"
    )

    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])

    st.info(
        "챕터 5 조사를 완료했습니다. "
        "다음은 프린터 기록과 학생들의 증언을 대조할 차례입니다."
    )
    
    if st.button(
        "챕터 6로 ▶",
        key="chapter5_to_chapter6",
        use_container_width=True
    ):
        st.session_state["page"] = "chapter6"
        st.rerun() 
