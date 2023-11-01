import pandas as pd
import matplotlib.pyplot as plt

def parse_line(line):
    """Parse a single line from the file to extract metrics."""
    
    # Check for expected components in the line
    if not all(keyword in line for keyword in ["Frame:", "Episode:", "R100:", "MaxR:", "R:", "FPS:", "L100:", "Epsilon:"]):
        return None

    parts = line.split(", ")
    
    # Ensure there are the expected number of parts
    if len(parts) != 7:
        return None

    try:
        frame = int(parts[0].split(":")[1].strip())
        episode = int(parts[0].split(":")[3].strip())
        r100 = float(parts[1].split(":")[1].strip())
        maxr = float(parts[2].split(":")[1].strip())
        r = float(parts[3].split(":")[1].strip())
        fps = float(parts[4].split(":")[1].strip())
        l100 = float(parts[5].split(":")[1].strip())
        epsilon = float(parts[6].split(":")[1].strip())
    except ValueError:
        return None

    return {"Frame": frame, "Episode": episode, "R100": r100, "MaxR": maxr, "R": r, "FPS": fps, "L100": l100, "Epsilon": epsilon}

def read_file(filename):
    """Read and parse the file."""
    with open(filename, 'r') as f:
        data = [parsed for parsed in (parse_line(line) for line in f) if parsed is not None]
    return pd.DataFrame(data)
