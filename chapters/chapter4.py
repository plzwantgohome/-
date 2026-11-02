
import streamlit as st
from dialogue import choose_dialogue
from ui import show_dialogue


CHAPTER = "CHAPTER 04"
TITLE = "사진 속 흔적"


# 챕터 3에서 조사 기록을 확인한 직후의 이야기
INTRO_LINES = [
    ("나레이션", "교무실 주변 기록을 모두 확인했지만, 시험지를 가져간 사람은 밝혀지지 않았다."),
    ("나레이션", "지현의 이동 시각과 CCTV의 공백은 수상했지만, 그 자체로 시험지 유출을 설명하지는 못했다."),
    ("나", '"놓친 게 있다면, 사건이 처음 알려진 순간에 남아 있겠지."'),
    ("나레이션", "나는 학교가 확보해 둔 익명 게시판의 캡처 화면을 다시 열었다."),
    ("나레이션", "게시글은 0시 17분에 올라왔고, 약 3분 뒤 삭제되었다."),
    ("나레이션", "화면에는 실제 시험지 일부가 찍힌 사진이 그대로 남아 있었다."),
    ("나", '"문제 내용만 보지 말고, 사진에 함께 찍힌 것들도 살펴보자."'),
]


# 캡처 화면에서 살펴볼 부분
PHOTO_DETAILS = {
    "시험지가 찍힌 부분": [
        ("나레이션", "사진 중앙에는 실제 시험지의 일부가 놓여 있었다."),
        ("나레이션", "종이는 책상 위에 펼쳐져 있고, 종이의 한쪽 끝이 사진 밖으로 잘려 있었다."),
        ("나", '"시험지가 사진에 찍혔다는 건 확실하지만, 이것만으로 촬영 장소를 알 수는 없어."'),
    ],
    "책상 모서리": [
        ("나레이션", "사진의 오른쪽 아래를 자세히 살펴보았다."),
        ("나레이션", "책상 모서리에 작은 파란 별 모양 스티커가 붙어 있었다."),
        ("나레이션", "스티커 한쪽이 조금 들떠 있었고, 주변 책상 표면에는 얕은 긁힌 자국이 보였다."),
        ("나", '"이런 표시가 있는 책상을 찾는다면 장소를 좁힐 수 있겠군."'),
    ],
    "사진의 배경": [
        ("나레이션", "시험지 뒤쪽에는 회색 장비의 일부가 흐릿하게 찍혀 있었다."),
        ("나레이션", "전체 모습은 보이지 않았지만, 종이를 다루는 장비처럼 보였다."),
        ("나", '"프린터일 수도 있겠어. 그렇지만 사진만 보고 단정하지 말자."'),
    ],
}


# 플레이어가 직접 확인할 장소
LOCATIONS = {
    "교무실": [
        ("나레이션", "학교 측의 허락을 받아 교무실 안쪽 책상을 살펴보았다."),
        ("나레이션", "여러 책상과 서류 보관함이 있었지만, 사진 속 파란 별 스티커는 발견되지 않았다."),
        ("나", '"지금 확인한 범위에서는 사진의 배경과 일치하는 자리가 없군."'),
    ],
    "학생회실": [
        ("나레이션", "학생회실에는 행사 서류와 문구류가 놓여 있었다."),
        ("나레이션", "책상 모서리들을 살펴보았지만 파란 별 스티커는 보이지 않았다."),
        ("나", '"학생회 업무 기록과는 별개로, 이곳이 사진의 촬영 장소라는 근거는 없어."'),
    ],
    "방송실": [
        ("나레이션", "방송실에는 모니터와 영상 장비가 나란히 놓여 있었다."),
        ("나레이션", "회색 장비는 있었지만, 사진 속 책상 모서리와 일치하는 흔적은 찾지 못했다."),
        ("나", '"예주가 장비를 다룬다는 사실만으로 이 사진과 연결할 수는 없지."'),
    ],
    "공용 인쇄실": [
        ("나레이션", "마지막으로 2층 공용 인쇄실에 들어섰다."),
        ("나레이션", "프린터 옆 책상을 살피던 순간, 익숙한 모양이 눈에 들어왔다."),
        ("나레이션", "책상 모서리에 작은 파란 별 스티커가 붙어 있었다."),
        ("나레이션", "스티커가 들뜬 방향과 옆의 긁힌 자국도 캡처 화면 속 모습과 같았다."),
        ("나", '"찾았다. 사진 속 책상이 이곳의 책상일 가능성이 높아."'),
        ("나레이션", "책상 바로 옆에는 사진 배경의 장비와 비슷한 회색 프린터가 놓여 있었다."),
        ("나", '"그렇다면 시험지가 교무실 밖으로 나와 있었을 수도 있다는 뜻이야."'),
    ],
}


ENDING_LINES = [
    ("나레이션", "나는 공용 인쇄실의 책상과 캡처 화면을 번갈아 확인했다."),
    ("나", '"같은 스티커에 긁힌 자국까지 일치해. 유출 사진은 이곳에서 찍혔을 가능성이 크군."'),
    ("나레이션", "그동안 나는 누군가 교무실에서 시험지를 빼냈을 가능성에만 집중하고 있었다."),
    ("나", '"하지만 시험지가 이미 인쇄실에 놓여 있었다면 이야기가 달라져."'),
    ("나레이션", "물론 아직 누가 사진을 찍었는지, 시험지가 왜 그곳에 있었는지는 알 수 없었다."),
    ("나", '"공용 프린터를 누가, 언제 사용했는지 확인해야겠어."'),
    ("나레이션", "나는 학교 측에 인쇄실 프린터의 출력 기록을 요청했다."),
    ("나레이션", "다음 조사의 시작점은 교무실 출입 기록이 아니라 프린터 사용 기록이었다."),
]


