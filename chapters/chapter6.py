
import streamlit as st
from dialogue import choose_dialogue, play_questions
from ui import show_dialogue


CHAPTER = "CHAPTER 06"
TITLE = "엇갈린 진술"


# SCENE 01 · 도입
INTRO_LINES = [
    ("나레이션", "나는 공용 프린터의 출력 기록과 다섯 학생의 면담 기록을 책상 위에 펼쳤다."),
    ("나", '"시험지가 인쇄실에 남았을 가능성은 있어. 하지만 누가 그것을 봤는지는 아직 몰라."'),
    ("나레이션", "프린터 사용 기록과 학생들의 말을 나란히 놓자, 확인해야 할 부분이 보이기 시작했다."),
    ("나", '"기억이 틀린 건지, 누군가 사실을 감추고 있는 건지 비교해 보자."'),
]


# SCENE 02 · 증언 및 출력 기록 조사
# 기록은 원하는 순서로 선택하고 다시 열람할 수 있다.
RECORDS = {
    "혜린의 첫 면담": {
        "location": "자료 열람실 · 면담 기록",
        "lines": [
            ("나레이션", "혜린은 사건 당일 수행평가 발표 자료를 정리했다고 말했다."),
            ("나레이션", "정확히 몇 시에 귀가했는지는 기억하지 못한다고 했다."),
            ("나레이션", "하지만 학교 프린터를 사용했는지 묻자 분명히 사용하지 않았다고 답했다."),
            ("나", '"귀가 시각은 불확실했어도 프린터 사용 여부는 부인했지."'),
        ],
    },
    "다인과 유주의 증언": {
        "location": "자료 열람실 · 면담 기록",
        "lines": [
            ("나레이션", "다인은 20시 30분쯤 공용 인쇄실에서 발표 자료를 출력했다고 진술했다."),
            ("나레이션", "유주는 1층에서 다인을 기다렸으며, 두 사람은 20시 40분쯤 함께 귀가했다고 말했다."),
            ("나레이션", "다인의 출력 시각은 프린터 기록과 일치했다."),
            ("나", '"두 사람의 귀가 시각은 증언이지만, 다인의 출력은 시험지보다 먼저였어."'),
        ],
    },
    "프린터 사용 기록": {
        "location": "공용 인쇄실 · 출력 기록",
        "lines": [
            ("나레이션", "20시 41분, 담당 교사 계정으로 시험지 파일이 출력됐다."),
            ("나레이션", "21시 07분, 혜린 계정으로 '수행평가_발표자료.pdf'를 출력한 기록이 남았다."),
            ("나", '"혜린은 프린터를 사용하지 않았다고 했는데, 기록에는 그 이름이 있어."'),
            ("나레이션", "계정 기록만으로 실제 사용자를 확정할 수는 없지만, 그냥 넘어갈 수 없는 차이였다."),
        ],
    },
}


# SCENE 04 · 혜린 재면담 도입
CONFRONT_INTRO_LINES = [
    ("나레이션", "기록을 다시 확인한 나는 혜린에게 추가 면담을 요청했다."),
    ("나레이션", "잠시 뒤 면담실 문이 열리고 혜린이 들어왔다."),
    ("혜린", '"다시 부르신 이유가 있나요?"'),
    ("나", '"지난번에 한 진술과 새로 확인한 기록이 일치하지 않는 부분이 있습니다."'),
    ("혜린", '"어떤 기록이요?"'),
]


