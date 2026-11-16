#imports af bibliotteker og filer
import log_loader
import runpy
from pathlib import Path


FOLDER = Path(__file__).parent

#Dette køre en python file
def run_file(filename):
    runpy.run_path(str(FOLDER / filename), run_name="__main__")

# Dette loop køre indtil at man afslutter med 0 eller q
while True:
    print("\n=== Bumle Business - VPN log analysis ===")
    print("1. Show log data in a table")
    print("2. Show failed login attempts per IP (bar chart)")
    print("3. Investigate relationships (scatter plots)")
    print("0 / q. Quit")

    choice = input("Choose: ").strip().lower()
    # Køre igennem fra top til bund og tjekker om input matcher til en af dem eller give den invalid choice
    if choice == "1":
        for lst in (log_loader.date, log_loader.time, log_loader.level,
                    log_loader.event, log_loader.user, log_loader.ip,
                    log_loader.host, log_loader.port, log_loader.status,
                    log_loader.msg):
            lst.clear()
        run_file("main.py")
    elif choice == "2":
        run_file("søjlediagram.py")
    elif choice == "3":
        print("Scatter plots have not been made yet.")
    elif choice in ("0", "q"):
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")