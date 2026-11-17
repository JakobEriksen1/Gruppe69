import matplotlib.pyplot as plt

from log_loader import load_logs



status_counts = {}
for line in load_logs():
    fields = dict(part.split("=", 1) for part in line.split()[1:] if "=" in part)
    status = fields.get("status")
    if status:
        status_counts[status] = status_counts.get(status, 0) + 1

if status_counts:
    plt.pie(
        status_counts.values(),
        labels=status_counts.keys(),
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Log event status distribution")
    plt.tight_layout()
    plt.show()
else:
    print("No status data was found in the log.")
