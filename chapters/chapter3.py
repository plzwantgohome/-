
import streamlit as st
from dialogue import choose_dialogue
from ui import show_dialogue


CHAPTER = "CHAPTER 03"
TITLE = "잠겨 있던 교무실"


# 챕터 2의 면담 직후 이어지는 장면
INTRO_LINES = [
    ("나레이션", "다섯 명의 면담이 끝났다. 나는 기록을 다시 펼쳐 보았다."),
    ("나레이션", "지현은 아홉 시 무렵 귀가했다고 했고, 예주는 늦은 저녁까지 방송실에 있었다고 말했다."),
    ("나", '"이제 기억이 아니라 실제 기록을 확인할 차례군."'),
    ("나레이션", "학교 측의 허락을 받아 교무실 주변 복도 영상과 출입 기록, 학생회 업무 자료를 살펴보기로 했다."),
    ("나레이션", "복도를 지나 교무실 앞에 도착했다. 문은 굳게 닫혀 있었다."),
    ("나", '"시험지가 이곳에 있었다면, 누가 이 방에 접근했는지부터 확인해야 해."'),
    ("나레이션", "나는 학교에서 전달받은 기록을 하나씩 확인하기로 했다."),
]


# 순서에 관계없이 조사할 수 있으며, 조사한 기록은 다시 열람할 수 있다.
RECORDS = {
    "학생회 업무 자료": {
        "location": "학교 본관 · 자료 열람실",
        "lines": [
            ("나레이션", "학생회실에서 작성한 행사 서류와 문서 수정 내역을 펼쳤다."),
            ("나레이션", "행사 서류는 실제로 작성되어 있었고, 마지막 수정 내역도 아홉 시 무렵에 남아 있었다."),
            ("나", '"학생회 일을 했다는 말은 사실인 것 같군."'),
            ("나레이션", "그런데 서류 한 장의 담당 교사 확인란이 비어 있었다."),
            ("나", '"이 서류를 처리하려고 다른 곳으로 이동했을 가능성도 있겠어. 하지만 아직은 추측일 뿐이야."'),
        ],
    },
    "2층 복도 CCTV": {
        "location": "학교 본관 · CCTV 열람실",
        "lines": [
            ("나레이션", "교무실이 있는 2층으로 이어지는 계단의 CCTV 영상을 재생했다."),
            ("나레이션", "화면 구석에 표시된 시각은 21시 18분이었다."),
            ("나레이션", "영상 속에서 지현이 계단을 올라 2층 복도로 향하는 모습이 보였다."),
            ("나", '"아홉 시쯤 바로 귀가했다고 했는데, 21시 18분에도 학교에 있었군."'),
            ("나레이션", "하지만 카메라는 계단 쪽을 비추고 있어 지현이 교무실 안으로 들어갔는지는 알 수 없었다."),
            ("나", '"진술과 어긋난 부분은 있다. 왜 2층으로 갔는지 직접 확인해야겠어."'),
        ],
    },
    "교무실 출입 기록": {
        "location": "학교 본관 · 교무실 앞",
        "lines": [
            ("나레이션", "학교 측이 보관 중인 교무실 출입 기록을 확인했다."),
            ("나레이션", "사건 당일 기록에는 다섯 학생이 교무실 문을 열고 들어갔다는 내역이 없었다."),
            ("나레이션", "사건이 알려진 뒤 확인한 교무실 문과 시험지 보관 서랍에도 훼손 흔적은 없었다."),
            ("나", '"지현이 2층에 올라온 건 사실이지만, 교무실에 들어갔다고 볼 증거는 없군."'),
            ("나레이션", "기록에 남지 않은 상황이 있었을 가능성까지 배제할 수는 없었다."),
        ],
    },
    "영상 저장 목록": {
        "location": "학교 본관 · CCTV 열람실",
        "lines": [
            ("나레이션", "다른 시간대의 CCTV 파일도 비교하던 중 이상한 부분을 발견했다."),
            ("나레이션", "22시 05분부터 22시 12분까지, 일부 영상 파일이 비어 있었다."),
            ("나", '"정확히 7분이 빠졌어. 단순 오류일까, 누군가 손을 댄 걸까?"'),
            ("나레이션", "예주는 방송실에서 영상 장비와 파일을 다루는 데 익숙하다고 말했다."),
            ("나", '"그렇다고 예주가 영상을 지웠다고 단정할 수는 없어. 저장 장치의 작동 기록도 확인해야 해."'),
        ],
    },
}


