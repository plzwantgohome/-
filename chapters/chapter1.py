
import streamlit as st


# ==========================================
# CHAPTER 1. 기본 설정
# ==========================================

def init_chapter1():
    if "chapter1_scene" not in st.session_state:
        st.session_state["chapter1_scene"] = 0

    if "chapter1_dialogue" not in st.session_state:
        st.session_state["chapter1_dialogue"] = 0

    if "chapter1_evidence" not in st.session_state:
        st.session_state["chapter1_evidence"] = []

    if "chapter1_interviewed" not in st.session_state:
        st.session_state["chapter1_interviewed"] = []

    if "chapter1_target" not in st.session_state:
        st.session_state["chapter1_target"] = None


def add_evidence(evidence):
    if evidence not in st.session_state["chapter1_evidence"]:
        st.session_state["chapter1_evidence"].append(evidence)


def next_scene():
    st.session_state["chapter1_scene"] += 1
    st.session_state["chapter1_dialogue"] = 0
    st.rerun()


# ==========================================
# CHAPTER 1. 스토리 데이터
# ==========================================

STORY = [
    # SCENE 0
    [
        ("나레이션", "오전 8시 12분. 평소와 다를 것 없는 아침이었다."),
        ("나레이션", "교실에는 시험 범위를 확인하는 학생들의 목소리와 책장 넘기는 소리가 뒤섞여 있었다."),
        ("나레이션", "적어도, 담임 선생님이 들어오기 전까지는."),
        ("나레이션", "드르륵. 교실 앞문이 열렸다."),
        ("담임", "다들 공부 멈추고 잠깐 앞을 봐."),
        ("나레이션", "선생님의 표정은 평소보다 훨씬 굳어 있었다."),
        ("담임", "어젯밤, 이번 시험 자료의 일부가 외부로 유출됐다는 사실이 확인됐다."),
        ("나레이션", "순간 교실이 조용해졌다."),
        ("학생", "네? 시험지가 유출됐다고요?"),
        ("담임", "아직 정확한 경위는 조사 중이야. 확인되지 않은 이야기는 퍼뜨리지 마."),
        ("나레이션", "나는 책상 위에 펼쳐 둔 문제집을 천천히 덮었다."),
        ("주인공", "시험 자료가 유출됐다고...?"),
    ],

    # SCENE 1
    [
        ("나레이션", "잠시 후, 학생들 사이에서 작은 목소리들이 오가기 시작했다."),
        ("지현", "잠깐만. 그럼 우리 시험은 어떻게 되는 거야?"),
        ("예주", "누가 그런 짓을 했는지는 알아?"),
        ("유주", "어제 학교에 늦게 남아 있던 사람부터 확인해야 하는 거 아니야?"),
        ("다인", "근데 학교에 남아 있었다고 다 의심하는 건 좀 그렇지 않아?"),
        ("혜린", "일단 정확히 뭐가 유출됐는지부터 알아야지."),
        ("나레이션", "혜린은 차분하게 말한 뒤 다시 자신의 책상으로 시선을 돌렸다."),
        ("나레이션", "누군가는 화를 냈고, 누군가는 불안해했으며, 누군가는 지나치게 조용했다."),
        ("주인공", "반응만으로 누군가를 의심할 수는 없어."),
        ("주인공", "직접 확인할 수 있는 정보부터 모아 보자."),
    ],

    # SCENE 2
    [
        ("나레이션", "쉬는 시간이 되자 교실 안의 소란은 더욱 커졌다."),
        ("나레이션", "나는 어젯밤 학교에 남아 있었다는 다섯 명의 이야기를 들어 보기로 했다."),
        ("주인공", "누군가 거짓말을 하고 있을지도 몰라."),
        ("나레이션", "하지만 지금은 누구도 범인이라고 단정할 수 없다."),
    ],

    # SCENE 4
    [
        ("나레이션", "다섯 명의 이야기를 모두 들었다."),
        ("나레이션", "각자의 말에는 조금씩 다른 정보가 담겨 있었다."),
        ("나레이션", "나는 조사 기록을 다시 펼쳤다."),
        ("주인공", "어젯밤 인쇄실에 누가 있었는지 확인해야 해."),
        ("주인공", "그리고 실제로 유출된 자료가 무엇인지도."),
        ("나레이션", "그때, 교실 앞에서 새로운 이야기가 들려왔다."),
        ("학생", "선생님이 인쇄실 기록을 확인하고 계신대."),
        ("나레이션", "나는 급히 자리에서 일어났다."),
        ("주인공", "인쇄실 기록이라면 시간을 확인할 수 있겠어."),
        ("나레이션", "사건의 진실은 아직 모습을 드러내지 않았다."),
        ("나레이션", "하지만 이제, 조사해야 할 방향은 분명해졌다."),
    ],
]


# ==========================================
# CHAPTER 1. 인물 조사 데이터
# ==========================================

