import streamlit as st


# 챕터 1: 학교의 의뢰
# main.py의 show_chapter1() 호출과 연결됩니다.

SCENES = {
    "arrival": [
        ("나레이션", "시험 자료가 유출된 다음 날 오후. 나는 학교의 의뢰를 받고 본관에 도착했다."),
        ("나레이션", "복도는 평소처럼 학생들로 붐볐지만 교무실 앞 분위기는 달랐다."),
        ("학교 관계자", "와 주셔서 감사합니다. 이쪽 회의실로 안내하겠습니다."),
        ("조사관", "먼저 지금까지 확인된 사실을 듣겠습니다."),
    ],
    "briefing": [
        ("학교 관계자", "어젯밤 0시 17분, 학교 익명 게시판에 중간고사 시험지 사진이 올라왔습니다."),
        ("학교 관계자", "게시물은 0시 20분에 삭제됐지만 화면을 저장한 학생들이 있었습니다."),
        ("조사관", "사진이 실제 시험지와 일치합니까?"),
        ("학교 관계자", "네. 시험지의 내용과 배치가 일치했습니다."),
        ("학교 관계자", "하지만 보관 서랍은 잠겨 있었고 교무실에 침입 흔적도 없었습니다."),
        ("학교 관계자", "시험 자료가 저장된 컴퓨터에서도 수상한 접근 기록은 확인되지 않았고요."),
        ("조사관", "그렇다고 시험지가 다른 장소에서 노출되지 않았다는 뜻은 아니겠군요."),
        ("학교 관계자", "맞습니다. 그래서 유출 경위를 조사해 주셨으면 합니다."),
        ("학교 관계자", "당일 교무실과 인쇄실 주변에서 활동한 학생 다섯 명의 면담을 준비했습니다."),
        ("조사관", "명단에 있다는 이유만으로 관련자라고 단정하지는 않겠습니다."),
        ("학교 관계자", "물론입니다. 학생들에게 면담 목적을 알리고 동의를 받겠습니다."),
        ("조사관", "그전에 사건 자료부터 확인하겠습니다."),
    ],
    "closing": [
        ("나레이션", "사건 보고서, 보관 현황, 면담 대상자 명단을 차례로 읽었다."),
        ("조사관", "지금 확인된 것은 시험지 사진이 게시되었다는 사실뿐입니다."),
        ("조사관", "누가 어디에서 그 사진을 얻었는지부터 확인해야겠군요."),
        ("학교 관계자", "면담에 동의한 학생들이 별도 교실에서 기다리고 있습니다."),
        ("나레이션", "나는 자료를 정리하고 회의실을 나섰다."),
        ("나레이션", "교실 문 너머로 학생들의 작은 목소리가 들려왔다."),
        ("조사관", "그럼 한 명씩 이야기를 들어보겠습니다."),
    ],
}

RECORDS = {
    "사건 개요 보고서": [
        "게시 시각: 00:17 / 삭제 시각: 00:20",
        "게시 장소: 학교 익명 게시판",
        "게시된 사진은 실제 중간고사 시험지 일부와 일치함",
        "삭제 전 저장된 게시물 화면이 남아 있음",
    ],
    "시험 자료 보관 현황": [
        "교무실 시험지 보관 서랍은 잠금 상태였음",
        "교무실 침입 흔적은 현재까지 확인되지 않음",
        "시험 자료 저장 컴퓨터에서 비정상 접근 기록이 확인되지 않음",
        "유출 경로가 없었다는 뜻은 아니므로 추가 조사가 필요함",
    ],
    "우선 면담 대상자": [
        "지현: 야간 자율학습 후 교무실 주변 복도를 지남",
        "혜린: 수행평가 자료를 준비하며 학교에 남아 있었음",
        "예주: 동아리 자료를 정리하고 귀가함",
        "유주: 방과 후 교내에서 다른 학생을 기다림",
        "다인: 발표 자료를 출력하기 위해 인쇄실을 이용함",
        "이들은 우선 면담 대상자이며 범인으로 확정된 것이 아님",
    ],
}


def initialize():
    if "chapter1_new_phase" not in st.session_state:
        st.session_state["chapter1_new_phase"] = "arrival"
    if "chapter1_new_line" not in st.session_state:
        st.session_state["chapter1_new_line"] = 0
    if "chapter1_new_document" not in st.session_state:
        st.session_state["chapter1_new_document"] = None
    if "chapter1_new_read" not in st.session_state:
        st.session_state["chapter1_new_read"] = []


def change_phase(phase):
    st.session_state["chapter1_new_phase"] = phase
    st.session_state["chapter1_new_line"] = 0
    st.rerun()


def display_scene(phase, next_phase, location):
    st.caption("CHAPTER 01 · 학교의 의뢰")
    st.subheader(location)

    line = st.session_state["chapter1_new_line"]
    speaker, words = SCENES[phase][line]

    with st.container(border=True):
        st.markdown("**" + speaker + "**")
        st.write(words)

    if line + 1 < len(SCENES[phase]):
        if st.button("다음 ▶", key="chapter1_next", use_container_width=True):
            st.session_state["chapter1_new_line"] += 1
            st.rerun()
    else:
        if st.button("계속 진행 ▶", key="chapter1_continue", use_container_width=True):