ENDING_LINES = [
    ("나레이션", "모든 기록을 확인한 뒤, 나는 면담 때 적어 둔 메모와 나란히 놓았다."),
    ("나", '"지현은 말한 귀가 시각보다 늦게까지 학교에 있었어. 하지만 교무실 출입은 확인되지 않았지."'),
    ("나", '"예주는 영상 장비에 익숙하고, 하필 일곱 분 동안 기록이 비어 있어."'),
    ("나레이션", "두 사람 모두 확인이 필요한 부분이 있었다. 그러나 아직 그 누구도 유출된 시험지와 직접 연결되지 않았다."),
    ("나", '"범인을 정하려면 더 확실한 증거가 필요해."'),
    ("나레이션", "나는 다시 사건 당일 익명 게시판에 올라왔던 시험지 사진을 떠올렸다."),
    ("나", '"사진 자체에도 아직 놓친 흔적이 있을지 몰라."'),
]


CASE_NOTES = {
    "학생회 업무 자료": "학생회 행사 서류는 실제로 작성됨. 아홉 시 무렵 수정 내역이 있으나 일부 교사 확인란은 비어 있음.",
    "2층 복도 CCTV": "21:18 지현이 2층으로 올라가는 장면 확인. 교무실 안으로 들어갔는지는 영상만으로 알 수 없음.",
    "교무실 출입 기록": "다섯 학생의 교무실 출입 내역은 확인되지 않음. 교무실 문과 시험지 보관 서랍에 훼손 흔적 없음.",
    "영상 저장 목록": "22:05~22:12 일부 CCTV 파일 공백. 원인 미확인. 예주가 영상 장비를 다룬다는 사실만으로 조작을 단정할 수 없음.",
}


def show_lines(lines, line_key, location):
    """기존 대화 UI로 문장을 한 줄씩 보여주고 종료 여부를 반환한다."""
    if line_key not in st.session_state:
        st.session_state[line_key] = 0

    index = st.session_state[line_key]
    if index >= len(lines):
        return True

    speaker, words = lines[index]
    show_dialogue(CHAPTER, TITLE, location, speaker, words)

    if st.button("다음 ▶", key=line_key + "_next", use_container_width=True):
        st.session_state[line_key] += 1
        st.rerun()

    return False


def show_records():
    """조사할 기록을 선택하고, 네 기록을 모두 확인하면 다음 장면으로 진행한다."""
    selected = st.session_state.get("chapter3_selected_record")
    checked = st.session_state["chapter3_checked_records"]

    if selected is None:
        show_dialogue(CHAPTER, TITLE, "학교 본관 · 자료 열람실", "나레이션", "어느 기록부터 조사할까?")
        st.caption(f"확인한 기록: {len(checked)} / {len(RECORDS)}")

        names = list(RECORDS)
        labels = [("✓ " if name in checked else "") + name for name in names]
        choice = choose_dialogue(labels, key_prefix="chapter3_record_choice")

        if choice is not None:
            st.session_state["chapter3_selected_record"] = names[choice]
            st.session_state["chapter3_record_line"] = 0
            st.rerun()

        if len(checked) == len(RECORDS):
            if st.button("조사 결과 정리하기 ▶", key="chapter3_to_ending", use_container_width=True):
                st.session_state["chapter3_phase"] = "ending"
                st.rerun()
        return

    # 이미 본 기록도 재선택하면 처음부터 다시 확인할 수 있다.
    record = RECORDS[selected]
    if show_lines(record["lines"], "chapter3_record_line", record["location"]):
        if selected not in checked:
            st.session_state["chapter3_checked_records"] = checked + [selected]
        st.session_state["chapter3_selected_record"] = None
        st.rerun()


def show_chapter3():
    if "chapter3_phase" not in st.session_state:
        st.session_state["chapter3_phase"] = "intro"
    if "chapter3_checked_records" not in st.session_state:
        st.session_state["chapter3_checked_records"] = []
    if "chapter3_selected_record" not in st.session_state:
        st.session_state["chapter3_selected_record"] = None

    phase = st.session_state["chapter3_phase"]

    if phase == "intro":
        if show_lines(INTRO_LINES, "chapter3_intro_line", "학교 본관 · 교무실 앞"):
            st.session_state["chapter3_phase"] = "records"
            st.rerun()
        return

    if phase == "records":
        show_records()
        return

    if phase == "ending":
        if show_lines(ENDING_LINES, "chapter3_ending_line", "학교 본관 · 자료 열람실"):
            st.session_state["chapter3_phase"] = "finished"
            st.rerun()
        return

    # 챕터 3을 마친 뒤 조사 내용을 다시 볼 수 있다.
    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")
    name = st.selectbox("확인할 기록", list(CASE_NOTES), key="chapter3_notes_record")
    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])
    st.info("챕터 3 조사를 완료했습니다. 챕터 4에서는 유출 사진 속 흔적을 살펴봅니다.")

    if st.button(
        "챕터 4로 ▶",
        key="chapter3_to_chapter4",
        use_container_width=True
    ):
        st.session_state["page"] = "chapter4"
        st.rerun()

