import plotly.graph_objects as go
from log_loader import (load_logs, date, time, level, event, user,
                        ip, host, port, status, msg)


if __name__ == "__main__":

    logs = load_logs()
    print(f"Loaded {len(logs)} loglines.")

    for log in logs:
        types = log.split(" ", 8)

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
        columnwidth=[80, 70, 60, 230, 90, 110, 70, 55, 80, 350],
        header=dict(values=["Dato", "Tid", "Level", "Event", "User", "IP", "Host", "Port", "Status", "Message"],
        align="left"),
        cells=dict(values=[date, time, level, event, user, ip, host, port, status, msg],
        align="left",
        height=28)
    )])
    fig.show(renderer="browser")