# Dialogue Structuring and Summarising Task

## Overview
This project processes a dialogue transcript and:
1. Classifies each utterance by function (e.g., Proposal, Challenge, etc.)
2. Uses a Hugging Face summarization model to describe the dialogue flow

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Script
```bash
python main.py
```

## File Descriptions
- `sample_dialogue.txt` — Input dialogue
- `classifier.py` — Labels each utterance
- `summariser.py` — Uses BART model to summarize dialogue
- `main.py` — Runs the full pipeline
- 'webapp.py' - Runs the webapp
