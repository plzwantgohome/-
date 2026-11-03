
import streamlit as st
from dialogue import choose_dialogue, play_questions
from ui import show_dialogue


CHAPTER = "CHAPTER 08"
TITLE = "사건의 진실"
MAX_LIVES = 3


# SCENE 01 · 마지막 면담 준비
INTRO_LINES = [
    ("나레이션", "나는 지금까지 확인한 사진 정보와 공용 프린터 기록을 다시 펼쳤다."),
    ("나", '"시험지 사진은 21시 09분에 촬영된 것으로 기록돼 있어. 혜린 계정의 출력은 21시 07분이었지."'),
    ("나레이션", "게시판에 공개된 사진에는 시험지 앞부분의 1~3번 문제만 담겨 있었다."),
    ("나", '"다른 사람이 게시물을 봤을 가능성도 있으니, 사진 내용만 안다고 범인이라고 단정할 수는 없어."'),
    ("나레이션", "나는 혜린에게 마지막으로 몇 가지를 확인하기로 했다."),
]


# SCENE 02 · 혜린의 마지막 면담
LAST_QUESTIONS = {
    "text": "혜린에게 어떤 질문부터 할까?",
    "choices": [
        (
            "21시 07분의 프린터 사용 기록에 관해 다시 설명해 줄 수 있나요?",
            '"제 계정으로 출력한 기록이 있다는 건 들었어요. 그런데 제가 직접 사용했는지는 기억이 안 나요."',
        ),
        (
            "유출된 시험지 사진에서 기억나는 내용이 있나요?",
            '"앞쪽 문제는 잘 기억 안 나요. 그런데 마지막 문제에 그래프까지 나온 건 너무 어렵지 않았어요?"',
        ),
        (
            "그 시험지 사진을 직접 본 적이 있나요?",
            '"사건이 알려진 뒤에 다른 학생들에게서 사진 이야기를 들었어요. 게시글을 직접 봤는지는 확실하지 않아요."',
        ),
    ],
    "answer_speaker": "혜린",
}


# SCENE 03 · 실언과 비공개 정보 대조
VERIFY_LINES = [
    ("나레이션", "면담이 끝난 뒤, 나는 혜린의 발언 중 한 구절을 다시 떠올렸다."),
    ("나", '"마지막 문제에 그래프가 나왔다고? 공개된 사진에는 1~3번 문제밖에 없었는데."'),
    ("나레이션", "나는 시험 담당 교사에게 공개되지 않은 나머지 문제의 구성을 확인했다."),
    ("교사", '"맞습니다. 시험지 뒷부분 마지막 문제에는 그래프가 들어 있습니다. 하지만 그 부분은 유출 사진에 나오지 않았어요."'),
    ("나레이션", "혜린이 말한 내용은 실제 시험지와 일치했다."),
    ("나", '"공개되지 않은 내용을 어떻게 알았을까? 프린터 기록과 촬영 시각까지 함께 따져 봐야겠어."'),
    ("나레이션", "나는 지금까지의 증거를 한자리에 정리하고 최종 추리를 시작했다."),
]


# 최종 추리에서 다시 열람할 수 있는 조사 기록
CASE_NOTES = {
    "공용 인쇄실": (
        "유출 사진의 배경에 나온 파란 별 스티커가 공용 인쇄실 책상의 스티커와 일치한다. "
        "사진이 인쇄실에서 촬영됐을 가능성이 높다."
    ),
    "프린터 사용 기록": (
        "20:30 다인 계정으로 발표 자료 출력 → 20:41 담당 교사 계정으로 시험지 출력 "
        "→ 21:07 혜린 계정으로 수행평가 자료 출력. 계정 기록만으로 실제 사용자를 확정할 수는 없다."
    ),
    "사진 촬영 시각": (
        "게시판 첨부 이미지 사본의 촬영 시각 정보는 21:09. "
        "혜린 계정의 출력 기록에서 2분 뒤다. 촬영 시각 정보 역시 단독 증거는 아니다."
    ),
    "혜린의 진술": (
        "혜린은 처음에 학교 프린터 사용을 부인했다. 마지막 면담에서는 "
        "공개 사진에 없는 시험지 뒷부분의 그래프 문제를 언급했다."
    ),
    "다른 학생들": (
        "지현의 21:18 이동에는 학생회 서류 기록이 있고, 예주의 22:05~22:12 CCTV 공백은 "
        "저장 채널 오류 기록으로 설명된다. 이 사실만으로 무관함이 완전히 증명되지는 않는다."
    ),
}


