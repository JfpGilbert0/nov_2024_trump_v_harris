
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged swing state polling data
data_path = "data/02-analysis_data/merged_swing_state_data.parquet"
df = pd.read_parquet(data_path)

# Convert date columns to datetime format
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# Calculate average polling percentages by candidate
avg_polling = df[['trump_pct', 'harris_pct']].mean()

# Create a bar plot
plt.figure(figsize=(8, 5))
avg_polling.plot(kind='bar', color=['blue', 'orange'])
plt.title('Average Polling Percentages by Candidate Across States')
plt.ylabel('Average Percentage')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Melt the DataFrame for seaborn
melted_df = df.melt(id_vars=['state', 'start_date'], value_vars=['trump_pct', 'harris_pct'],
                     var_name='candidate', value_name='percentage')

# Create a violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='candidate', y='percentage', data=melted_df, palette='muted')
plt.title('Distribution of Polling Percentages by Candidate')
plt.ylabel('Percentage')
plt.tight_layout()
plt.show()

