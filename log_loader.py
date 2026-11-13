from pathlib import Path

date = []
time = []
level = []
event = []
user = []
ip = []
host = []
port = []
status = []
msg = []


# En funktion til at åbne log filen og finde antallet af linjer
def load_logs():
    logfile = Path(__file__).parent / "cyber_security_log_sample.txt"
    with logfile.open("r", encoding="utf-8") as file:
        return file.read().splitlines()