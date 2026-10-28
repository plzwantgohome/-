                ("나", '"게시물을 올린 사람이 누구인지는 알아내지 못한 겁니까?"'),
                ("교장", '"그렇습니다. 게시물의 내용은 확인했지만, 작성자의 신원은 아직 밝혀지지 않았습니다."'),
                ("나", '"그렇다면 시험 자료를 어떤 경로로 입수했는지도 알 수 없겠군요."'),
                ("교장", '"네. 다만 조사에 도움이 될 만한 기록들을 정리해 두었습니다."'),
                ("나레이션", "교장은 책상 서랍에서 서류철 하나를 꺼내 내밀었다."),
                ("나레이션", "나는 교장에게서 서류철을 건네받았다. 겉표지에는 다음과 같은 글자가 적혀 있었다."),
                ("나레이션", "[시험 자료 유출 사건 관련 기록]"),
                ("나레이션", "서류철을 펼치자 사건에 관한 여러 기록이 눈에 들어왔다. 이제 본격적인 조사를 시작할 차례였다."),
            ],
        ),
    ]

    # 모든 장면의 대사를 순서대로 연결
    story = []
    for location, dialogues in scenes:
        for speaker, words in dialogues:
            story.append((location, speaker, words))

    # 기록 확인 후 이어지는 마지막 대사
    ending = [
        ("나레이션", "나는 서류철을 덮고 잠시 생각에 잠겼다."),
        ("나레이션", "학교 커뮤니티에 시험 문제가 올라온 사실은 확인되었다. 하지만 누가, 어떻게 시험 자료를 입수했는지는 여전히 의문이었다."),
        ("나레이션", "우선 사건과 관련된 학생들을 직접 만나 이야기를 들어 볼 필요가 있었다."),
        ("나", '"교장 선생님, 이 학생들과 직접 이야기를 나눌 수 있을까요?"'),
        ("교장", '"물론입니다. 조사에 필요한 협조는 최대한 제공하겠습니다."'),
        ("나레이션", "나는 수첩을 챙기고 자리에서 일어났다. 이제 본격적인 조사를 시작할 시간이었다."),
    ]

    # 기존 챕터 1 진행 기록과 충돌하지 않도록 처음 한 번 초기화
    if "chapter1_vn_initialized" not in st.session_state:
        st.session_state.chapter1_step = 0
        st.session_state.chapter1_vn_initialized = True

    step = st.session_state.chapter1_step

    # 1. 일반 스토리 화면
    if step < len(story):
        location, speaker, words = story[step]
        show_dialogue(location, speaker, words)

        if words == "나는 잠시 생각에 잠겼다.":
            button_text = "의뢰를 수락한다"
        elif step == len(story) - 1:
            button_text = "서류철 열어보기"
        else:
            button_text = "다음 →"

        if st.button(button_text, key="chapter1_next", use_container_width=True):
            st.session_state.chapter1_step += 1
            st.rerun()
        return

    # 2. 사건 기록 확인 화면 (기존 기능 유지)
    if step == len(story):
        st.caption("CHAPTER 01")
        st.title("낯선 의뢰")
        st.subheader("시험 자료 유출 사건 기록")
        st.write("교장에게 전달받은 서류철에는 사건과 관련된 자료가 정리되어 있었다.")
        st.write("나는 하나씩 내용을 확인하기 시작했다.")

        record = st.radio(
            "확인할 기록을 선택하세요.",
            ["사건 개요", "제보 내용", "관련 학생"],
            key="chapter1_record",
        )

        with st.container(border=True):
            if record == "사건 개요":
                st.subheader("사건 개요")
                st.markdown(
                    "**사건명:** 시험 자료 유출 사건\n\n"
                    "**발생 장소:** 둔산여자고등학교\n\n"
                    "**사건 내용:**\n\n"
                    "예정된 시험을 앞두고 학교 커뮤니티에 "
                    "시험 문제 일부가 게시되었다.\n\n"
                    "학교 측은 게시물의 내용이 실제 시험 문제와 "
                    "일치한다는 사실을 확인했다.\n\n"
                    "**현재 상황:**\n\n"
                    "해당 시험은 연기된 상태이며, "
                    "유출자의 신원과 자료의 입수 경로는 "
                    "아직 밝혀지지 않았다."
                )
            elif record == "제보 내용":
                st.subheader("제보 내용")
                st.markdown(
                    "**제보 접수:** 시험 실시 이전\n\n"
                    "**제보 내용:**\n\n"
                    "시험을 앞두고 학교 커뮤니티에 "
                    "시험 문제 일부가 게시되었다.\n\n"
                    "이를 발견한 학생들이 선생님께 알렸고, "
                    "학교 측이 실제 시험 문제와 대조한 결과 "
                    "일치하는 내용이 확인되었다.\n\n"
                    "이에 따라 학교는 시험을 연기했다.\n\n"
                    "**추가 확인 사항:**\n\n"
                    "게시물을 작성한 사람이 누구인지, "
                    "시험 자료를 어떤 경로로 입수했는지 "
                    "확인해야 한다.\n\n"
                    "또한 게시자와 최초 유출자가 "
                    "동일인인지도 조사할 필요가 있다."
                )
            else:
                st.subheader("관련 학생 명단")
                st.write("학교 측에서 우선적으로 면담이 필요하다고 정리한 학생들이다.")
                st.markdown("- 지현\n- 혜린\n- 예주\n- 유주\n- 다인")
                st.warning("현재까지 이 학생들이 사건에 가담했다는 사실이 확인된 것은 아니다.")

        if st.button("기록 확인을 마친다", key="chapter1_finish", use_container_width=True):
            st.session_state.chapter1_step += 1
            st.rerun()
        return

    # 3. 기록 확인 이후 화면
    ending_step = step - len(story) - 1
    if ending_step < len(ending):
        speaker, words = ending[ending_step]
        show_dialogue("학교 본관 · 교장실", speaker, words)

        if ending_step == len(ending) - 1:
            button_text = "CHAPTER 2로 이동 →"
        else:
            button_text = "다음 →"

        if st.button(button_text, key="chapter1_ending_next", use_container_width=True):
            if ending_step == len(ending) - 1:
                st.session_state["page"] = "chapter2"
            else:
                st.session_state.chapter1_step += 1
            st.rerun()
