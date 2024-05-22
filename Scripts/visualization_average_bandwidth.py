import matplotlib.pyplot as plt

# Data for each service
tests = [1, 2, 3, 4, 5]
service_i_bandwidth = [13.6, 17.5, 14.9, 18.6, 13.7]
service_primary_bandwidth = [15.3, 14.7, 17.3, 17.6, 18.2]

# Compute the total average bandwidth for each service
average_bandwidth_service_i = sum(service_i_bandwidth) / len(service_i_bandwidth)
average_bandwidth_service_primary = sum(service_primary_bandwidth) / len(service_primary_bandwidth)

# Creating the plot with average bandwidth comparison
plt.figure(figsize=(10, 8))
plt.plot(tests, service_i_bandwidth, label='Service-i', marker='o', color='red')
plt.plot(tests, service_primary_bandwidth, label='Service-primary', marker='o', color='blue')

# Adding title, labels, and legend
plt.title('Average Bandwidth Comparison')
plt.xlabel('Test Number')
plt.ylabel('Average Bandwidth (Mbps)')
plt.xticks(tests)  # Set x-ticks to be test numbers
plt.legend()

# Adding a textbox for the total average bandwidth
textstr = f'Service-i Average Bandwidth: {average_bandwidth_service_i:.2f} Mbps\n'
textstr += f'Service-primary Average Bandwidth: {average_bandwidth_service_primary:.2f} Mbps'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.gca().text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
               verticalalignment='top', bbox=props, color='black')

# Displaying the plot with textbox
plt.grid(True)
plt.show()
