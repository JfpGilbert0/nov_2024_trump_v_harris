# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load the cleaned polling data
data_path = "data/02-analysis_data/merged_swing_state_data.csv"
clean_poll_data = pd.read_csv(data_path)

# Check if necessary columns exist
required_columns = ['trump_pct', 'harris_pct', 'end_date', 'sample_size', 'state']
for column in required_columns:
    if column not in clean_poll_data.columns:
        raise ValueError(f"The required column '{column}' is not present in the dataset.")

# Convert end_date column to datetime format
clean_poll_data['end_date'] = pd.to_datetime(clean_poll_data['end_date'])

# Define a weighting function
def calculate_weight(row):
    # Weight based on recency (more recent = higher weight)
    recency_weight = 1 / (pd.Timestamp.now() - row['end_date']).days  # More recent polls have higher weights
    sample_size_weight = row['sample_size'] / clean_poll_data['sample_size'].max()  # Scale by max sample size
    return recency_weight * sample_size_weight

# Apply the weighting function to create a new 'weight' column
clean_poll_data['weight'] = clean_poll_data.apply(calculate_weight, axis=1)

# Aggregate polling percentages for Trump and Harris by state, weighted by sample size and recency
state_average = clean_poll_data.groupby('state').agg(
    trump_pct=('trump_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum()),
    harris_pct=('harris_pct', lambda x: (x * clean_poll_data.loc[x.index, 'weight']).sum() / clean_poll_data.loc[x.index, 'weight'].sum()),
    total_weight=('weight', 'sum')  # Total weight for reference
).reset_index()

# Create a binary outcome for prediction: 1 if Trump is predicted to win, 0 if Harris
state_average['winner'] = (state_average['trump_pct'] > state_average['harris_pct']).astype(int)

# Features and target
X = state_average[['trump_pct', 'harris_pct']]
y = state_average['winner']

# Initialize the Logistic Regression model with L2 regularization
logistic_model = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=2000)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
logistic_model.fit(X_scaled, y)

# Predict outcomes for all states
state_average['predicted_winner'] = logistic_model.predict(X_scaled)

# Save the model to a file for future use
joblib.dump(logistic_model, 'models/state_winner_model.pkl')

# Output the state-level predictions
print(state_average[['state', 'trump_pct', 'harris_pct', 'predicted_winner']])

# Save the state predictions to a CSV file
state_average.to_csv("state_predictions.csv", index=False)