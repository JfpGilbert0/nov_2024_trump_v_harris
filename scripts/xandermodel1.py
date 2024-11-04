import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the cleaned polling data
clean_poll_data = pd.read_parquet("data/02-analysis_data/merged_swing_state_data.parquet")

# Create a weight for each poll based on recency and sample size
current_date = pd.to_datetime('today')
clean_poll_data['start_date'] = pd.to_datetime(clean_poll_data['start_date'])
clean_poll_data['recency_weight'] = (current_date - clean_poll_data['start_date']).dt.days

# Normalize the recency weight (larger weight for more recent polls)
clean_poll_data['recency_weight'] = clean_poll_data['recency_weight'].max() - clean_poll_data['recency_weight']
clean_poll_data['weight'] = clean_poll_data['sample_size'] * clean_poll_data['recency_weight']

# Aggregate polling percentages for Trump and Harris by state, weighted by sample size and recency
state_average = clean_poll_data.groupby('state').agg(
    trump_pct=('trump_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum()),
    harris_pct=('harris_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum())
).reset_index()

# Calculate the probabilities of Trump winning based on the weighted percentages
state_average['trump_win_prob'] = state_average['trump_pct'] / (state_average['trump_pct'] + state_average['harris_pct'])

# Prepare the logistic regression model
X = state_average[['trump_pct', 'harris_pct']]
y = (state_average['trump_pct'] > state_average['harris_pct']).astype(int)  # Binary outcome for the model

# Fit the logistic regression model
logistic_model = LogisticRegression()
logistic_model.fit(X, y)

# Predict probabilities of Trump winning
state_average['predicted_win_prob'] = logistic_model.predict_proba(X)[:, 1]

# Predict binary outcomes for Trump winning (1) or losing (0)
state_average['predicted_winner'] = (state_average['predicted_win_prob'] > 0.5).astype(int)

# Output the results
final_results = state_average[['state', 'trump_pct', 'harris_pct', 'predicted_win_prob', 'predicted_winner']].copy()
final_results['predicted_win_prob'] = final_results['predicted_win_prob'] * 100  # Convert to percentage
final_results.columns = ['State', 'Trump %', 'Harris %', 'Percentage Chance of Trump Winning', 'Predicted Winner']

print(final_results)