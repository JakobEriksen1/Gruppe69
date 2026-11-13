import matplotlib.pyplot as plt
from log_loader import load_logs

loginforsøg = {}

for log in load_logs():
    felter = log.split()
    if felter[2] == "event=LOGIN_FAILED":
        ip = felter[4].split("=")[1]
        loginforsøg[ip] = loginforsøg.get(ip, 0) + 1

# Vis IP-adresserne med flest mislykkede loginforsøg først.
loginforsøg = dict(sorted(loginforsøg.items(), key=lambda par: par[1], reverse=True))

plt.bar(loginforsøg.keys(), loginforsøg.values())
plt.title("Mislykkede loginforsøg pr. IP-adresse")
plt.xlabel("IP-adresse")
plt.ylabel("Antal mislykkede loginforsøg")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
