    .c1-end {background:#101010;border:1px solid #383838;border-radius:9px;
        padding:75px 25px;text-align:center;color:#eee;}
    .c1-end-small {color:#888;letter-spacing:4px;font-size:12px;margin-bottom:19px;}
    .c1-end-title {font-size:31px;font-weight:800;margin-bottom:16px;}
    .c1-end-text {font-size:14px;color:#aaa;line-height:2;}
    </style>
    """)


def show_stage(location):
    st.html(f"""
    <div class="c1-wrap">
        <div class="c1-heading">CHAPTER 01 · 학교의 의뢰</div>
        <div class="c1-stage">
            <div class="c1-window"></div>
            <div class="c1-board"></div>
            <div class="c1-desk"></div>
            <div class="c1-location">{escape(location)}</div>
        </div>
    </div>
    """)


def show_dialogue(speaker, words):
    st.html(f"""
    <div class="c1-wrap">
        <div class="c1-dialogue">
            <div class="c1-speaker">{escape(speaker)}</div>
            <div class="c1-words">{escape(words)}</div>
        </div>
    </div>
    """)


def play_dialogues(lines, next_phase, location):
    show_stage(location)
    index = st.session_state["c1_v2_line"]
    speaker, words = lines[index]
    show_dialogue(speaker, words)

    if index < len(lines) - 1:
        if st.button("다음  ▶", key="c1_next", use_container_width=True):
            st.session_state["c1_v2_line"] += 1
            st.rerun()
    else:
        if st.button("계속 진행  ▶", key="c1_continue", use_container_width=True):
            move_to(next_phase)


# ==========================================
# 조사 자료 열람 (클릭 상호작용)
# ==========================================

def show_records():
    st.html("""
    <div class="c1-wrap">
        <div class="c1-heading">CHAPTER 01 · 학교의 의뢰</div>
        <div class="c1-record-heading">사건 자료 열람</div>
        <div class="c1-record-caption">학교 측이 제출한 자료입니다. 원하는 문서를 눌러 내용을 확인하세요.</div>
    </div>
    """)

    for index, title in enumerate(RECORDS, 1):
        checked = title in st.session_state["c1_v2_checked"]
        label = f"✓  {title}" if checked else f"{index:02d}  {title}"
        if st.button(label, key=f"c1_record_{index}", use_container_width=True):
            st.session_state["c1_v2_selected"] = title
            if not checked:
                st.session_state["c1_v2_checked"].append(title)
            st.rerun()

    selected = st.session_state["c1_v2_selected"]
    if selected:
        items = "".join(
            f'<div class="c1-paper-item">{escape(item)}</div>'
            for item in RECORDS[selected]
        )
        st.html(f"""
        <div class="c1-wrap">
            <div class="c1-paper">
                <div class="c1-paper-title">{escape(selected)}</div>
                {items}
            </div>
        </div>
        """)

    if len(st.session_state["c1_v2_checked"]) == len(RECORDS):
        if st.button("자료 확인 완료  ▶", key="c1_records_done", use_container_width=True):
            move_to("closing")
    else:
        st.info("세 가지 자료를 모두 확인하면 다음 장면으로 진행할 수 있습니다.")


# ==========================================
# 챕터 1 엔딩 (챕터 2는 연결하지 않음)
# ==========================================

def show_ending():
    st.session_state["c1_v2_complete"] = True
    st.html("""
    <div class="c1-wrap">
        <div class="c1-end">
            <div class="c1-end-small">CHAPTER 01 COMPLETE</div>
            <div class="c1-end-title">학교의 의뢰</div>
            <div class="c1-end-text">
                사건 자료 확인 완료<br>
                다음 조사: 다섯 명의 증언<br><br>
                TO BE CONTINUED
            </div>
        </div>
    </div>
    """)
    st.caption("챕터 2는 아직 연결하지 않았습니다.")


# ==========================================
# main.py에서 호출하는 함수
# ==========================================

def show_chapter1():
    init_chapter1()
    chapter1_style()

    phase = st.session_state["c1_v2_phase"]

    if phase == "arrival":
        play_dialogues(ARRIVAL, "briefing", "학교 본관 · 복도")
    elif phase == "briefing":
