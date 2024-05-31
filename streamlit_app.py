import streamlit as st

# Initialize session state for phrases if not already done
if 'phrases' not in st.session_state:
    st.session_state.phrases = ["Welcome", "Streamlit", "Edit", "This", "List"]

# Title of the app
st.title("Phrase Editor and Sorter")

# Input to edit the list of phrases
st.header("Edit Phrases")
phrases_text = st.text_area("Enter phrases separated by new lines:", "\n".join(st.session_state.phrases))

# Update the phrases in session state
st.session_state.phrases = [phrase.strip() for phrase in phrases_text.split('\n') if phrase.strip()]

# Button to sort phrases
if st.button("Sort Phrases"):
    st.session_state.phrases.sort()
    st.experimental_rerun()  # Refresh the page to show sorted list

# Display current list of phrases
st.header("Current Phrases")
for i, phrase in enumerate(st.session_state.phrases):
    st.text(f"{i + 1}. {phrase}")
