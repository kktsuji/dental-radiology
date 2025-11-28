"""load .txt file and remove unnecessary lines"""

from glob import glob
import os

base = "data/transcripts/*.txt"

for file in glob(base):
    output = []
    fn = os.path.basename(file)
    print(f"Processing file: {fn}")
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            if (
                line.strip()  # blank line check
                and not "Unknown" in line.strip()  # check lines containing "Unknown"
                and not line.strip()
                .replace(":", "")
                .replace(".", "")
                .replace("-", "")
                .replace(" ", "")
                .isdigit()  # check lines with only timestamp (e.g."04:35:51:25 - 04:36:18:26")
            ):
                output.append(line.strip())

    with open(f"out/modified_{fn}", "w", encoding="utf-8") as f:
        for line in output:
            f.write(line + "\n\n")
