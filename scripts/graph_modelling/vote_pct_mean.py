import pandas as pd

# Assuming df is your DataFrame with the relevant data
# Replace 'path_to_your_csv' with the actual path if reading from CSV
# df = pd.read_csv('path_to_your_csv')

df = pd.read_parquet('data/02-analysis_data/merged_swing_state_data.parquet')

# Group by state and calculate the mean and standard deviation for trump_pct and harris_pct
summary_stats = df.groupby('state').agg(
    trump_pct_mean=('trump_pct', 'mean'),
    trump_pct_sd=('trump_pct', 'std'),
    harris_pct_mean=('harris_pct', 'mean'),
    harris_pct_sd=('harris_pct', 'std')
).reset_index()

# Round the values to 1 decimal place for neatness
summary_stats = summary_stats.round(1)

# Display the summary table
from tabulate import tabulate

print(tabulate(summary_stats, headers='keys', tablefmt='fancy_grid'))
