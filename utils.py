def read_dialogue(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def format_output(dialogue_lines, labelled_dialogue, summary):
    print("\n=== Original Dialogue ===")
    for line in dialogue_lines:
        print(line)

    print("\n=== Labelled Utterances ===")
    for line, label, confidence, rationale in labelled_dialogue:
        print(f"[{label}] {line} (Confidence: {confidence:.2f}, Rationale: {rationale})")

    print("\n=== Dialogue Summary ===")
    print(summary)

def visualise_dialogue_flow(labelled_dialogue, output_path="dialogue_flow.png"):
    try:
        from graphviz import Digraph
        from graphviz.backend import ExecutableNotFound
    except ImportError:
        print("graphviz not installed, skipping visualisation.")
        return
    dot = Digraph(comment="Dialogue Flow")
    for idx, (line, label, confidence, rationale) in enumerate(labelled_dialogue):
        dot.node(str(idx), f"{label}\n{line.split(':',1)[0]}")
        if idx > 0:
            dot.edge(str(idx-1), str(idx))
    try:
        dot.render(output_path, format="png", cleanup=True)
        print(f"Dialogue flow diagram saved to {output_path}")
    except ExecutableNotFound:
        print("Graphviz executables not found. Please install Graphviz and ensure its executables are on your system PATH. Skipping visualisation.")
