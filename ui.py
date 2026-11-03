
import streamlit as st


def show_dialogue(
    chapter, title, location, speaker, words,
    skip_key=None, skip_changes=None
):
    """모든 챕터에서 공통으로 사용하는 미연시형 대화 화면."""

    # 챕터 1 스킵 버튼의 크기와 디자인

    st.html("""
    <style>
    /* 배경 영역 높이 유지 및 스크롤 방지 */
    div.st-key-vn_background {
        min-height: 280px !important;
        width: 100% !important;
        box-sizing: border-box !important;
        overflow: visible !important;
    }

    /* 스킵 버튼 오른쪽 정렬 */
    div[class*="st-key-story_skip_"] {
        display: flex !important;
        justify-content: flex-end !important;
        width: 100% !important;
    }

    div[class*="st-key-story_skip_"] button {
        width: fit-content !important;
        min-width: 0 !important;
        max-width: 100% !important;
        height: 28px !important;
        min-height: 28px !important;
        padding: 0 6px !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #aaaaaa !important;
    }

    div[class*="st-key-story_skip_"] button p {
        font-size: 13px !important;
        white-space: nowrap !important;
    }

    div[class*="st-key-story_skip_"] button:hover {
        color: #ffffff !important;
    }
    </style>
    """)


    st.caption(chapter)
    st.title(title)

    with st.container(border=True):

        # 배경과 캐릭터가 들어갈 공간
        with st.container(
            border=False,
            key="vn_background"
        ):

            if skip_key is not None and skip_changes is not None:

                left, right = st.columns(
                    [8, 2],
                    vertical_alignment="center"
                )

                with left:
                    st.caption(location)

                with right:
                    if st.button(
                        "스킵 ⏭",
                        key=skip_key,
                        type="tertiary"
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