SUSPECTS = {
    "지현": {
        "dialogue": [
            ("주인공", "지현아, 어제 학교에 몇 시까지 있었어?"),
            ("지현", "8시 조금 넘어서 나갔어. 시험 공부 때문에 남아 있었거든."),
            ("주인공", "그때 뭔가 이상한 일은 없었어?"),
            ("지현", "글쎄... 딱히? 복도에 사람이 몇 명 있긴 했어."),
            ("지현", "근데 누가 있었는지는 정확히 기억 안 나."),
        ],
        "evidence": "지현의 진술: 오후 8시 조금 넘어 귀가했다고 주장함."
    },

    "혜린": {
        "dialogue": [
            ("주인공", "혜린아, 어제 늦게까지 학교에 있었지?"),
            ("혜린", "응. 수행평가 자료 때문에."),
            ("주인공", "몇 시쯤 나갔어?"),
            ("혜린", "정확히는 모르겠는데, 9시쯤이었을걸?"),
            ("주인공", "그동안 계속 교실에 있었어?"),
            ("혜린", "아니. 출력할 게 있어서 잠깐 인쇄실에도 갔어."),
            ("혜린", "근데 왜? 나 의심하는 거야?"),
            ("주인공", "아니, 그냥 확인하는 거야."),
        ],
        "evidence": "혜린의 진술: 오후 9시 무렵 귀가했으며 인쇄실에 들렀다고 말함."
    },

    "예주": {
        "dialogue": [
            ("주인공", "예주야, 어제 학교에서 뭐 했어?"),
            ("예주", "동아리 자료 정리했어. 거의 끝나서 바로 집에 갔고."),
            ("주인공", "몇 시쯤?"),
            ("예주", "8시 반쯤이었던 것 같아."),
            ("예주", "아, 그런데 복도에서 프린터 돌아가는 소리가 들렸어."),
            ("주인공", "누가 사용했는지는 봤어?"),
            ("예주", "아니. 소리만 들었어."),
        ],
        "evidence": "예주의 진술: 오후 8시 30분 무렵 복도에서 프린터 소리를 들었다고 함."
    },

    "유주": {
        "dialogue": [
            ("주인공", "유주야, 어제 학교에 남아 있었어?"),
            ("유주", "응. 친구 기다리느라 조금 늦었어."),
            ("주인공", "혹시 인쇄실 근처에도 갔어?"),
            ("유주", "지나가긴 했는데 안으로 들어가지는 않았어."),
            ("유주", "근데 그쪽에서 누가 나오는 것 같긴 했어."),
            ("주인공", "누군지 확인했어?"),
            ("유주", "아니, 멀리서 봐서 잘 모르겠어."),
        ],
        "evidence": "유주의 진술: 인쇄실 근처에서 누군가 나오는 모습을 멀리서 봤다고 함."
    },

    "다인": {
        "dialogue": [
            ("주인공", "다인아, 너도 어제 인쇄실에 갔다고 했지?"),
            ("다인", "응. 발표 자료 출력하러 갔어."),
            ("주인공", "언제쯤?"),
            ("다인", "8시 반쯤이었어. 출력하고 바로 나왔지."),
            ("주인공", "특별한 건 없었어?"),
            ("다인", "내가 갔을 때는 그냥 평소랑 똑같았어."),
            ("다인", "아, 프린터 옆에 종이가 좀 쌓여 있었던 것 같기도 해."),
        ],
        "evidence": "다인의 진술: 오후 8시 30분 무렵 인쇄실에서 발표 자료를 출력했다고 함."
    },
}


# ==========================================
# CHAPTER 1. 화면 디자인
# ==========================================

