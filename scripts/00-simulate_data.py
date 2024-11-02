#### Preamble ####
# Purpose: Simulates US presidential election polling data
# Author: Alexander Guarasci & Jacob Gilbert
# Date: November 4, 2024
# Contact: alexander.guarasci@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)





import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define constants
states = ['Arizona', 'Georgia', 'Michigan', 'Nevada', 'North Carolina', 'Pennsylvania', 'Wisconsin']
candidates = ['Donald Trump', 'Kamala Harris']

# Create a list to hold the simulated data
data = []

# Simulate 400 rows of data
for _ in range(400):
    # Generate poll_id
    poll_id = np.random.randint(88795, 88800)

    # Create unique question_id and sample_size
    question_id = np.random.randint(213382, 213400)
    sample_size = np.random.randint(1400, 1500)

    # Randomly choose a state from the specified states
    state = np.random.choice(states)

    # Generate candidate percentages ensuring their sum is around 100%
    pct_harris = np.random.uniform(0, 50)  # Max 50% for Kamala Harris
    pct_trump = 100 - pct_harris            # Donald Trump's percentage is the remainder

    # Ensure the total percentage is less than or equal to 100
    if pct_harris + pct_trump > 100:
        pct_harris = np.random.uniform(0, 100)
        pct_trump = 100 - pct_harris

    # Append Kamala Harris data
    data.append([
        poll_id,
        state,
        "Kamala Harris",
        round(pct_harris, 1)  # percentage for Kamala Harris
    ])

    # Append Donald Trump data
    data.append([
        poll_id,
        state,
        "Donald Trump",
        round(pct_trump, 1)  # percentage for Donald Trump
    ])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=[
    "poll_id", "state", "candidate_name", "pct"
])

# Display the first few rows of the simulated dataset
print(df.head())

# Save the simulated dataset to a parquet file
df.to_parquet("data/00-simulated_data/simulated_data.parquet", index=False)