
import streamlit as st


def show_dialogue(
    chapter, title, location, speaker, words,
    skip_key=None, skip_changes=None
):
    """모든 챕터에서 공통으로 사용하는 미연시형 대화 화면."""

    st.caption(chapter)
    st.title(title)

    with st.container(border=True):

        # 배경과 캐릭터가 들어갈 공간
        with st.container(height=280, border=False):

            if skip_key is not None and skip_changes is not None:

                left, right = st.columns(
                    [9, 1],
                    vertical_alignment="center"
                )

                with left:
                    st.caption(location)

                with right:
                    if st.button(
                        "스킵 ⏭",
                        key=skip_key,
                        type="tertiary",
                        use_container_width=True
                    ):
                        st.session_state.update(skip_changes)
                        st.rerun()

            else:
                st.caption(location)

            st.caption("배경 및 캐릭터 이미지 영역")

        # 현재 화자의 대사
        with st.container(height=140, border=True):
            st.markdown("**" + speaker + "**")
            st.write(words)
