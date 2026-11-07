
import streamlit as st

from chapters.chapter2 import SCENES, INTERVIEW_NOTES
from chapters.chapter3 import CASE_NOTES as NOTES3
from chapters.chapter5 import CASE_NOTES as NOTES5
from chapters.chapter6 import CASE_NOTES as NOTES6
from chapters.chapter7 import CASE_NOTES as NOTES7


st.set_page_config(
    page_title="추리 노트",
    page_icon="📓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================
# 추리 노트 기록 관리
# =========================

records = []
timeline = []


def add(chapter, kind, title, content):
    records.append((chapter, kind, title, content))


def add_time(order, clock, content):
    timeline.append((order, clock, content))


# =========================
# 프롤로그 기록
# =========================

if st.session_state.get("prologue_step", 0) >= 4:
    add(
        0,
        "증거",
        "익명 게시판 게시글",
        "00:17에 시험지 일부가 담긴 사진이 게시되었으며, "
        "약 3분 뒤 삭제되었다. 작성자는 확인되지 않았다."
    )

    add_time(90, "00:17", "시험지 사진 게시 [게시물]")
    add_time(100, "00:20", "게시글 삭제 [게시물]")


# =========================
# 챕터 2 · 인물 증언
# =========================

seen = st.session_state.get("chapter2_vn_index", 0)

scene_end = {}
line_count = 0

for scene_name, lines in SCENES:
    line_count += len(lines)

    for person in INTERVIEW_NOTES:
        if person in scene_name:
            scene_end[person] = line_count

for person, note in INTERVIEW_NOTES.items():
    if seen >= scene_end.get(person, line_count) and seen > 0:
        add(2, "증언", f"{person}의 첫 면담", note)


# =========================
# 챕터 3 · 사건 기록
# =========================

for title in st.session_state.get("chapter3_checked_records", []):
    if title in NOTES3:
        add(3, "증거", title, NOTES3[title])

    if title == "2층 복도 CCTV":
        add_time(
            50, "21:18",
            "지현이 2층으로 올라가는 모습 확인 [CCTV]"
        )

    if title == "영상 저장 목록":
        add_time(
            70, "22:05~22:12",
            "CCTV 영상 일부 공백 발견 [저장 목록]"
        )


# =========================
# 챕터 4 · 사진 및 장소 조사
# =========================

photo_notes = {
    "시험지가 찍힌 부분":
        "공개된 사진 중앙에 실제 시험지 일부가 찍혀 있다. "
        "촬영 장소는 아직 알 수 없다.",

    "책상 모서리":
        "사진 속 책상 모서리에 파란 별 스티커와 "
        "얕은 긁힌 자국이 보인다.",

    "사진의 배경":
        "시험지 뒤쪽에 회색 장비의 일부가 보인다. "
        "프린터일 가능성이 있으나 확정되지 않았다.",
}

location_notes = {
    "교무실":
        "교무실 책상에서 사진 속 파란 별 스티커를 찾지 못했다.",

    "학생회실":
        "학생회실에서는 사진과 일치하는 스티커가 발견되지 않았다.",

    "방송실":
        "장비는 있었지만 사진 속 책상과 일치하는 "
        "흔적은 확인되지 않았다.",

    "공용 인쇄실":
        "공용 인쇄실 책상의 파란 별 스티커와 긁힌 자국이 "
        "유출 사진 속 모습과 일치한다. "
        "촬영 장소일 가능성이 높다.",
}

for title in st.session_state.get("chapter4_checked_photo", []):
    if title in photo_notes:
        add(4, "증거", f"사진 조사 · {title}", photo_notes[title])

for title in st.session_state.get("chapter4_checked_locations", []):
    if title in location_notes:
        add(4, "증거", f"장소 조사 · {title}", location_notes[title])


# =========================
# 챕터 5 · 프린터 기록
# =========================

printer_notes = {
    "다인": (
        "다인 출력 기록",
        10, "20:30",
        "다인 계정으로 발표 자료 출력 [기록]"
    ),
    "담당 교사": (
        "시험지 출력 기록",
        20, "20:41",
        "담당 교사 계정으로 시험지 출력 [기록]"
    ),
    "혜린": (
        "혜린 출력 기록",
        30, "21:07",
        "혜린 계정으로 발표 자료 출력 [기록]"
    ),
}

for person in st.session_state.get("chapter5_checked_records", []):
    if person in printer_notes:
        title, order, clock, event = printer_notes[person]

        add(5, "증거", title, NOTES5[title])
        add_time(order, clock, event)

if st.session_state.get("chapter5_phase") in ("ending", "finished"):
    add(
        5, "증언",
        "시험 담당 교사 확인",
        NOTES5["시험 담당 교사 확인"]
    )


# =========================
# 챕터 6 · 증언과 기록 대조
# =========================

compare_notes = {
    "혜린의 첫 면담": "혜린의 첫 진술",
    "다인과 유주의 증언": "다인·유주의 증언",
    "프린터 사용 기록": "프린터 사용 기록",
}

for title in st.session_state.get("chapter6_checked_records", []):
    if title in compare_notes:
        note_title = compare_notes[title]

        kind = "증거" if title == "프린터 사용 기록" else "증언"

        add(6, kind, note_title, NOTES6[note_title])

if st.session_state.get("chapter6_phase") in ("ending", "finished"):
    add(
        6, "증언",
        "혜린의 재면담",
        NOTES6["혜린의 재면담"]
    )


# =========================
# 챕터 7 · 추가 조사
# =========================

for person in st.session_state.get("chapter7_checked_people", []):
    if person == "지현":
        add(
            7, "증거",
            "지현의 이동 재검증",
            NOTES7["지현의 이동"]
        )

        add_time(60, "21:27", "지현의 귀가 모습 확인 [CCTV]")

    elif person == "예주":
        add(
            7, "증거",
            "예주의 CCTV 의혹 재검증",
            NOTES7["예주의 CCTV 의혹"]
        )

        add(
            7, "증언",
            "예주의 목격담",
            NOTES7["예주의 목격담"]
        )

if (
    st.session_state.get("chapter7_photo_line", 0) >= 5
    or st.session_state.get("chapter7_phase") in ("ending", "finished")
):
    add(
        7, "증거",
        "유출 사진의 촬영 시각",
        NOTES7["유출 사진의 촬영 시각"]
    )

    add_time(
        40, "21:09",
        "유출 사진의 촬영 시각 정보 확인 [이미지 사본]"
    )


# =========================
# 챕터 8 · 마지막 증거
# =========================

if st.session_state.get("chapter8_verify_line", 0) >= 5:
    add(
        8, "증거",
        "공개되지 않은 시험지 정보",
        "혜린은 공개된 사진에 없는 마지막 문제의 그래프를 "
        "언급했다. 담당 교사는 실제로 해당 문제가 존재하며 "
        "유출 사진에는 나오지 않는다고 확인했다."
    )


# =========================
# 추리 노트 화면
# =========================

st.caption("CASE FILE 01 · INVESTIGATION RECORD")
st.title("📓 추리 노트")

st.write(
    "조사 과정에서 확인한 증언과 증거를 "
    "모아 두는 기록장이다."
)

st.caption(f"현재 확보한 기록: {len(records)}개")

st.page_link("main.py", label="◀ 조사로 돌아가기")

st.divider()


# =========================
# 기록 분류
# =========================

tab_people, tab_evidence, tab_time, tab_memo = st.tabs(
    ["인물 증언", "물적 증거", "사건 시간표", "나의 추리"]
)


def show_records(kind):
    chosen = [r for r in records if r[1] == kind]

    if not chosen:
        st.info("아직 확인한 기록이 없습니다.")
        return

    for chapter, _, title, content in chosen:
        with st.container(border=True):
            if chapter == 0:
                st.caption("PROLOGUE")
            else:
                st.caption(f"CHAPTER {chapter:02d}")

            st.markdown(f"**{title}**")
            st.markdown(content)


with tab_people:
    show_records("증언")


with tab_evidence:
    show_records("증거")


# =========================
# 사건 시간표
# =========================

with tab_time:
    if not timeline:
        st.info("아직 시간 정보가 없습니다.")

    else:
        for _, clock, detail in sorted(timeline):
            st.write(f"**{clock}** · {detail}")

    st.caption(
        "확인된 기록과 인물의 진술을 구분해서 살펴보세요. "
        "00시대 기록은 다음 날 새벽의 사건입니다."
    )


# =========================
# 플레이어 개인 메모
# =========================

with tab_memo:
    st.write("수사 중 떠오른 의문이나 추측을 자유롭게 적어 보세요.")

    if "detective_memo" not in st.session_state:
        st.session_state["detective_memo"] = ""

    memo = st.text_area(
        "개인 추리 메모",
        value=st.session_state["detective_memo"],
        height=220,
        key="detective_memo_editor"
    )

    if st.button("메모 저장", use_container_width=True):
        st.session_state["detective_memo"] = memo
        st.success("메모를 저장했습니다.")

