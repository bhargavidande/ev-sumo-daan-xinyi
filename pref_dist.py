import numpy as np
import pandas as pd
from scipy.stats import truncnorm
import os

# Configuration
num_users = 2000
output_file = "../appendices/AppendixA_user_pref.txt"
param_table_file = "../appendices/parameters_table.csv"
np.random.seed(42)  # Reproducibility

# Truncated Normal Distribution Helper
def get_truncated_normal(mean=120, sd=30, low=30, upp=240):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# Generate parking duration preferences
duration_distribution = get_truncated_normal()
parking_durations = duration_distribution.rvs(num_users).round(2)

# Simulate location preference scores using Gaussian decay
def generate_location_preference(alpha=0.005, num_pls=8):
    distances = np.random.uniform(100, 2000, num_pls)  # distances in meters
    preference_scores = np.exp(-alpha * distances)
    return preference_scores.round(4)

location_preferences = [generate_location_preference() for _ in range(num_users)]

# Save to file
with open(output_file, "w") as f:
    f.write("user_id,parking_duration(min),location_preference_scores\n")
    for i in range(num_users):
        scores = ",".join(map(str, location_preferences[i]))
        f.write(f"{i+1},{parking_durations[i]},{scores}\n")

print(f"User preference file saved to {output_file}")

# Generate Parameters Table CSV
param_table = {
    "Parameter": ["mu_d", "sigma_d", "Duration Range", "Alpha", "Distance Range"],
    "Value": [120, 30, "[30, 240]", 0.005, "[100, 2000] meters"],
    "Description": [
        "Mean parking duration in minutes",
        "Standard deviation of duration",
        "Valid parking duration range",
        "Decay factor for distance-based preference",
        "Simulated distance range from preferred location"
    ]
}
df = pd.DataFrame(param_table)
df.to_csv(param_table_file, index=False)
print(f"Parameter table saved to {param_table_file}")
