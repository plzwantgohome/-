
import streamlit as st


def show_dialogue(chapter, title, location, speaker, words):
    """모든 챕터에서 공통으로 사용하는 미연시형 대화 화면."""
    st.caption(chapter)
    st.title(title)

    with st.container(border=True):
        # 배경과 캐릭터가 들어갈 공간 (추후 이미지 추가)
        with st.container(height=280, border=False):
            st.caption(location)
            st.caption("배경 및 캐릭터 이미지 영역")

        # 현재 화자의 대사 한 개만 고정된 위치에 표시
        with st.container(height=140, border=True):
            st.markdown("**" + speaker + "**")
            st.write(words)
