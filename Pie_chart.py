import matplotlib.pyplot as plt

from log_loader import load_logs



failed_logins = {}
for line in load_logs():
    fields = dict(part.split("=", 1) for part in line.split()[1:] if "=" in part)
    if fields.get("event") == "LOGIN_FAILED" and "src_ip" in fields:
        ip = fields["src_ip"]
        failed_logins[ip] = failed_logins.get(ip, 0) + 1

if failed_logins:

    sorted_ips = sorted(failed_logins.items(), key=lambda item: item[1], reverse=True)
    top_ips = sorted_ips[:5]
    labels = [ip for ip, count in top_ips]
    counts = [count for ip, count in top_ips]

    other_count = sum(count for ip, count in sorted_ips[5:])
    if other_count > 0:
        labels.append("Other IPs")
        counts.append(other_count)

    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Failed login attempts by source IP")
    plt.tight_layout()
    plt.show()

    most_attempts = sorted_ips[0]
    print(f"Most failed logins: {most_attempts[0]} ({most_attempts[1]} attempts).")
else:
    print("No failed login attempts were found in the log.")