# SCENE 05 · 혜린에게 직접 질문
QUESTIONS = {
    "text": "혜린의 첫 진술과 출력 기록을 대조하자. 어떤 질문부터 할까?",
    "choices": [
        (
            "처음 면담에서 프린터를 사용하지 않았다고 말했죠?",
            '"네. 그렇게 말씀드렸어요. 그날 학교 프린터를 쓴 기억은 없어요."',
        ),
        (
            "21시 07분에 혜린 학생 계정으로 발표 자료가 출력된 기록이 있습니다.",
            '"제 계정이요? 그 기록이 있다면 누가 사용했는지 확인해 봐야 할 것 같아요. 저는 기억나지 않아요."',
        ),
        (
            "그날 정확히 언제 학교를 떠났는지 확인할 수 있습니까?",
            '"정확한 시간은 잘 모르겠어요. 자료를 정리하고 나간 건 맞는데, 몇 시였는지는 다시 생각해 볼게요."',
        ),
    ],
    "answer_speaker": "혜린",
}


# SCENE 06 · 마지막 장면
ENDING_LINES = [
    ("나레이션", "혜린과의 추가 면담을 마쳤다. 그녀는 프린터 사용 기록을 명확하게 설명하지 못했다."),
    ("나", '"혜린은 프린터를 사용하지 않았다고 했지만, 기록에는 혜린 계정으로 출력한 내역이 있어."'),
    ("나", '"그렇다고 계정 기록만으로 혜린이 시험지를 촬영했다고 단정할 수는 없어."'),
    ("나레이션", "나는 잠시 책상 위에 놓인 유출 사진을 바라보았다."),
    ("나", '"사진이 공용 인쇄실에서 찍혔다는 사실과 출력 기록을 연결할 다른 단서가 필요해."'),
    ("나레이션", "사진이 언제 촬영됐는지, 공개된 내용이 전부인지 확인할 차례였다."),
]


# 챕터 6 완료 후 조사 기록 요약
CASE_NOTES = {
    "혜린의 첫 진술": (
        "수행평가 자료를 정리했다고 했으며 귀가 시각은 기억하지 못했다. "
        "학교 프린터 사용은 부인했다."
    ),
    "다인·유주의 증언": (
        "다인은 20:30경 출력했고 유주는 1층에서 기다렸다고 했다. "
        "두 사람은 20:40경 함께 귀가했다고 진술했다."
    ),
    "프린터 사용 기록": (
        "20:41 시험지 출력, 21:07 혜린 계정으로 수행평가 자료 출력. "
        "계정과 실제 사용자가 일치하는지는 추가 확인이 필요하다."
    ),
    "혜린의 재면담": (
        "혜린은 자신의 계정으로 남은 출력 기록을 설명하지 못했다. "
        "프린터 사용을 부인한 첫 진술과 충돌한다."
    ),
}


def show_lines(lines, line_key, location, skip_target=None):
    """대사를 한 줄씩 보여주며 스킵은 지정한 장면에서만 허용한다."""
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
            skip_changes={"chapter6_phase": skip_target},
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
    """세 기록을 모두 확인할 때까지 자유롭게 다시 열람할 수 있다."""
    selected = st.session_state["chapter6_selected_record"]
    checked = st.session_state["chapter6_checked_records"]

    if selected is None:
        show_dialogue(
            CHAPTER, TITLE, "자료 열람실 · 증언 대조",
            "나레이션", "어떤 기록부터 다시 확인할까?"
        )

        st.caption(f"확인한 기록: {len(checked)} / {len(RECORDS)}")

        names = list(RECORDS)
        labels = [
            ("✓ " if name in checked else "") + name
            for name in names
        ]

        choice = choose_dialogue(
            labels,
            key_prefix="chapter6_record_choice"
        )

        if choice is not None:
            st.session_state["chapter6_selected_record"] = names[choice]
            st.session_state["chapter6_record_line"] = 0
            st.rerun()

        if len(checked) == len(RECORDS):
            if st.button(
                "모순되는 진술 찾기 ▶",
                key="chapter6_to_compare",
                use_container_width=True
            ):
                st.session_state["chapter6_phase"] = "compare"
                st.rerun()

        return

    record = RECORDS[selected]

    if show_lines(
        record["lines"],
        "chapter6_record_line",
        record["location"]
    ):
        if selected not in checked:
            st.session_state["chapter6_checked_records"] = checked + [selected]

        st.session_state["chapter6_selected_record"] = None
        st.rerun()


