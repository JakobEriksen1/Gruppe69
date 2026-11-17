import matplotlib.pyplot as plt
from log_loader import load_logs

loginforsøg = {}

for log in load_logs():
    felter = log.split()
    if felter[2] == "event=LOGIN_FAILED":
        ip = felter[4].split("=")[1]
        loginforsøg[ip] = loginforsøg.get(ip, 0) + 1


loginforsøg = dict(sorted(loginforsøg.items(), key=lambda par: par[1], reverse=True))

plt.bar(loginforsøg.keys(), loginforsøg.values())
plt.title("Failed Login Attempts per IP Address")
plt.xlabel("IP Address")
plt.ylabel("Number of Failed Login Attempts")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
