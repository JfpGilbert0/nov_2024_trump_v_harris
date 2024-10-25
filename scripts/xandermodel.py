import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the cleaned polling data
clean_poll_data = pd.read_csv("data/02-analysis_data/merged_swing_state_data.csv")

# Create a weight for each poll based on recency and sample size
# For simplicity, let's assume that the weight is based on the sample size directly
# and a recency factor that gives more weight to recent polls
# You can customize the recency weight according to your requirements
current_date = pd.to_datetime('today')
clean_poll_data['start_date'] = pd.to_datetime(clean_poll_data['start_date'])

# Calculate recency weight: newer polls have larger weights
clean_poll_data['recency_weight'] = (current_date - clean_poll_data['start_date']).dt.days
clean_poll_data['recency_weight'] = clean_poll_data['recency_weight'].max() - clean_poll_data['recency_weight']

# Calculate the overall weight by multiplying sample size with recency weight
clean_poll_data['weight'] = clean_poll_data['sample_size'] * clean_poll_data['recency_weight']

# Aggregate polling percentages for Trump and Harris by state, weighted by sample size and recency
state_average = clean_poll_data.groupby('state').agg(
    trump_pct_mean=('trump_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum()),
    harris_pct_mean=('harris_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum()),
    trump_pct_sd=('trump_pct', 'std'),
    harris_pct_sd=('harris_pct', 'std')
).reset_index()

# Calculate the probabilities of Trump winning based on the weighted percentages
state_average['trump_win_prob'] = state_average['trump_pct_mean'] / (state_average['trump_pct_mean'] + state_average['harris_pct_mean'])

# Prepare the logistic regression model
X = state_average[['trump_pct_mean', 'harris_pct_mean']]
y = (state_average['trump_pct_mean'] > state_average['harris_pct_mean']).astype(int)  # Binary outcome for the model

# Fit the logistic regression model
logistic_model = LogisticRegression()
logistic_model.fit(X, y)

# Predict probabilities of Trump winning
state_average['predicted_win_prob'] = logistic_model.predict_proba(X)[:, 1]


# Output the results
final_results = state_average[['state', 'trump_pct_mean', 'trump_pct_sd', 
                               'harris_pct_mean', 'harris_pct_sd',
                               'predicted_win_prob']].copy()

# Convert predicted probability to percentage
final_results['predicted_win_prob'] = final_results['predicted_win_prob'] * 100  # Convert to percentage

# Rename columns
final_results.columns = [
    'State', 'Trump % (Mean)', 'Trump % (SD)', 
    'Harris % (Mean)', 'Harris % (SD)', 'Percentage Chance of Trump Winning'
]

# Round the results to 1 decimal place
final_results = final_results.round(2)

# Print the final table
print(final_results)









