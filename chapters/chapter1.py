
import streamlit as st


def show_chapter1():

    # 챕터 1 스토리
    story = [
        (
            "늦은 오후, 조용한 탐정 사무소에 전화벨이 울렸다.\n\n"
            "평소와 다를 것 없는 하루였다.\n"
            "책상 위에는 정리되지 않은 서류들이 쌓여 있었다.\n\n"
            "나는 수화기를 집어 들었다."
        ),

        (
            '**???** : "안녕하십니까. 혹시 탐정 사무소가 맞습니까?"\n\n'
            '**나** : "네, 맞습니다. 무슨 일이시죠?"'
        ),

        (
            '**???** : "저는 둔산여자고등학교의 교장입니다. '
            '다름이 아니라... 학교에서 조금 곤란한 일이 발생했습니다."\n\n'
            '**교장** : "최근 교내 시험 자료가 외부로 유출되었다는 '
            '의혹이 제기되었습니다."'
        ),

        (
            '**나** : "시험 자료 유출이라... '
            '학교 내부에서 조사하면 되는 일 아닙니까?"\n\n'
            '**교장** : "그게 그렇게 간단하지 않습니다. '
            '관련된 사람이 학생인지, 교직원인지조차 '
            '알 수 없는 상황입니다."'
        ),

        (
            '**교장** : "현재로서는 외부에 알려지지 않도록 '
            '사실관계를 확인하고 싶습니다."\n\n'
            '**교장** : "혹시 직접 학교에 방문해 '
            '조사해 주실 수 있겠습니까?"\n\n'
            '나는 잠시 생각에 잠겼다.'
        )
    ]

    # 현재 대화 위치 저장
    if "chapter1_step" not in st.session_state:
        st.session_state.chapter1_step = 0

    # 챕터 제목
    st.caption("CHAPTER 01")
    st.title("낯선 의뢰")
    st.divider()

    # 스토리 출력
    step = st.session_state.chapter1_step

    with st.container(border=True):

        if step < len(story):
            st.markdown(story[step])

        else:
            st.markdown(
                '**나** : "알겠습니다. 내일 학교로 찾아가겠습니다."\n\n'
                '**교장** : "감사합니다. '
                '자세한 사항은 학교에서 말씀드리겠습니다."\n\n'
                '전화가 끊겼다.\n\n'
                '나는 수첩을 펼쳐 학교의 이름을 적었다.\n\n'
                '둔산여자고등학교... 평범한 시험 자료 유출 사건일까.\n'
                '아니면 그 뒤에 무언가 더 숨겨져 있을까.'
            )

    # 버튼
    if step < len(story):

        if step == len(story) - 1:
            button_text = "의뢰를 수락한다"
        else:
            button_text = "다음 →"

        if st.button(button_text, use_container_width=True):
            st.session_state.chapter1_step += 1
            st.rerun()

    else:
        st.caption("다음 장면 : 학교 방문")

        if st.button("처음부터 보기", use_container_width=True):
            st.session_state.chapter1_step = 0
            st.rerun()

    # 스토리 출력
    step = st.session_state.chapter1_step

    if step < len(story):

        with st.container(border=True):
            st.markdown(story[step])

        if step == 4:
            button_text = "의뢰를 수락한다"

        elif step == len(story) - 1:
            button_text = "서류철 열어보기"

        else:
            button_text = "다음 →"

        if st.button(button_text, use_container_width=True):
            st.session_state.chapter1_step += 1
            st.rerun()

    # 사건 기록 확인
    elif step == len(story):

        st.subheader("시험 자료 유출 사건 기록")

        st.write(
            "교장에게 전달받은 서류철에는 "
            "사건과 관련된 자료가 정리되어 있었다."
        )

        st.write("나는 하나씩 내용을 확인하기 시작했다.")

        record = st.radio(
            "확인할 기록을 선택하세요.",
            ["사건 개요", "제보 내용", "관련 학생"]
        )

        with st.container(border=True):

            if record == "사건 개요":

                st.subheader("사건 개요")

                st.markdown("""
                **사건명:** 시험 자료 유출 의혹 사건

                **발생 장소:** 둔산여자고등학교

                **사건 내용:**

                최근 실시된 시험에서 일부 학생들이
                시험 문제를 사전에 알고 있었다는
                의혹이 제기되었다.

                학교 측은 시험 자료가 외부로
                유출되었을 가능성을 조사하고 있다.

                **현재 상황:**

                유출 여부와 경로는 아직 확인되지 않았다.
                """)

            elif record == "제보 내용":

                st.subheader("제보 내용")

                st.markdown("""
                **제보 접수:** 시험 종료 이후

                **제보 내용:**

                일부 학생들이 시험 전에
                출제된 문제의 내용을 알고 있었다는
                제보가 학교 측에 접수되었다.

                학교에서는 단순히 예상 문제가
                적중했을 가능성도 검토했으나,
                다른 정황도 확인할 필요가 있다고 판단했다.

                **추가 확인 사항:**

                실제 시험 자료에 접근한 사람이 있는지,
                학생들에게 문제가 어떻게 알려졌는지
                조사해야 한다.
                """)

            elif record == "관련 학생":

                st.subheader("관련 학생 명단")

                st.write(
                    "학교 측에서 우선적으로 "
                    "면담이 필요하다고 정리한 학생들이다."
                )

                st.markdown("""
                - 지현
                - 혜린
                - 예주
                - 유주
                - 다인
                """)

                st.warning(
                    "현재까지 이 학생들이 사건에 "
                    "가담했다는 사실이 확인된 것은 아니다."
                )

        if st.button("기록 확인을 마친다", use_container_width=True):
            st.session_state.chapter1_step += 1
            st.rerun()

    # 기록 확인 이후
    else:

        with st.container(border=True):

            st.markdown("""
            나는 서류철을 덮고 잠시 생각에 잠겼다.

            아직 확인되지 않은 사실이 너무 많았다.

            우선 사건과 관련된 학생들을 직접 만나
            이야기를 들어 볼 필요가 있었다.

            **나** : "교장 선생님, 이 학생들과
            직접 이야기를 나눌 수 있을까요?"

            **교장** : "물론입니다.
            조사에 필요한 협조는 최대한 제공하겠습니다."

            나는 수첩을 챙기고 자리에서 일어났다.

            이제 본격적인 조사를 시작할 시간이었다.
            """)

        st.caption("다음 장면 : 학생 조사")