# 최종 추리 선택지
SUSPECTS = ["지현", "혜린", "예주", "유주", "다인"]

PLACES = [
    "교무실",
    "학생회실",
    "방송실",
    "공용 인쇄실",
]

EVIDENCES = [
    "지현이 21시 18분에 2층으로 올라간 CCTV 기록",
    "혜린 계정의 출력 기록과 공개되지 않은 문제를 언급한 혜린의 발언",
    "예주가 영상 장비를 다룰 수 있다는 사실",
    "유주와 다인이 함께 귀가했다고 말한 증언",
]


# SCENE 05 · 추리 성공 시 진엔딩
TRUE_ENDING_LINES = [
    ("나레이션", "나는 모아 둔 증거를 다시 살펴본 뒤 혜린을 불렀다."),
    ("나", '"21시 07분에 혜린 학생 계정으로 출력된 기록이 있습니다. 사진의 촬영 시각은 그로부터 2분 뒤였죠."'),
    ("나", '"무엇보다 공개된 사진에는 없던 마지막 그래프 문제를 알고 있었어요. 어떻게 알았습니까?"'),
    ("나레이션", "혜린은 한동안 말을 잇지 못했다."),
    ("혜린", '"...맞아요. 그날 인쇄실에서 제 자료를 출력했어요."'),
    ("혜린", '"프린터 옆에 시험지 한 장이 남아 있었어요. 그냥 두고 나왔어야 했는데 사진을 찍었어요."'),
    ("혜린", '"그날 밤 익명 게시판에 올렸다가 무서워져서 바로 지웠어요."'),
    ("나레이션", "혜린의 자백으로 사진을 촬영한 사람과 시험지가 인쇄실에 남게 된 경위가 밝혀졌다."),
    ("나", '"흩어져 있던 기록들이 이제 하나의 흐름으로 이어지는군."'),
]


# SCENE 06 · 세 번 실패 시 배드엔딩
FALSE_ENDING_LINES = [
    ("나레이션", "세 번의 추리 끝에도 나는 증거들을 올바르게 연결하지 못했다."),
    ("나레이션", "결정적인 결론을 내리지 못한 채 조사는 종료되었다."),
    ("나레이션", "며칠 뒤, 아무도 없는 공용 인쇄실에 혜린이 들어섰다."),
    ("나레이션", "혜린은 프린터를 바라보다가 작게 비웃었다."),
    ("혜린", '"끝까지 못 알아챘네. 아무도 못 찾을 줄 알았는데."'),
    ("나레이션", "사건의 진실을 밝혀낼 마지막 기회는 그렇게 지나갔다."),
]


# 진엔딩에서 확인하는 사건 전체 시간표
EVENT_TIMELINE = [
    "20:30 · 다인이 발표 자료 출력",
    "20:41 · 담당 교사가 시험지 출력, 한 장을 인쇄실에 남김",
    "21:07 · 혜린이 수행평가 자료 출력 중 남은 시험지 발견",
    "21:09 · 혜린이 시험지를 촬영",
    "00:17 · 혜린이 익명 게시판에 시험지 사진 게시",
    "00:20 · 혜린이 게시물을 삭제",
]


def show_lines(lines, line_key, location, skip_target=None):
    """기존 대화 UI를 이용해 한 줄씩 보여준다."""
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
            skip_changes={"chapter8_phase": skip_target},
        )

    if st.button(
        "다음 ▶",
        key=line_key + "_next",
        use_container_width=True
    ):
        st.session_state[line_key] += 1
        st.rerun()

    return False


def show_case_notes():
    """추리 중 기존 수사 기록을 다시 확인한다."""
    with st.expander("수사 기록 다시 보기"):
        name = st.selectbox(
            "확인할 기록",
            list(CASE_NOTES),
            key="chapter8_review_record"
        )
        st.write(CASE_NOTES[name])


