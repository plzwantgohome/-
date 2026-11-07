
import streamlit as st
from dialogue import choose_dialogue, play_questions
from ui import show_dialogue


CHAPTER = "CHAPTER 07"
TITLE = "남겨진 의혹"


# SCENE 01 · 도입
INTRO_LINES = [
    ("나레이션", "혜린과의 추가 면담을 마친 나는 앞서 조사했던 기록들을 다시 펼쳤다."),
    ("나", '"혜린의 말과 출력 기록이 어긋나지만, 아직 확실한 결론을 내릴 수는 없어."'),
    ("나레이션", "지현의 늦은 이동과 예주가 다룰 줄 아는 CCTV의 기록 공백도 해결되지 않은 채 남아 있었다."),
    ("나", '"다른 의혹을 그대로 둔 채 한 사람만 의심할 수는 없지. 두 사람부터 다시 확인하자."'),
]


# SCENE 02 · 재면담에서 선택할 질문
INTERVIEWS = {
    "지현": {
        "text": "21시 18분에 2층으로 올라간 지현에게 무엇을 물어볼까?",
        "choices": [
            (
                "21시 18분에 2층으로 올라간 이유가 무엇인가요?",
                '"학생회 행사 서류를 교무실 옆 제출함에 넣으러 갔어요. 담당 선생님께 드려야 했거든요."',
            ),
            (
                "그런데 처음에는 아홉 시쯤 귀가했다고 했잖아요?",
                '"정확한 시간을 보지 않고 대충 기억해서 그렇게 말했어요. 생각보다 늦게까지 남았네요."',
            ),
        ],
        "answer_speaker": "지현",
    },
    "예주": {
        "text": "CCTV 기록 공백이 발견된 예주에게 무엇을 물어볼까?",
        "choices": [
            (
                "22시 05분부터 12분까지 CCTV 영상이 비어 있던데, 이유를 아나요?",
                '"저는 그 시간에 CCTV 저장 장치를 만지지 않았어요. 무슨 문제였는지도 잘 몰라요."',
            ),
            (
                "20시 30분쯤 인쇄실 근처에서 봤다는 사람은 혜린이 맞나요?",
                '"멀리서 파란 파일 같은 걸 든 사람을 봤을 뿐이에요. 혜린이라고 확신할 수는 없어요."',
            ),
        ],
        "answer_speaker": "예주",
    },
}


# 면담 내용을 다른 자료와 대조해 검증하는 장면
VERIFICATION = {
    "지현": [
        ("나레이션", "나는 지현이 제출했다는 학생회 행사 서류부터 확인했다."),
        ("나레이션", "서류 파일에는 21시 12분에 수정한 기록이 남아 있었다."),
        ("나레이션", "교무실 옆 서류 제출함에서도 해당 서류가 발견됐다. 담당 교사 확인란은 아직 비어 있었다."),
        ("나", '"늦게까지 서류를 정리했다는 설명은 자료와 맞아떨어져."'),
        ("나레이션", "학교 출입구 영상에는 21시 27분에 지현이 학교를 나서는 모습도 남아 있었다."),
        ("나", '"아홉 시에 귀가했다는 말은 부정확했지만, 2층에 올라간 이유를 뒷받침할 기록은 있군."'),
        ("나레이션", "다만 이 기록만으로 지현이 시험지 유출과 무관하다고 완전히 단정할 수는 없었다."),
    ],
    "예주": [
        ("나레이션", "예주의 말을 들은 나는 학교 CCTV 관리 담당자에게 저장 장치 작동 기록을 요청했다."),
        ("나레이션", "기록에는 22시 05분에 일부 영상 저장 채널의 연결이 끊겼다는 오류가 남아 있었다."),
        ("나레이션", "22시 12분에는 해당 채널이 자동으로 복구된 내역이 확인됐다."),
        ("나", '"영상이 비어 있었던 시간과 일치해. 저장 장치 오류로 설명할 수 있겠어."'),
        ("나레이션", "확인한 로그에는 해당 구간을 수동으로 삭제한 내역이 없었다."),
        ("나", '"예주가 영상 장비를 다룬다는 이유만으로 조작했다고 볼 수는 없지."'),
        ("나레이션", "20시 30분쯤 보았다는 사람 역시 얼굴을 확인하지 못한 목격담일 뿐이었다."),
    ],
}


