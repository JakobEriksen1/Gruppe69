from pathlib import Path


def indlæs_logs():
    logfil = Path(file).parent / "cyber_security_log_sample.txt"
    with logfil.open("r", encoding="utf-8") as fil:
        return fil.read().splitlines()


if name == "main":
    logs = indlæs_logs()
    print(f"Indlæst {len(logs)} loglinjer.")
    for linje in logs[:5]:
        print(linje)