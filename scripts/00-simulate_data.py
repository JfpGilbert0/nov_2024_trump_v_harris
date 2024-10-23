#### Preamble ####
# Purpose: Simulates a dataset of Australian electoral divisions, including the 
  # state and party that won each division.
# Author: Rohan Alexander
# Date: 26 September 2024
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)


#### Workspace setup ####
import pandas as pd
import numpy as np
from random import choice, uniform, randint
from datetime import timedelta, datetime

# Function to generate random dates
def random_dates(start, end, n=1):
    """Generate random dates between start and end."""
    return [start + timedelta(days=randint(0, (end - start).days)) for _ in range(n)]

# Define constants
pollster_names = ["AtlasIntel", "YouGov", "Washington Post/George Mason University"]
methods = ["Online Ad", "Online Panel", "Live Phone/Text-to-Web/Email/Mail-to-Web"]
states = ["Arizona", "Georgia", "Michigan", "Nevada", "North Carolina", "Pennsylvania", "Wisconsin"]
candidates = ["Kamala Harris", "Donald Trump"]

# Create an empty list to store rows of data
data = []

# Set a random seed for reproducibility
np.random.seed(42)

# Generate 400 rows of data
for poll_id in range(88795, 88795 + 400, 1):
    # Pollster ID is constant for simplicity in this example
    pollster_id = 1528
    pollster = choice(pollster_names)
    numeric_grade = round(uniform(2.0, 3.5), 1)
    pollscore = round(uniform(-2.0, 2.0), 1)
    methodology = choice(methods)
    transparency_score = round(uniform(5.0, 10.0), 1)
    state = choice(states)
    start_date = random_dates(datetime(2024, 10, 1), datetime(2024, 10, 15))[0].strftime("%m/%d/%y")
    end_date = random_dates(datetime(2024, 10, 16), datetime(2024, 10, 20))[0].strftime("%m/%d/%y")
    question_id = 213382 + (poll_id - 88795) % 1000  # Incrementing question ID based on poll_id
    sample_size = round(uniform(600, 2500))  # Sample size between 600 and 2500
    population = choice(['lv', 'rv'])  # Likely voters or registered voters
    race_id = 8759 + (poll_id - 88795) % 100  # Incrementing race ID
    party = choice(['DEM', 'REP'])
    candidate_name = choice(candidates)
    pct = round(uniform(40.0, 60.0), 1)  # Percentages between 40 and 60

    # Append generated data to the list
    data.append([
        poll_id, pollster_id, pollster, numeric_grade, pollscore,
        methodology, transparency_score, state, start_date, end_date,
        question_id, sample_size, population, population, race_id,
        party, candidate_name, pct
    ])

# Create a DataFrame
columns = [
    "poll_id", "pollster_id", "pollster", "numeric_grade", "pollscore",
    "methodology", "transparency_score", "state", "start_date", "end_date",
    "question_id", "sample_size", "population", "population_full",
    "race_id", "party", "candidate_name", "pct"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('data/00-simulated_data/simulated_data.csv', index=False)

# Display the first few rows of the DataFrame
print(df.head())