# SCENE 04 · 새 단서를 찾기 위한 사진 확인
PHOTO_LINES = [
    ("나레이션", "두 사람을 다시 조사했지만, 시험지를 촬영한 사람이 누구인지는 여전히 밝혀지지 않았다."),
    ("나", '"교무실 출입 기록보다 유출 사진 자체를 더 살펴봐야겠어."'),
    ("나레이션", "기존 게시글 캡처 화면에는 사진의 촬영 시간이 표시되어 있지 않았다."),
    ("나레이션", "학교 측은 게시판 운영진에게 요청해 삭제된 게시글의 첨부 이미지 사본을 확보했다."),
    ("나레이션", "이미지에 남은 촬영 시각 정보는 21시 09분이었다."),
    ("나", '"21시 09분... 혜린 계정으로 프린터를 사용한 21시 07분에서 불과 2분 뒤야."'),
    ("나레이션", "촬영 시각 정보는 변경될 수도 있어 이것만으로 촬영자를 확정할 수는 없었다."),
    ("나", '"하지만 두 기록이 가까운 시간에 남았다는 건 분명 확인할 가치가 있어."'),
]


# SCENE 05 · 마지막 장면
ENDING_LINES = [
    ("나레이션", "나는 다시 조사한 결과와 유출 사진의 정보를 한데 모았다."),
    ("나", '"지현의 늦은 이동은 학생회 서류와 연결되고, 예주의 CCTV 공백도 장치 오류 기록으로 설명할 수 있어."'),
    ("나", '"반면 혜린은 프린터를 사용하지 않았다고 했지만, 21시 07분에 혜린 계정의 출력 기록이 남아 있지."'),
    ("나레이션", "게다가 사진 파일에 남은 촬영 시각은 그로부터 2분 뒤인 21시 09분이었다."),
    ("나레이션", "게시판에 공개되었던 사진에는 시험지의 일부만 담겨 있었다."),
    ("나", '"누군가 공개된 사진에 없는 내용까지 알고 있다면, 그 이유를 설명해야 할 거야."'),
    ("나레이션", "나는 마지막 면담을 준비하며 지금까지 모은 기록을 다시 정리했다."),
]


# 챕터 마지막 조사 기록 요약
CASE_NOTES = {
    "지현의 이동": (
        "21:18에 2층으로 올라간 모습이 확인됨. 학생회 서류 수정 기록(21:12), "
        "서류 제출함에 남은 문서, 귀가 영상(21:27)이 늦은 이동에 대한 설명을 뒷받침함."
    ),
    "예주의 CCTV 의혹": (
        "22:05~22:12 일부 CCTV 영상 공백. 같은 시간대에 저장 채널 연결 오류와 자동 복구 "
        "기록이 있으며, 확인한 로그에서 수동 삭제 내역은 발견되지 않음."
    ),
    "예주의 목격담": (
        "20:30경 인쇄실 쪽 복도에서 파란 파일 같은 물건을 든 사람을 봤으나 "
        "얼굴은 확인하지 못함. 혜린이라고 확정할 수 없음."
    ),
    "유출 사진의 촬영 시각": (
        "게시판 운영진이 제공한 첨부 이미지 사본의 촬영 시각 정보는 21:09. "
        "21:07 혜린 계정의 프린터 출력 기록과 2분 차이. 촬영자는 미확정."
    ),
}


PERSON_KEYS = {"지현": "jihyun", "예주": "yeju"}


def show_lines(lines, line_key, location, skip_target=None):
    """공통 대화 UI로 한 줄씩 보여주고 스킵 기능을 적용한다."""
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
            skip_changes=(
                {line_key: len(lines)}
                if skip_target == "line_end"
                else {"chapter7_phase": skip_target}
),
        )

    if st.button(
        "다음 ▶",
        key=line_key + "_next",
        use_container_width=True
    ):
        st.session_state[line_key] += 1
        st.rerun()

    return False


def show_people():
    """지현과 예주를 원하는 순서로 재면담하고 기록으로 검증한다."""
    selected = st.session_state["chapter7_selected_person"]
    checked = st.session_state["chapter7_checked_people"]

    if selected is None:
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 자료 열람실",
            "나레이션", "아직 설명되지 않은 의혹이 남아 있다. 누구부터 다시 조사할까?"
        )

        st.caption(f"조사한 인물: {len(checked)} / {len(INTERVIEWS)}")

        names = list(INTERVIEWS)
        labels = [("✓ " if name in checked else "") + name for name in names]

        choice = choose_dialogue(
            labels,
            key_prefix="chapter7_person_choice"
        )

        if choice is not None:
            person = names[choice]
            st.session_state["chapter7_selected_person"] = person
            st.session_state["chapter7_person_stage"] = (
                "verify" if person in checked else "interview"
            )
            st.session_state["chapter7_verify_line"] = 0
            st.rerun()

        if len(checked) == len(INTERVIEWS):
            if st.button(
                "재조사 결과 정리하기 ▶",
                key="chapter7_to_judgment",
                use_container_width=True
            ):
                st.session_state["chapter7_phase"] = "judgment"
                st.rerun()

        return

    person_key = PERSON_KEYS[selected]

    if st.session_state["chapter7_person_stage"] == "interview":
        if play_questions(
            INTERVIEWS[selected],
            "chapter7_" + person_key + "_questions",
            CHAPTER,
            TITLE,
            "학교 본관 · 면담실"
        ):
            st.session_state["chapter7_person_stage"] = "verify"
            st.rerun()
        return

    if show_lines(
        VERIFICATION[selected],
        "chapter7_verify_line",
        "학교 본관 · 기록 대조",
        skip_target="line_end"
    ):
        if selected not in checked:
            st.session_state["chapter7_checked_people"] = checked + [selected]

        st.session_state["chapter7_selected_person"] = None
        st.session_state["chapter7_person_stage"] = "interview"
        st.rerun()


