import matplotlib.pyplot as plt
from utils import read_file


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

