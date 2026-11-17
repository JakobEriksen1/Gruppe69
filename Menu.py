# Imports used to run the different program features.
import log_loader
import runpy
from pathlib import Path


FOLDER = Path(__file__).parent

# Run a Python file from this project folder.
def run_file(filename):
    runpy.run_path(str(FOLDER / filename), run_name="__main__")

# Keep showing the menu until the user chooses to quit.
while True:
    print("\n=== Bumle Business - VPN log analysis ===")
    print("1. Show log data in a table")
    print("2. Show failed login attempts per IP (bar chart)")
    print("3. Show log event status distribution (pie chart)")
    print("0 / q. Quit")

    choice = input("Choose: ").strip().lower()
    # Run the feature selected by the user.
    if choice == "1":
        for lst in (log_loader.date, log_loader.time, log_loader.level,
                    log_loader.event, log_loader.user, log_loader.ip,
                    log_loader.host, log_loader.port, log_loader.status,
                    log_loader.msg):
            lst.clear()
        run_file("main.py")
    elif choice == "2":
        run_file("Søjlediagram.py")
    elif choice == "3":
        run_file("Pie_chart.py")
    elif choice in ("0", "q"):
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
