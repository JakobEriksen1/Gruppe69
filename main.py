from pathlib import Path
import plotly.graph_objects as go

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
    with logfile.open("r", encoding="utf-8") as fil:
        return fil.read().splitlines()


if __name__ == "__main__":

    logs = load_logs()
    print(f"Loaded {len(logs)} loglines.")




    for log in logs:
        types = log.split()

        date.append(types[0].split("T")[0])
        time.append(types[0].split("T")[1])
        level.append(types[1].split("=")[1])
        event.append(types[2].split("=")[1])
        user.append(types[3].split("=")[1])
        ip.append(types[4].split("=")[1])
        host.append(types[5].split("=")[1])
        port.append(types[6].split("=")[1])
        status.append(types[7].split("=")[1])
        msg.append(types[8].split("msg=")[1].strip('"'))


fig = go.Figure(data=[go.Table(

    header=dict(values=["Dato", "Tid", "Level", "Event", "User", "IP", "Host", "Port", "Status", "Message"]),

    cells=dict(values=[date, time, level, event, user, ip, host, port, status, msg])
)])



fig.show()

