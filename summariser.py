from transformers import pipeline

def generate_summary(dialogue_lines):
    dialogue_text = " ".join(dialogue_lines)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    if len(dialogue_text.split()) > 800:
        dialogue_text = " ".join(dialogue_text.split()[:800])

    summary = summarizer(dialogue_text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
