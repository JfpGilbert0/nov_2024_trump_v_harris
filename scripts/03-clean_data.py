#### Preamble ####
# Purpose: Cleans the raw plane data recorded by two observers..... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 6 April 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]

#### Workspace setup ####
import pandas as pd

# Load the dataset
df = pd.read_csv('data/raw_data/swing_state_polls.csv')

# Select the required columns
selected_columns = [
    'poll_id',
    'pollster_id',
    'pollster',
    'numeric_grade',
    'pollscore',
    'methodology',
    'transparency_score',
    'state',
    'start_date',
    'end_date',
    'question_id',
    'sample_size',
    'population',
    'population_full',
    'race_id',
    'party',
    'candidate_name',
    'pct'
]

# Filter the DataFrame
filtered_df = df[selected_columns]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('data/02-analysis_data/cleaned_swing_state_polls.csv', index=False)

