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

# Read the files
df_sync = read_file('data/q3_sync')
df_alpha = read_file('data/q3_alpha')


#  Plot the learning curves
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(df_sync['Episode'], df_sync['R100'], label='Hard Update (sync)')
plt.plot(df_alpha['Episode'], df_alpha['R100'], label='Soft Update (alpha)')
plt.xlabel('Episode')
plt.ylabel('R100 (Avg Reward)')
plt.title('Learning Curves: Average Reward vs Episode')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(df_sync['Episode'], df_sync['L100'], label='Hard Update (sync)')
plt.plot(df_alpha['Episode'], df_alpha['L100'], label='Soft Update (alpha)')
plt.xlabel('Episode')
plt.ylabel('L100 (Avg Loss)')
plt.title('Learning Curves: Average Loss vs Episode')
plt.legend()

plt.tight_layout()
plt.show()


# Peak Performance
max_reward_sync = df_sync['MaxR'].max()
episode_at_max_sync = df_sync[df_sync['MaxR'] == max_reward_sync]['Episode'].iloc[0]

max_reward_alpha = df_alpha['MaxR'].max()
episode_at_max_alpha = df_alpha[df_alpha['MaxR'] == max_reward_alpha]['Episode'].iloc[0]

print(f"Hard Update: Max Reward {max_reward_sync} at Episode {episode_at_max_sync}")
print(f"Soft Update: Max Reward {max_reward_alpha} at Episode {episode_at_max_alpha}")


# Computational Efficiency
print(f"Hard Update: Average FPS {df_sync['FPS'].mean()}")
print(f"Soft Update: Average FPS {df_alpha['FPS'].mean()}")

# Final Perfomance
print(f"Hard Update: Final R100 {df_sync['R100'].iloc[-1]}, Final R {df_sync['R'].iloc[-1]}")
print(f"Soft Update: Final R100 {df_alpha['R100'].iloc[-1]}, Final R {df_alpha['R'].iloc[-1]}")