def show_guess():
    """범인, 범행 장소, 결정적 증거를 순서대로 선택한다."""
    phase = st.session_state["chapter8_phase"]
    lives = st.session_state["chapter8_lives"]

    st.caption(f"남은 추리 기회: {lives} / {MAX_LIVES}")
    show_case_notes()

    # 첫 번째 질문 · 범인
    if phase == "suspect":
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 최종 추리",
            "나", '"시험지를 유출한 사람은 누구일까?"'
        )

        choice = choose_dialogue(
            SUSPECTS,
            key_prefix="chapter8_suspect_choice"
        )

        if choice is not None:
            st.session_state["chapter8_suspect"] = SUSPECTS[choice]
            st.session_state["chapter8_phase"] = "place"
            st.rerun()

        return

    # 두 번째 질문 · 사진 촬영 장소
    if phase == "place":
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 최종 추리",
            "나", '"시험지 사진은 어디에서 촬영되었을까?"'
        )

        choice = choose_dialogue(
            PLACES,
            key_prefix="chapter8_place_choice"
        )

        if choice is not None:
            st.session_state["chapter8_place"] = PLACES[choice]
            st.session_state["chapter8_phase"] = "evidence"
            st.rerun()

        return

    # 세 번째 질문 · 결정적 증거
    if phase == "evidence":
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 최종 추리",
            "나", '"범인과 사진 촬영을 가장 설득력 있게 연결하는 증거는 무엇일까?"'
        )

        choice = choose_dialogue(
            EVIDENCES,
            key_prefix="chapter8_evidence_choice"
        )

        if choice is not None:
            st.session_state["chapter8_evidence"] = EVIDENCES[choice]
            st.session_state["chapter8_phase"] = "confirm"
            st.rerun()

        return

    # 최종 확인 화면
    show_dialogue(
        CHAPTER, TITLE, "학교 본관 · 최종 추리",
        "나", '"이 추리로 사건의 진실을 밝힐 수 있을까?"'
    )

    with st.container(border=True):
        st.write("**지목한 사람:**", st.session_state["chapter8_suspect"])
        st.write("**사진 촬영 장소:**", st.session_state["chapter8_place"])
        st.write("**결정적 증거:**", st.session_state["chapter8_evidence"])

    # 답안 제출 및 기회 차감
    if st.button(
        "이 추리로 지목하기 ▶",
        key="chapter8_submit_guess",
        use_container_width=True
    ):
        correct = (
            st.session_state["chapter8_suspect"] == "혜린"
            and st.session_state["chapter8_place"] == "공용 인쇄실"
            and st.session_state["chapter8_evidence"] == EVIDENCES[1]
        )

        if correct:
            st.session_state["chapter8_phase"] = "true_ending"
        else:
            st.session_state["chapter8_lives"] -= 1

            if st.session_state["chapter8_lives"] == 0:
                st.session_state["chapter8_phase"] = "false_ending"
            else:
                st.session_state["chapter8_phase"] = "retry"

        st.rerun()

    # 제출 전에는 기회 차감 없이 답변 변경 가능
    if st.button(
        "선택 다시 하기",
        key="chapter8_change_guess",
        use_container_width=True
    ):
        st.session_state["chapter8_phase"] = "suspect"
        st.rerun()


def show_retry():
    """추리 실패 시 기록을 재열람한 뒤 다시 시도한다."""
    lives = st.session_state["chapter8_lives"]

    show_dialogue(
        CHAPTER, TITLE, "학교 본관 · 최종 추리",
        "나레이션", "증거를 다시 확인해야 한다. 아직 추리 기회가 남아 있다."
    )

    st.warning(f"추리 실패 · 남은 기회 {lives} / {MAX_LIVES}")

    show_case_notes()

    if st.button(
        "다시 추리하기 ▶",
        key="chapter8_retry_guess",
        use_container_width=True
    ):
        st.session_state["chapter8_phase"] = "suspect"
        st.rerun()


def reset_chapter8():
    """챕터 8의 진행 상태만 초기화한다."""
    for key in list(st.session_state.keys()):
        if key.startswith("chapter8_"):
            del st.session_state[key]

    st.rerun()


