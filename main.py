from classifier import classify_dialogue
from summariser import generate_summary
from utils import read_dialogue, format_output, visualise_dialogue_flow

if __name__ == "__main__":
    dialogue_lines = read_dialogue("sample_dialogue.txt")
    labelled_dialogue = classify_dialogue(dialogue_lines)
    summary = generate_summary(dialogue_lines)
    format_output(dialogue_lines, labelled_dialogue, summary)
    visualise_dialogue_flow(labelled_dialogue)
