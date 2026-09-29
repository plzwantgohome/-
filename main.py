import streamlit as st

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

</style>
""", unsafe_allow_html=True)


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
        st.session_state["page"] = "intro"
        st.rerun()


# =========================
# 아직 다음 화면을 만들지 않았을 때
# =========================

if st.session_state.get("page") == "intro":
    st.info("다음 단계에서 사건 도입 화면을 연결할 예정입니다.")


# =========================
# 하단 문구
# =========================

st.markdown("""
<div class="bottom-text">
CONFIDENTIAL · SCHOOL INVESTIGATION RECORD