def show_judgment():
    """재조사 결과를 과도하게 단정하지 않고 올바르게 해석한다."""
    show_dialogue(
        CHAPTER, TITLE, "학교 본관 · 자료 열람실",
        "나", '"지현과 예주에 관한 기록을 종합하면 어떤 결론이 가장 타당할까?"'
    )

    options = [
        "지현이 늦게 귀가했으니 시험지를 유출한 범인이다.",
        "예주가 영상 장비를 다룰 줄 아니 CCTV 기록을 조작했다.",
        "두 사람의 수상한 정황에는 다른 설명이 있지만, 유출에 관여하지 않았다고 단정할 수도 없다.",
    ]

    choice = choose_dialogue(
        options,
        key_prefix="chapter7_judgment_choice"
    )

    if choice is not None:
        if choice == 2:
            st.session_state["chapter7_phase"] = "photo"
            st.session_state["chapter7_wrong_judgment"] = False
        else:
            st.session_state["chapter7_wrong_judgment"] = True

        st.rerun()

    if st.session_state["chapter7_wrong_judgment"]:
        st.warning(
            "의심스러운 행동과 범행의 증거를 구별해야 해. 다시 생각해 보자."
        )

    if st.button(
        "재조사 기록 다시 보기",
        key="chapter7_back_to_people",
        use_container_width=True
    ):
        st.session_state["chapter7_phase"] = "people"
        st.rerun()


def show_chapter7():
    """챕터 7의 조사 순서와 장면 전환을 관리한다."""
    if "chapter7_phase" not in st.session_state:
        st.session_state["chapter7_phase"] = "intro"

    if "chapter7_selected_person" not in st.session_state:
        st.session_state["chapter7_selected_person"] = None

    if "chapter7_checked_people" not in st.session_state:
        st.session_state["chapter7_checked_people"] = []

    if "chapter7_person_stage" not in st.session_state:
        st.session_state["chapter7_person_stage"] = "interview"

    if "chapter7_wrong_judgment" not in st.session_state:
        st.session_state["chapter7_wrong_judgment"] = False

    phase = st.session_state["chapter7_phase"]

    # SCENE 01 · 도입
    if phase == "intro":
        if show_lines(
            INTRO_LINES,
            "chapter7_intro_line",
            "학교 본관 · 자료 열람실",
            skip_target="people"
        ):
            st.session_state["chapter7_phase"] = "people"
            st.rerun()
        return

    # SCENE 02 · 지현과 예주 재조사
    if phase == "people":
        show_people()
        return

    # SCENE 03 · 추리 결과 판단
    if phase == "judgment":
        show_judgment()
        return

    # SCENE 04 · 사진 촬영 시각 조사
    if phase == "photo":
        if show_lines(
            PHOTO_LINES,
            "chapter7_photo_line",
            "학교 본관 · 자료 열람실",
            skip_target="finished"
        ):
            st.session_state["chapter7_phase"] = "ending"
            st.rerun()
        return

    # SCENE 05 · 마지막 장면
    if phase == "ending":
        if show_lines(
            ENDING_LINES,
            "chapter7_ending_line",
            "학교 본관 · 자료 열람실",
            skip_target="finished"
        ):
            st.session_state["chapter7_phase"] = "finished"
            st.rerun()
        return

    # 챕터 마지막에 핵심 증거를 요약하고 다음 챕터로 이동한다.
    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")

    name = st.selectbox(
        "확인할 기록",
        list(CASE_NOTES),
        key="chapter7_notes_record"
    )

    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])

    st.info(
        "챕터 7 조사를 완료했습니다. "
        "다음은 사건의 진실을 밝히는 마지막 추리입니다."
    )
   
    if st.button(
        "챕터 8로 ▶",
        key="chapter7_to_chapter8",
        use_container_width=True
    ):
        st.session_state["page"] = "chapter8"
        st.rerun() 
