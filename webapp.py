import streamlit as st
from dialogue_summariser.classifier import classify_dialogue
from dialogue_summariser.summariser import generate_summary
from dialogue_summariser.utils import visualise_dialogue_flow

def parse_uploaded_file(uploaded_file):
    lines = []
    for line in uploaded_file:
        decoded = line.decode("utf-8").strip()
        if decoded:
            lines.append(decoded)
    return lines

st.title("Dialogue Structuring and Summarising")

uploaded_file = st.file_uploader("Upload a dialogue transcript (.txt)", type=["txt"])

if uploaded_file is None:
    st.info("Please upload a .txt file to begin or close the app to exit.")
else:
    dialogue_lines = parse_uploaded_file(uploaded_file)
    st.subheader("Original Dialogue")
    for line in dialogue_lines:
        st.text(line)

    labelled_dialogue = classify_dialogue(dialogue_lines)
    st.subheader("Labelled Utterances")
    for line, label, confidence, rationale in labelled_dialogue:
        st.markdown(f"**[{label}]** {line}  \n_Confidence: {confidence:.2f}, Rationale: {rationale}_")

    summary = generate_summary(dialogue_lines)
    st.subheader("Dialogue Summary")
    st.write(summary)

    # Visualisation
    if st.button("Show Dialogue Flow Diagram"):
        output_path = "webapp_dialogue_flow"
        visualise_dialogue_flow(labelled_dialogue, output_path=output_path)
        st.image(f"{output_path}.png", caption="Dialogue Flow Diagram")

    # Use session state to prevent both actions at once
    if "exited" not in st.session_state:
        st.session_state["exited"] = False

    if not st.session_state["exited"]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Add a new file"):
                st.experimental_rerun()
        with col2:
            if st.button("Exit"):
                st.session_state["exited"] = True
                st.success("Thank you for using the Dialogue Summariser!")
                st.stop()
    else:
        st.success("Thank you for using the Dialogue Summariser!")
        st.stop()
