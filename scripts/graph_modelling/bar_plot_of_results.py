import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'State': ['Arizona', 'Georgia', 'Michigan', 'Nevada', 'North Carolina', 
              'Pennsylvania', 'Wisconsin'],
    'Trump % (Mean)': [49.85, 49.39, 48.57, 47.9, 48.48, 47.68, 47.76],
    'Trump % (SD)': [1.24, 1.78, 2.14, 1.5, 1.41, 1.81, 2.0],
    'Harris % (Mean)': [47.04, 47.66, 47.72, 48.63, 48.58, 48.53, 48.92],
    'Harris % (SD)': [2.17, 2.52, 2.12, 1.19, 1.55, 1.29, 1.72],
    'Percentage Chance of Trump Winning': [86.85, 71.18, 53.09, 21.34, 32.31, 19.67, 15.52]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the distance from 50%
df['Distance from 50'] = df['Percentage Chance of Trump Winning'] - 50

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars: left if below 50, right if above 50
colors = ['blue' if x < 0 else 'red' for x in df['Distance from 50']]
ax.barh(df['State'], df['Distance from 50'], color=colors, align='center')

# Draw a vertical line at 0 (representing 50%)
ax.axvline(0, color='black', linewidth=1)

# Set labels and title
ax.set_xlabel('Distance from 50% (Trump Winning Probability)')
ax.set_title('Centered Bar Chart of Trump’s Winning Probability by State')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
