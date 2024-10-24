import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data/02-analysis_data/merged_swing_state_data.csv")  # Replace with your file path

# Convert the end_date to datetime for plotting
data['end_date'] = pd.to_datetime(data['end_date'])

# Scatter plot: Poll Score over Time, Colored by State
plt.figure(figsize=(12, 6))
states = data['state'].unique()

# Plot each state's data with a different color
for state in states:
    subset = data[data['state'] == state]
    plt.scatter(subset['end_date'], subset['numeric_grade'], label=state, alpha=0.6)

plt.title('poll grade over Time by State')
plt.xlabel('End Date')
plt.ylabel('grade Score')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
plt.tight_layout()
plt.show()