def chapter1_style():
    st.markdown("""
    <style>
    .chapter-title {
        text-align: center;
        color: #eeeeee;
        font-size: 29px;
        font-weight: 700;
        letter-spacing: 2px;
        margin: 25px 0 8px 0;
    }

    .chapter-subtitle {
        text-align: center;
        color: #888888;
        font-size: 13px;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }

    .story-box {
        background: #171717;
        border: 1px solid #383838;
        border-radius: 12px;
        padding: 25px 27px;
        min-height: 160px;
        margin: 15px 0;
    }

    .story-name {
        color: #dddddd;
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    .story-text {
        color: #cccccc;
        font-size: 16px;
        line-height: 2;
        white-space: pre-wrap;
        overflow-wrap: anywhere;
    }

    .investigation-title {
        color: #eeeeee;
        font-size: 19px;
        font-weight: 700;
        margin: 20px 0;
    }

    .evidence-box {
        background: #141414;
        border: 1px solid #363636;
        border-radius: 10px;
        padding: 18px;
        margin: 10px 0;
        color: #cccccc;
        line-height: 1.8;
    }

    .chapter-note {
        color: #888888;
        text-align: center;
        font-size: 13px;
        margin: 12px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def show_dialogue(name, text):
    # HTML 태그가 대사에 들어가도 그대로 표시하도록 처리
    from html import escape

    st.markdown(f"""
    <div class="story-box">
        <div class="story-name">{escape(name)}</div>
        <div class="story-text">{escape(text)}</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# CHAPTER 1. 소설 진행
# ==========================================

def play_story(story_index):
    dialogues = STORY[story_index]
    current = st.session_state["chapter1_dialogue"]

    name, text = dialogues[current]
    show_dialogue(name, text)

    st.caption(f"{current + 1} / {len(dialogues)}")

    if current < len(dialogues) - 1:
        if st.button("다음 ▶", key=f"story_next_{story_index}"):
            st.session_state["chapter1_dialogue"] += 1
            st.rerun()
    else:
        if st.button("계속 진행 ▶", key=f"story_end_{story_index}"):
            next_scene()


# ==========================================
# CHAPTER 1. 자유 조사
# ==========================================

def investigate():
    st.markdown(
        '<div class="investigation-title">인물 조사</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="chapter-note">대화할 인물을 선택하세요.</div>',
        unsafe_allow_html=True
    )

    target = st.session_state["chapter1_target"]

    if target is None:
        names = list(SUSPECTS.keys())

        for name in names:
            checked = name in st.session_state["chapter1_interviewed"]
            label = f"✓ {name} - 조사 완료" if checked else f"{name} - 대화하기"

            if st.button(label, key=f"suspect_{name}", use_container_width=True):
                st.session_state["chapter1_target"] = name
                st.session_state["chapter1_dialogue"] = 0
                st.rerun()

        st.divider()

        count = len(st.session_state["chapter1_interviewed"])
        st.caption(f"조사 완료: {count} / 5명")

        if count == 5:
            st.success("모든 인물의 조사가 완료되었습니다.")

            if st.button("조사 기록 확인 ▶", use_container_width=True):
                next_scene()
        else:
            st.info("다섯 명 모두와 대화해야 다음 장면으로 진행할 수 있습니다.")

    else:
        dialogues = SUSPECTS[target]["dialogue"]
        current = st.session_state["chapter1_dialogue"]

        name, text = dialogues[current]
        show_dialogue(name, text)

        st.caption(f"{current + 1} / {len(dialogues)}")

        if current < len(dialogues) - 1:
            if st.button("다음 ▶", key="interview_next"):
                st.session_state["chapter1_dialogue"] += 1
                st.rerun()

        else:
            if st.button("대화 종료 및 기록 저장", use_container_width=True):
                add_evidence(SUSPECTS[target]["evidence"])

                if target not in st.session_state["chapter1_interviewed"]:
                    st.session_state["chapter1_interviewed"].append(target)

                st.session_state["chapter1_target"] = None
                st.session_state["chapter1_dialogue"] = 0
                st.rerun()


# ==========================================
# CHAPTER 1. 수집한 단서 확인
# ==========================================

def show_evidence():
    st.markdown(
        '<div class="investigation-title">조사 기록</div>',
        unsafe_allow_html=True
    )

    for index, evidence in enumerate(st.session_state["chapter1_evidence"], 1):
        from html import escape
        st.markdown(
            f'<div class="evidence-box">기록 {index:02d}<hr>{escape(evidence)}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="chapter-note">모든 진술이 사실인지는 아직 확인되지 않았습니다.</div>',
        unsafe_allow_html=True
    )

    if st.button("기록 정리 완료 ▶", use_container_width=True):
        next_scene()


# ==========================================
# CHAPTER 1. 마지막 장면
# ==========================================

def chapter1_ending():
    st.markdown(
        '<div class="chapter-subtitle">CHAPTER 1 COMPLETE</div>',
        unsafe_allow_html=True
    )

    show_dialogue(
        "나레이션",
        "다섯 명의 진술을 확보했다.\n"
        "하지만 진술만으로는 사건의 진실에 도달할 수 없다.\n\n"
        "다음으로 확인해야 할 것은 인쇄실의 기록이다."
    )

    st.info("챕터 1이 완료되었습니다. 다음 챕터에서는 인쇄실 기록을 조사합니다.")

    # 챕터 2가 완성되기 전까지는 여기서 종료합니다.
    # 나중에 chapter2.py를 만든 뒤 이동 버튼을 연결할 예정입니다.


# ==========================================
# CHAPTER 1. 메인 함수
# ==========================================

def show_chapter1():
    init_chapter1()
    chapter1_style()

    st.markdown(
        '<div class="chapter-title">CHAPTER 1</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="chapter-subtitle">사라진 시험 자료</div>',
        unsafe_allow_html=True
    )

    scene = st.session_state["chapter1_scene"]

    if scene == 0:
        play_story(0)

    elif scene == 1:
        play_story(1)

    elif scene == 2:
        play_story(2)

    elif scene == 3:
        investigate()

    elif scene == 4:
        show_evidence()

    elif scene == 5:
        play_story(3)

    elif scene == 6:
        chapter1_ending()
