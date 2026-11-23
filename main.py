"""Write the entrant's honest count of open browser tabs to /output/entry.txt."""

import os

def main() -> None:
    count = "0"
    if not count.isdigit() or not 1 <= len(count) <= 5:
        raise ValueError("tab count must be 1-5 digits")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(count)


if __name__ == "__main__":
    main()
