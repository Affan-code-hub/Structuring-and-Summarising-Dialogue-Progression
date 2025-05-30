import re

def classify_dialogue(dialogue_lines):
    """
    Classifies each utterance in the dialogue according to its conversational function.
    Returns a list of tuples: (original_line, label, confidence, rationale)
    """
    labels = []
    proposal_keywords = [
        "should", "let’s", "we could", "we might", "how about", "let us", "let's", "why don't we", "we can", "i propose", "i suggest", "we need to", "we ought to", "we should", "let me", "let me suggest"
    ]
    query_keywords = [
        "why", "how", "what", "did we", "do we", "have we", "are we", "is it", "could we", "would it", "can we", "shall we", "will we", "who", "when", "where"
    ]
    challenge_keywords = [
        "not sure", "don’t", "i’m not", "i disagree", "i don't think", "i doubt", "i still think", "that's not", "that's a bold claim", "i don't believe", "i am not convinced"
    ]
    justification_keywords = [
        "because", "since", "as", "due to", "it uses", "true", "we've seen", "the reason", "as a result", "so that", "in order to"
    ]
    deferral_keywords = [
        "not yet", "later", "roadmap", "next week", "next month", "after", "once", "when we", "soon", "eventually"
    ]
    commitment_keywords = [
        "i will", "i’ll", "i am going to", "i can", "i'll", "i'll check", "i'll get", "i'll include", "i'll update", "i'll draft", "i'll start", "i'll prepare", "i'll do", "i'll make", "i'll send", "i'll follow up", "i'll get started", "i'll get on it"
    ]

    for line in dialogue_lines:
        try:
            speaker, utterance = line.split(":", 1)
            utterance = utterance.strip().lower()
            utterance_clean = re.sub(r'[^\w\s]', '', utterance)  # remove punctuation
        except ValueError:
            labels.append((line, "Invalid", 0.0, "Could not parse line"))
            continue

        label = "Other"
        confidence = 0.5
        rationale = "No strong keyword match"

        # Proposal
        if any(kw in utterance_clean for kw in proposal_keywords):
            label = "Proposal"
            confidence = 0.9
            rationale = "Contains proposal keywords"
        # Query (also check for question mark)
        elif any(kw in utterance_clean for kw in query_keywords) or utterance.strip().endswith("?"):
            label = "Query"
            confidence = 0.85
            rationale = "Contains query keywords or is a question"
        # Challenge
        elif any(kw in utterance_clean for kw in challenge_keywords):
            label = "Challenge"
            confidence = 0.8
            rationale = "Contains challenge keywords"
        # Justification
        elif any(kw in utterance_clean for kw in justification_keywords):
            label = "Justification"
            confidence = 0.8
            rationale = "Contains justification keywords"
        # Deferral
        elif any(kw in utterance_clean for kw in deferral_keywords):
            label = "Deferral"
            confidence = 0.8
            rationale = "Contains deferral keywords"
        # Commitment
        elif any(kw in utterance_clean for kw in commitment_keywords):
            label = "Commitment"
            confidence = 0.85
            rationale = "Contains commitment keywords"

        labels.append((line, label, confidence, rationale))
    return labels