def show_compare():
    """서로 충돌하는 기록을 선택해야 재면담으로 진행할 수 있다."""
    show_dialogue(
        CHAPTER, TITLE, "자료 열람실 · 증언 대조",
        "나", '"지금까지 확인한 기록 중, 분명히 서로 어긋나는 것은 무엇일까?"'
    )

    options = [
        "다인이 시험지보다 먼저 발표 자료를 출력했다는 사실",
        "혜린이 프린터 사용을 부인했지만 혜린 계정으로 출력한 기록이 있다는 사실",
        "담당 교사가 모든 출력물을 챙겼는지 기억하지 못하는 사실",
    ]

    choice = choose_dialogue(
        options,
        key_prefix="chapter6_compare_choice"
    )

    if choice is not None:
        if choice == 1:
            st.session_state["chapter6_phase"] = "confront_intro"
        else:
            st.session_state["chapter6_wrong_comparison"] = True

        st.rerun()

    if st.session_state["chapter6_wrong_comparison"]:
        st.warning(
            "두 기록이 서로 반대되는 내용을 말하는지 다시 확인하자."
        )

        if st.button(
            "기록 다시 보기",
            key="chapter6_back_to_records",
            use_container_width=True
        ):
            st.session_state["chapter6_phase"] = "records"
            st.rerun()


def show_chapter6():
    """챕터 6의 진행 상태와 장면 전환을 관리한다."""
    if "chapter6_phase" not in st.session_state:
        st.session_state["chapter6_phase"] = "intro"

    if "chapter6_selected_record" not in st.session_state:
        st.session_state["chapter6_selected_record"] = None

    if "chapter6_checked_records" not in st.session_state:
        st.session_state["chapter6_checked_records"] = []

    if "chapter6_wrong_comparison" not in st.session_state:
        st.session_state["chapter6_wrong_comparison"] = False

    phase = st.session_state["chapter6_phase"]

    # SCENE 01 · 도입
    if phase == "intro":
        if show_lines(
            INTRO_LINES,
            "chapter6_intro_line",
            "학교 본관 · 자료 열람실",
            skip_target="records"
        ):
            st.session_state["chapter6_phase"] = "records"
            st.rerun()
        return

    # SCENE 02 · 기록 조사
    if phase == "records":
        show_records()
        return

    # SCENE 03 · 모순 찾기
    if phase == "compare":
        show_compare()
        return

    # SCENE 04 · 혜린 재면담 도입
    if phase == "confront_intro":
        if show_lines(
            CONFRONT_INTRO_LINES,
            "chapter6_confront_line",
            "학교 본관 · 면담실",
            skip_target="questions"
        ):
            st.session_state["chapter6_phase"] = "questions"
            st.rerun()
        return

    # SCENE 05 · 혜린에게 질문
    if phase == "questions":
        if play_questions(
            QUESTIONS,
            "chapter6_questions",
            CHAPTER,
            TITLE,
            "학교 본관 · 면담실"
        ):
            st.session_state["chapter6_phase"] = "ending"
            st.rerun()
        return

    # SCENE 06 · 마지막 장면
    if phase == "ending":
        if show_lines(
            ENDING_LINES,
            "chapter6_ending_line",
            "학교 본관 · 자료 열람실",
            skip_target="finished"
        ):
            st.session_state["chapter6_phase"] = "finished"
            st.rerun()
        return

    # 챕터 6 조사 기록 정리
    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")

    name = st.selectbox(
        "확인할 기록",
        list(CASE_NOTES),
        key="chapter6_notes_record"
    )

    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])

    st.info(
        "챕터 6 조사를 완료했습니다. "
        "다음은 유출 사진에 남은 정보입니다."
    )
    
    if st.button(
        "챕터 7로 ▶",
        key="chapter6_to_chapter7",
        use_container_width=True
    ):
        st.session_state["page"] = "chapter7"
        st.rerun() 
