import pandas as pd
import matplotlib.pyplot as plt

# Load your data (replace with your actual data file path)
data = pd.read_parquet('data/02-analysis_data/merged_swing_state_data.parquet')

# Ensure date column is in datetime format
data['end_date'] = pd.to_datetime(data['end_date'])

# Plot the histogram of poll quantity by end date
plt.figure(figsize=(12, 6))
plt.hist(data['end_date'], bins=20, edgecolor='black', alpha=0.7)

# Adding labels and title
plt.xlabel('End Date of Poll')
plt.ylabel('Number of Polls')
plt.title('Histogram of Poll Quantity by End Date')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
