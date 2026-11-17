import matplotlib.pyplot as plt

from log_loader import load_logs



level_counts = {}
for line in load_logs():
    fields = dict(part.split("=", 1) for part in line.split()[1:] if "=" in part)
    level = fields.get("level")
    if level:
        level_counts[level] = level_counts.get(level, 0) + 1

if level_counts:
    plt.pie(
        level_counts.values(),
        labels=level_counts.keys(),
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Log Level Distribution")
    plt.tight_layout()
    plt.show()
else:
    print("No log level data was found in the log.")
