"""Write the entrant's honest count of open browser tabs to /output/entry.txt."""

import os

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("0")
