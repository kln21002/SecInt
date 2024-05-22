import matplotlib.pyplot as plt
import numpy as np

# Read and process data from a text file
with open('performance test meridio/sum.txt', 'r') as file:
    y_data = [round(float(line.strip())) for line in file.readlines()]

# Assuming x_data remains the same, representing the number of TCP connections
x_data = np.arange(1, len(y_data) + 1)  # Adjust x_data to match the length of y_data

# Calculate statistics
max_latency = max(y_data)
min_latency = min(y_data)
range_latency = max_latency - min_latency  # Range of latency
average_latency = np.mean(y_data)
diff_delays = np.diff(y_data)
abs_diff_delays = np.abs(diff_delays)
jitter = np.mean(abs_diff_delays)  # Traditional network jitter calculation

# Create a figure and an axes.
fig, ax = plt.subplots()

# Plotting the data
ax.plot(x_data, y_data, linestyle='-', color='r')

# Adding title and labels
ax.set_title('Latency test - service-i')
ax.set_xlabel('TCP Connection')
ax.set_ylabel('Latency (ms)')

# Display statistics
stats_text = (f"Max Latency: {max_latency} ms\n"
              f"Min Latency: {min_latency} ms\n"
              f"Latency Range: {range_latency} ms\n"
              f"Average Latency: {average_latency:.2f} ms\n"
              f"Jitter: {jitter:.2f} ms")
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

# Optional: Set the limit for the axes
ax.set_xlim([0, max(x_data) + 10])
ax.set_ylim([0, max(y_data) + 10])

# Display the plot
plt.grid(True)
plt.show()
