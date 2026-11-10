from pathlib import Path


def load_logs():
    logfile = Path(__file__).parent / "cyber_security_log_sample.txt"
    with logfile.open("r", encoding="utf-8") as fil:
        return fil.read().splitlines()


if __name__ == "__main__":
    logs = load_logs()
    print(f"Load {len(logs)} loglines.")
    for line in logs[:5]:
        print(line)