# 챕터 완료 후 다시 읽을 수 있는 핵심 정보
CASE_NOTES = {
    "유출 게시글": "0시 17분에 게시된 뒤 약 3분 만에 삭제됨. 학교가 확보한 캡처 화면을 확인함.",
    "사진 속 특징": "책상 모서리의 파란 별 스티커, 스티커 옆 긁힌 자국, 배경의 회색 장비가 확인됨.",
    "장소 조사 결과": "공용 인쇄실 책상의 스티커와 긁힌 자국이 사진 속 특징과 일치함. 촬영 장소로 유력함.",
    "아직 밝혀지지 않은 점": "시험지가 인쇄실에 있었던 이유, 촬영자, 프린터 사용 시각은 아직 확인되지 않음.",
}


def show_lines(lines, line_key, location):
    """대사를 한 줄씩 보여주고, 전부 확인했으면 True를 반환한다."""
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


def show_photo_investigation():
    """사진의 세 부분을 원하는 순서로 조사한다."""
    selected = st.session_state["chapter4_selected_photo"]
    checked = st.session_state["chapter4_checked_photo"]

    if selected is None:
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 자료 열람실",
            "나레이션", "캡처 화면에서 어느 부분을 살펴볼까?"
        )
        st.caption(f"확인한 부분: {len(checked)} / {len(PHOTO_DETAILS)}")

        names = list(PHOTO_DETAILS)
        labels = [("✓ " if name in checked else "") + name for name in names]
        choice = choose_dialogue(labels, key_prefix="chapter4_photo_choice")

        if choice is not None:
            st.session_state["chapter4_selected_photo"] = names[choice]
            st.session_state["chapter4_photo_line"] = 0
            st.rerun()

        if len(checked) == len(PHOTO_DETAILS):
            if st.button(
                "촬영 장소 찾아보기 ▶",
                key="chapter4_to_locations",
                use_container_width=True
            ):
                st.session_state["chapter4_phase"] = "locations"
                st.rerun()
        return

    if show_lines(
        PHOTO_DETAILS[selected],
        "chapter4_photo_line",
        "학교 본관 · 자료 열람실"
    ):
        if selected not in checked:
            st.session_state["chapter4_checked_photo"] = checked + [selected]
        st.session_state["chapter4_selected_photo"] = None
        st.rerun()


def show_location_investigation():
    """학교의 장소들을 조사하고 사진 속 특징과 일치하는 장소를 찾는다."""
    selected = st.session_state["chapter4_selected_location"]
    checked = st.session_state["chapter4_checked_locations"]

    if selected is None:
        show_dialogue(
            CHAPTER, TITLE, "학교 본관 · 복도",
            "나레이션", "사진 속 책상을 어디에서 찾아볼까?"
        )
        st.caption(f"방문한 장소: {len(checked)} / {len(LOCATIONS)}")

        names = list(LOCATIONS)
        labels = [("✓ " if name in checked else "") + name for name in names]
        choice = choose_dialogue(labels, key_prefix="chapter4_location_choice")

        if choice is not None:
            st.session_state["chapter4_selected_location"] = names[choice]
            st.session_state["chapter4_location_line"] = 0
            st.rerun()
        return

    if show_lines(
        LOCATIONS[selected],
        "chapter4_location_line",
        "학교 본관 · " + selected
    ):
        if selected not in checked:
            st.session_state["chapter4_checked_locations"] = checked + [selected]
        st.session_state["chapter4_selected_location"] = None

        # 올바른 장소를 찾으면 마지막 장면으로 넘어간다.
        if selected == "공용 인쇄실":
            st.session_state["chapter4_phase"] = "ending"
        st.rerun()


def show_chapter4():
    """챕터 4의 진행 상태를 관리한다."""
    if "chapter4_phase" not in st.session_state:
        st.session_state["chapter4_phase"] = "intro"
    if "chapter4_selected_photo" not in st.session_state:
        st.session_state["chapter4_selected_photo"] = None
    if "chapter4_checked_photo" not in st.session_state:
        st.session_state["chapter4_checked_photo"] = []
    if "chapter4_selected_location" not in st.session_state:
        st.session_state["chapter4_selected_location"] = None
    if "chapter4_checked_locations" not in st.session_state:
        st.session_state["chapter4_checked_locations"] = []

    phase = st.session_state["chapter4_phase"]

    if phase == "intro":
        if show_lines(
            INTRO_LINES,
            "chapter4_intro_line",
            "학교 본관 · 자료 열람실"
        ):
            st.session_state["chapter4_phase"] = "photo"
            st.rerun()
        return

    if phase == "photo":
        show_photo_investigation()
        return

    if phase == "locations":
        show_location_investigation()
        return

    if phase == "ending":
        if show_lines(
            ENDING_LINES,
            "chapter4_ending_line",
            "학교 본관 · 공용 인쇄실"
        ):
            st.session_state["chapter4_phase"] = "finished"
            st.rerun()
        return

    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")

    name = st.selectbox(
        "확인할 기록",
        list(CASE_NOTES),
        key="chapter4_notes_record"
    )
    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])

    st.info(
        "챕터 4 조사를 완료했습니다. "
        "다음 챕터에서는 공용 프린터 사용 기록을 확인합니다."
    )
