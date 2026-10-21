
import streamlit as st


def show_chapter1():

    # 챕터 1 스토리
    story = [
        (
            "늦은 오후, 조용한 탐정 사무소에 전화벨이 울렸다.\n\n"
            "평소와 다를 것 없는 하루였다.\n"
            "책상 위에는 정리되지 않은 서류들이 쌓여 있었다.\n\n"
            "탐정은 수화기를 집어 들었다."
        ),

        (
            '**???** : "안녕하십니까. 혹시 탐정 사무소가 맞습니까?"\n\n'
            '**탐정** : "네, 맞습니다. 무슨 일이시죠?"'
        ),

        (
            '**???** : "저는 ○○고등학교의 교장입니다. '
            '다름이 아니라... 학교에서 조금 곤란한 일이 발생했습니다."\n\n'
            '**교장** : "최근 교내 시험 자료가 외부로 유출되었다는 '
            '의혹이 제기되었습니다."'
        ),

        (
            '**탐정** : "시험 자료 유출이라... '
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
            '탐정은 잠시 생각에 잠겼다.'
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
                '**탐정** : "알겠습니다. 내일 학교로 찾아가겠습니다."\n\n'
                '**교장** : "감사합니다. '
                '자세한 사항은 학교에서 말씀드리겠습니다."\n\n'
                '전화가 끊겼다.\n\n'
                '탐정은 수첩을 펼쳐 학교의 이름을 적었다.\n\n'
                '평범한 시험 자료 유출 사건일까.\n'
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
