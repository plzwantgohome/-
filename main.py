import streamlit as st
from textwrap import dedent


# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="시험 자료 유출 사건",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# 화면 상태 설정
# =========================

# 처음 접속하면 타이틀 화면
if "page" not in st.session_state:
    st.session_state["page"] = "title"

# 프롤로그에서 현재 몇 번째 장면인지 저장
if "prologue_step" not in st.session_state:
    st.session_state["prologue_step"] = 0


# =========================
# CSS
# =========================
st.markdown("""
<style>

/* 전체 화면 */
.stApp {
    background:
        radial-gradient(
            circle at center,
            #171717 0%,
            #0b0b0b 45%,
            #000000 100%
        );
    color: white;
}

/* 상단 기본 여백 줄이기 */
.block-container {
    padding-top: 3rem;
    max-width: 1100px;
}

/* Streamlit 기본 메뉴 숨기기 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================
   타이틀 영역
   ========================= */

.title-wrap {
    text-align: center;
    margin-top: 8vh;
}

.case-number {
    color: #777777;
    font-size: 13px;
    letter-spacing: 7px;
    margin-bottom: 25px;
}

.main-title {
    font-size: 68px;
    font-weight: 800;
    letter-spacing: -3px;
    margin: 0;
    color: #f5f5f5;
    text-shadow:
        0 0 20px rgba(255,255,255,0.05);
}

.red-line {
    width: 45px;
    height: 2px;
    background: #9e2424;
    margin: 28px auto;
}

.subtitle {
    color: #8c8c8c;
    font-size: 17px;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.description {
    color: #5f5f5f;
    font-size: 13px;
    letter-spacing: 1px;
    margin-top: 18px;
}


/* =========================
   사건 파일 장식
   ========================= */

.case-file {
    width: 530px;
    max-width: 90%;
    margin: 55px auto 35px auto;

    padding: 10px 24px;

    background: rgba(20, 20, 20, 0.75);

    border: 1px solid #292929;
    border-left: 3px solid #7b1f1f;

    border-radius: 5px;

    color: #777777;

    font-size: 13px;
    letter-spacing: 1px;

    text-align: left;
}

.case-file strong {
    color: #b8b8b8;
    font-weight: 500;
}


/* =========================
   버튼
   ========================= */

div.stButton {
    text-align: center;
}

div.stButton > button {

    width: 240px;
    height: 55px;

    background: #0d0d0d;

    color: #dcdcdc;

    border: 1px solid #444444;

    border-radius: 3px;

    font-size: 15px;
    font-weight: 500;

    letter-spacing: 3px;

    transition: 0.25s;
}

div.stButton > button:hover {

    background: #171717;

    color: white;

    border-color: #8c2929;

    box-shadow:
        0 0 20px rgba(140, 41, 41, 0.13);

    transform: translateY(-1px);
}

div.stButton > button:active {
    transform: translateY(1px);
}


/* 하단 문구 */
.bottom-text {
    margin-top: 70px;

    text-align: center;

    color: #333333;

    font-size: 11px;

    letter-spacing: 3px;
}


/* =========================
   프롤로그 전체
   ========================= */

.prologue-wrap {
    max-width: 900px;
    margin: 35px auto 0 auto;
}


/* =========================
   어두운 장면
   ========================= */

.scene-dark {
    min-height: 430px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    padding: 50px;

    background:
        radial-gradient(
            circle at center,
            #202020 0%,
            #101010 55%,
            #050505 100%
        );

    border: 1px solid #222222;
    border-radius: 10px;

    color: white;
    text-align: center;
}

.scene-small {
    color: #777777;
    font-size: 13px;
    letter-spacing: 3px;
    margin-bottom: 20px;
}

.scene-text {
    font-size: 20px;
    line-height: 2;
    font-weight: 400;
}

.scene-time {
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 3px;

    margin-bottom: 18px;

    color: #ffffff;
}


/* =========================
   익명 게시판
   ========================= */

.phone-area {
    min-height: 430px;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 40px 20px;

    background-color: #0b0b0b;

    border: 1px solid #222222;
    border-radius: 10px;
}

.phone {
    width: 340px;

    padding: 18px;

    border: 1px solid #333333;
    border-radius: 18px;

    background-color: #181818;
    color: #eeeeee;
}

.phone-header {
    display: flex;
    justify-content: space-between;

    padding-bottom: 13px;
    margin-bottom: 16px;

    border-bottom: 1px solid #333333;

    font-size: 13px;
    color: #888888;
}

.post-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 9px;
}

.post-meta {
    font-size: 12px;
    color: #777777;
    margin-bottom: 18px;
}


/* =========================
   시험지 사진
   ========================= */

.exam-photo {
    border: 1px solid #444444;
    border-radius: 5px;

    background-color: #eeeeee;

    padding: 18px;

    color: #222222;

    transform: rotate(-1deg);
}

.exam-head {
    text-align: center;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 15px;
}

.exam-line {
    height: 7px;

    margin: 9px 0;

    border-radius: 5px;

    background-color: #aaaaaa;
}

.exam-line.short {
    width: 63%;
}

.exam-line.middle {
    width: 82%;
}


/* =========================
   댓글
   ========================= */

.comment {
    padding: 11px 4px;

    border-bottom: 1px solid #292929;

    font-size: 13px;
    line-height: 1.5;
}

.comment-time {
    color: #666666;
    font-size: 11px;
    margin-left: 5px;
}


/* =========================
   삭제된 게시물
   ========================= */

.deleted {
    padding: 90px 20px;

    color: #777777;

    text-align: center;
    font-size: 14px;
}


/* =========================
   다음 날 학교
   ========================= */

.school-scene {
    min-height: 430px;

    position: relative;

    display: flex;
    align-items: flex-end;

    padding: 35px;

    border: 1px solid #222222;
    border-radius: 10px;

    background:
        linear-gradient(
            rgba(0, 0, 0, 0.18),
            rgba(0, 0, 0, 0.35)
        ),
        linear-gradient(
            135deg,
            #c4c4c4,
            #eeeeee
        );
}

.dialogue-box {
    width: 100%;

    padding: 20px 24px;

    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 7px;

    background-color: rgba(10,10,10,0.93);

    color: white;
}

.dialogue-name {
    margin-bottom: 7px;

    color: #999999;

    font-size: 12px;
    font-weight: 700;
}

.dialogue-text {
    font-size: 16px;
    line-height: 1.8;
}


/* =========================
   CASE 시작 화면
   ========================= */

.case-screen {
    min-height: 430px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    border: 1px solid #222222;
    border-radius: 10px;

    background-color: #050505;

    text-align: center;
    color: white;
}

.case-start-number {
    color: #666666;

    font-size: 13px;
    letter-spacing: 5px;

    margin-bottom: 13px;
}

.case-start-title {
    font-size: 38px;
    font-weight: 800;

    letter-spacing: -1px;

    margin-bottom: 13px;
}

.case-start-description {
    color: #999999;

    font-size: 14px;
    line-height: 1.8;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)



# =========================================================
# 타이틀 화면
# =========================================================

if st.session_state["page"] == "title":

    # =========================
    # 타이틀
    # =========================

    st.markdown("""
<div class="title-wrap">
<div class="case-number">CASE FILE 01</div>
<div class="main-title">시험 자료 유출 사건</div>
<div class="red-line"></div>
<div class="subtitle">삭제된 파일과 다섯 명의 용의자</div>
<div class="description">진술과 기록 속 모순을 찾아 사건의 진실을 밝혀내라.</div>
</div>
""", unsafe_allow_html=True)


    # =========================
    # 사건 파일 느낌 장식
    # =========================

    st.markdown("""
<div class="case-file">
<strong>사건 분류</strong>
&nbsp;&nbsp; 교내 시험 자료 유출 의혹

<br><br>

<strong>용의자</strong>
&nbsp;&nbsp; 5명
</div>
""", unsafe_allow_html=True)


    # =========================
    # 시작 버튼
    # =========================

    col1, col2, col3 = st.columns([1, 0.8, 1])

    with col2:
        if st.button("조사 시작"):
            st.session_state["page"] = "prologue"
            st.session_state["prologue_step"] = 0
            st.rerun()


    # =========================
    # 하단 문구
    # =========================

    st.markdown("""
<div class="bottom-text">
CONFIDENTIAL · SCHOOL INVESTIGATION RECORD
</div>
""", unsafe_allow_html=True)



# =========================================================
# 프롤로그
# =========================================================

elif st.session_state["page"] == "prologue":

    step = st.session_state["prologue_step"]


    # =====================================================
    # SCENE 1
    # 시험 전날 밤
    # =====================================================

    if step == 0:

        st.html("""
<div class="prologue-wrap">
    <div class="scene-dark">
        <div class="scene-small">PROLOGUE</div>

        <div class="scene-text">
            중간고사를 하루 앞둔 밤.<br><br>
            늦은 시간까지 불이 켜져 있던 학교도<br>
            어느새 조용해져 있었다.
        </div>
    </div>
</div>
""")

        if st.button(
            "다음  ▶",
            use_container_width=True,
            key="prologue_0"
        ):
            st.session_state["prologue_step"] = 1
            st.rerun()


    # =====================================================
    # SCENE 2
    # 00:17 게시물
    # =====================================================

    elif step == 1:

        st.html("""
<div class="prologue-wrap">
    <div class="phone-area">
        <div>
            <div class="scene-time" style="text-align:center;">
                00:17
            </div>

            <div class="phone">
                <div class="phone-header">
                    <span>학교 익명 게시판</span>
                    <span>00:17</span>
                </div>

                <div class="post-title">
                    내일 시험, 미리 보고 싶은 사람?
                </div>

                <div class="post-meta">
                    익명 · 방금 전
                </div>

                <div class="exam-photo">
                    <div class="exam-head">
                        2학년 중간고사
                    </div>

                    <div class="exam-line"></div>
                    <div class="exam-line middle"></div>
                    <div class="exam-line"></div>
                    <div class="exam-line short"></div>
                    <div class="exam-line middle"></div>
                </div>
            </div>
        </div>
    </div>
</div>
""")

        if st.button(
            "게시물을 확인한다  ▶",
            use_container_width=True,
            key="prologue_1"
        ):
            st.session_state["prologue_step"] = 2
            st.rerun()


    # =====================================================
    # SCENE 3
    # 댓글
    # =====================================================

    elif step == 2:

        st.html("""
<div class="prologue-wrap">
    <div class="phone-area">
        <div class="phone">

            <div class="phone-header">
                <span>학교 익명 게시판</span>
                <span>00:19</span>
            </div>

            <div class="post-title">
                내일 시험, 미리 보고 싶은 사람?
            </div>

            <div class="comment">
                익명1
                <span class="comment-time">00:18</span>
                <br>
                이거 진짜야?
            </div>

            <div class="comment">
                익명2
                <span class="comment-time">00:18</span>
                <br>
                잠깐만 이거 내일 시험 아니야?
            </div>

            <div class="comment">
                익명3
                <span class="comment-time">00:19</span>
                <br>
                누가 이런 걸 올림?
            </div>

            <div class="comment">
                익명4
                <span class="comment-time">00:19</span>
                <br>
                일단 저장함
            </div>

        </div>
    </div>
</div>
""")

        if st.button(
            "다음  ▶",
            use_container_width=True,
            key="prologue_2"
        ):
            st.session_state["prologue_step"] = 3
            st.rerun()


    # =====================================================
    # SCENE 4
    # 게시물 삭제
    # =====================================================

    elif step == 3:

        st.html("""
<div class="prologue-wrap">
    <div class="phone-area">
        <div>

            <div class="scene-time" style="text-align:center;">
                00:20
            </div>

            <div class="phone">

                <div class="phone-header">
                    <span>학교 익명 게시판</span>
                    <span>00:20</span>
                </div>

                <div class="deleted">
                    삭제된 게시물입니다.
                </div>

            </div>
        </div>
    </div>
</div>
""")

        if st.button(
            "다음 날  ▶",
            use_container_width=True,
            key="prologue_3"
        ):
            st.session_state["prologue_step"] = 4
            st.rerun()


    # =====================================================
    # SCENE 5
    # 다음 날 학교
    # =====================================================

    elif step == 4:

        st.html("""
<div class="prologue-wrap">
    <div class="school-scene">

        <div class="dialogue-box">

            <div class="dialogue-name">
                학생들의 대화
            </div>

            <div class="dialogue-text">
                “야, 어제 게시판에 올라온 거 봤어?”<br><br>
                “그 사진 진짜 시험 문제래.”<br><br>
                “그래서 오늘 시험 미뤄진다던데.”
            </div>

        </div>

    </div>
</div>
""")

        if st.button(
            "계속 듣는다  ▶",
            use_container_width=True,
            key="prologue_4"
        ):
            st.session_state["prologue_step"] = 5
            st.rerun()


    # =====================================================
    # SCENE 6
    # 사건의 이상점
    # =====================================================

    elif step == 5:

        st.html("""
<div class="prologue-wrap">
    <div class="scene-dark">

        <div class="scene-text">
            사진에 찍힌 것은<br>
            실제 시험에 사용될 예정이었던 원본이었다.<br><br>

            하지만 교무실의 문에는<br>
            침입한 흔적이 없었다.<br><br>

            시험지를 보관한 서랍도 잠겨 있었다.<br><br>

            컴퓨터에서도<br>
            수상한 접근 기록은 발견되지 않았다.
        </div>

    </div>
</div>
""")

        if st.button(
            "사건을 확인한다  ▶",
            use_container_width=True,
            key="prologue_5"
        ):
            st.session_state["prologue_step"] = 6
            st.rerun()


    # =====================================================
    # SCENE 7
    # CASE START
    # =====================================================

    elif step == 6:

        st.html("""
<div class="prologue-wrap">
    <div class="case-screen">

        <div class="case-start-number">
            CASE 00:17
        </div>

        <div class="case-start-title">
            유출된 시험지
        </div>

        <div class="case-start-description">
            다섯 명의 증언과 기록 속에서<br>
            사건의 진실을 찾아내십시오.
        </div>

    </div>
</div>
""")

        if st.button(
            "CHAPTER 1 시작",
            use_container_width=True,
            key="start_chapter_1"
        ):
            st.session_state["page"] = "chapter1"
            st.rerun()
