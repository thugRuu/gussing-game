import streamlit as st

st.title("📝 Simple Markdown Note-Taking App")

# Create a two-column layout: Left for typing, Right for live preview
col1, col2 = st.columns(2)

with col1:
    st.subheader("Markdown Editor")
    # A text box that holds your notes
    note_text = st.text_area(
        "Write your notes here...", 
        height=400, 
        value="# Welcome!\n\n- Type **Markdown** on the left.\n- See the magic on the right."
    )

with col2:
    st.subheader("Live Preview")
    # Streamlit automatically renders Markdown natively!
    st.markdown(note_text)