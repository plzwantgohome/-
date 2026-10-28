
import streamlit as st


def choose_dialogue(options, key_prefix):

    st.html("""
    <style>
    div[class*="st-key-dialogue_option_"] button {
        width: fit-content !important;
        max-width: 100% !important;
        height: auto !important;
        min-height: 55px !important;
        padding: 12px 20px !important;
        letter-spacing: 1px !important;
    }

    div[class*="st-key-dialogue_option_"] button p {
        white-space: normal !important;
        overflow-wrap: anywhere !important;
        line-height: 1.6 !important;
    }
    </style>
    """)

    for i, option in enumerate(options):

        with st.container(
            key=f"dialogue_option_{key_prefix}_{i}"
        ):
            if st.button(
                option,
                key=f"{key_prefix}_{i}"
            ):
                return i

    return None