def show_finished(outcome):
    """엔딩별 완료 화면을 표시한다."""
    st.caption(CHAPTER)
    st.title(TITLE)

    if outcome == "true":
        st.subheader("진엔딩 · 밝혀진 진실")
        st.success("추리 성공! 시험 자료 유출 사건의 진실을 밝혀냈습니다.")

        for item in EVENT_TIMELINE:
            st.write("• " + item)

        st.write(
            "**사건의 결론:** 혜린이 공용 인쇄실에 남은 시험지를 촬영해 "
            "익명 게시판에 게시했다가 삭제했다."
        )

    elif outcome == "false":
        st.subheader("실패 엔딩 · 미해결 사건")
        st.error("세 번의 추리에 실패하여 사건을 해결하지 못했습니다.")
        st.write(
            "마지막 장면에서 혜린의 반응이 드러났지만, "
            "탐정은 사건을 밝혀내지 못했습니다."
        )

    else:
        st.subheader("사건 기록 요약")
        st.info(
            "스토리를 건너뛰었습니다. "
            "추리 결과는 아직 확정되지 않았습니다."
        )
        st.write(
            "주요 증거를 확인한 뒤 아래 버튼으로 "
            "직접 최종 추리에 도전할 수 있습니다."
        )

    # 엔딩 후에도 증거 열람 가능
    with st.container(border=True):
        st.markdown("**최종 수사 기록**")

        name = st.selectbox(
            "확인할 기록",
            list(CASE_NOTES),
            key="chapter8_finished_record"
        )

        st.write(CASE_NOTES[name])

    # 스킵한 경우 추리 화면으로 이동 가능
    if outcome == "skipped":
        if st.button(
            "최종 추리 시작하기 ▶",
            key="chapter8_start_after_skip",
            use_container_width=True
        ):
            st.session_state["chapter8_phase"] = "suspect"
            st.rerun()

    # 실패 엔딩에서만 다시 시작할 수 있다.
    if outcome == "false":
        if st.button(
            "챕터 8 처음부터 다시 하기 ↻",
            key="chapter8_restart",
            use_container_width=True
        ):
            reset_chapter8()

def show_chapter8():
    """마지막 면담부터 최종 추리와 분기 엔딩까지 관리한다."""
    if "chapter8_phase" not in st.session_state:
        st.session_state["chapter8_phase"] = "intro"

    if "chapter8_lives" not in st.session_state:
        st.session_state["chapter8_lives"] = MAX_LIVES

    phase = st.session_state["chapter8_phase"]

    # SCENE 01 · 도입
    if phase == "intro":
        if show_lines(
            INTRO_LINES,
            "chapter8_intro_line",
            "학교 본관 · 자료 열람실",
            skip_target="skipped"
        ):
            st.session_state["chapter8_phase"] = "interview"
            st.rerun()
        return

    # SCENE 02 · 혜린의 마지막 면담
    if phase == "interview":
        if play_questions(
            LAST_QUESTIONS,
            "chapter8_last_questions",
            CHAPTER,
            TITLE,
            "학교 본관 · 면담실"
        ):
            st.session_state["chapter8_phase"] = "verify"
            st.rerun()
        return

    # SCENE 03 · 실언 검증
    if phase == "verify":
        if show_lines(
            VERIFY_LINES,
            "chapter8_verify_line",
            "학교 본관 · 자료 열람실",
            skip_target="skipped"
        ):
            st.session_state["chapter8_phase"] = "suspect"
            st.rerun()
        return

    # SCENE 04 · 최종 추리
    if phase in ("suspect", "place", "evidence", "confirm"):
        show_guess()
        return

    # 오답 후 다시 도전
    if phase == "retry":
        show_retry()
        return

    # SCENE 05 · 추리 성공 엔딩
    if phase == "true_ending":
        if show_lines(
            TRUE_ENDING_LINES,
            "chapter8_true_line",
            "학교 본관 · 면담실",
            skip_target="finished_true"
        ):
            st.session_state["chapter8_phase"] = "finished_true"
            st.rerun()
        return

    # SCENE 06 · 추리 실패 엔딩
    if phase == "false_ending":
        if show_lines(
            FALSE_ENDING_LINES,
            "chapter8_false_line",
            "공용 인쇄실",
            skip_target="finished_false"
        ):
            st.session_state["chapter8_phase"] = "finished_false"
            st.rerun()
        return

    # 마지막 요약 화면
    if phase == "finished_true":
        show_finished("true")

    elif phase == "finished_false":
        show_finished("false")

    else:
        show_finished("skipped")

