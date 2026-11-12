from pathlib import Path
import plotly.graph_objects as go

def load_logs():
    logfile = Path(__file__).parent / "cyber_security_log_sample.txt"
    with logfile.open("r", encoding="utf-8") as fil:
        return fil.read().splitlines()


if __name__ == "__main__":
    logs = load_logs()
    print(f"Loaded {len(logs)} loglines.")

fig = go.Figure(data=[go.Table(
    header=dict(values=["Log information"]),
    cells=dict(values=[logs])
)])

fig.show()
