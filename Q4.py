from utils import read_file
import matplotlib.pyplot as plt


# Read the files
v0 = read_file('data/v0_output_Q4.txt')
v1 = read_file('data/v1_output_Q4.txt')


#  Plot the learning curves
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(v0['Episode'], v0['R100'], label='CartPole-v0')
plt.plot(v1['Episode'], v1['R100'], label=' CartPole-v1')
plt.xlabel('Episode')
plt.ylabel('R100 (Avg Reward)')
plt.title('Learning Curves: Average Reward vs Episode')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(v0['Episode'], v0['R'], label='CartPole-v0')
plt.plot(v1['Episode'], v1['R'], label=' CartPole-v1')
plt.xlabel('Episode')
plt.ylabel('R (Episode Reward)')
plt.title('Learning Curves: Episode Reward vs Episode')
plt.legend()

plt.tight_layout()
plt.show()


