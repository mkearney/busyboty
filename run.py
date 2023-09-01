from pathlib import Path
from datetime import datetime


bb = Path("/Users/mwk/projects/busyboty/count.txt")

now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S\n")

with open(bb, "a") as f:
    f.write(now)
