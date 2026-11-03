        )

    if st.button("다음 ▶", key=line_key + "_next", use_container_width=True):
        st.session_state[line_key] += 1
        st.rerun()

    return False


def show_records():
    """네 가지 기록을 자유롭게 조사하고, 모두 확인하면 순서 맞추기로 이동한다."""
    selected = st.session_state["chapter5_selected_record"]
    checked = st.session_state["chapter5_checked_records"]

    if selected is None:
        show_dialogue(CHAPTER, TITLE, "공용 인쇄실 · 기록 조사", "나레이션", "어떤 기록부터 확인할까?")
        st.caption(f"확인한 기록: {len(checked)} / {len(RECORDS)}")
        names = list(RECORDS)
        labels = [("✓ " if name in checked else "") + name for name in names]
        choice = choose_dialogue(labels, key_prefix="chapter5_record_choice")

        if choice is not None:
            st.session_state["chapter5_selected_record"] = names[choice]
            st.session_state["chapter5_record_line"] = 0
            st.rerun()

        if len(checked) == len(RECORDS):
            if st.button("기록의 순서 정리하기 ▶", key="chapter5_to_timeline", use_container_width=True):
                st.session_state["chapter5_phase"] = "timeline"
                st.rerun()
        return

    record = RECORDS[selected]
    if show_lines(record["lines"], "chapter5_record_line", record["location"]):
        if selected not in checked:
            st.session_state["chapter5_checked_records"] = checked + [selected]
        st.session_state["chapter5_selected_record"] = None
        st.rerun()


def show_timeline():
    """출력 기록에 나타난 세 계정의 사용 순서를 확인한다."""
    show_dialogue(
        CHAPTER, TITLE, "공용 인쇄실 · 사건 기록",
        "나", '"세 건의 출력 기록을 시간순으로 놓으면 어떤 순서가 될까?"'
    )

    options = [
        "다인 → 시험 담당 교사 → 혜린",
        "시험 담당 교사 → 다인 → 혜린",
        "혜린 → 다인 → 시험 담당 교사",
    ]
    choice = choose_dialogue(options, key_prefix="chapter5_timeline_choice")

    if choice is not None:
        if choice == 0:
            st.session_state["chapter5_phase"] = "ending"
        else:
            st.session_state["chapter5_wrong_order"] = True
        st.rerun()

    if st.session_state["chapter5_wrong_order"]:
        st.warning("출력 시각을 다시 확인해 보자. 기록 목록으로 돌아가 다시 열람할 수 있다.")

    if st.button("출력 기록 다시 보기", key="chapter5_back_to_records", use_container_width=True):
        st.session_state["chapter5_phase"] = "records"
        st.rerun()


def show_chapter5():
    """챕터 5의 장면 전환을 관리한다."""
    if "chapter5_phase" not in st.session_state:
        st.session_state["chapter5_phase"] = "intro"
    if "chapter5_checked_records" not in st.session_state:
        st.session_state["chapter5_checked_records"] = []
    if "chapter5_selected_record" not in st.session_state:
        st.session_state["chapter5_selected_record"] = None
    if "chapter5_wrong_order" not in st.session_state:
        st.session_state["chapter5_wrong_order"] = False

    phase = st.session_state["chapter5_phase"]

    if phase == "intro":
        if show_lines(INTRO_LINES, "chapter5_intro_line", "공용 인쇄실", skip_target="records"):
            st.session_state["chapter5_phase"] = "records"
            st.rerun()
        return

    if phase == "records":
        show_records()
        return

    if phase == "timeline":
        show_timeline()
        return

    if phase == "ending":
        if show_lines(ENDING_LINES, "chapter5_ending_line", "학교 본관 · 자료 열람실", skip_target="finished"):
            st.session_state["chapter5_phase"] = "finished"
            st.rerun()
        return

    # 챕터를 마친 뒤에도 조사 요약은 자유롭게 다시 열람할 수 있다.
    st.caption(CHAPTER)
    st.title(TITLE)
    st.subheader("조사 기록 정리")
    name = st.selectbox("확인할 기록", list(CASE_NOTES), key="chapter5_notes_record")
    with st.container(border=True):
        st.markdown("**" + name + "**")
        st.write(CASE_NOTES[name])
    st.info("챕터 5 조사를 완료했습니다. 다음은 프린터 기록과 학생들의 증언을 대조할 차례입니다.")
