#### Preamble ####
# Purpose: Tests... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 26 September 2024 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
import pandas as pd

# Load the dataset
df = pd.read_csv('data/02-analysis_data/merged_swing_state_data.csv')

def test_trump_harris_pct_sum():
    """
    Test to ensure that the sum of Trump and Harris polling percentages does not exceed 100%.
    """
    invalid_rows = df[df['trump_pct'] + df['harris_pct'] > 100]
    assert invalid_rows.empty, f"Found rows where Trump + Harris percentage exceeds 100%: {invalid_rows}"

def test_valid_states():
    """
    Test to ensure that only certain states are present in the dataset.
    """
    valid_states = ['Arizona', 'Georgia', 'Michigan', 'Nevada', 'North Carolina', 'Pennsylvania', 'Wisconsin']
    invalid_states = df[~df['state'].isin(valid_states)]
    assert invalid_states.empty, f"Found rows with invalid states: {invalid_states['state'].unique()}"

def test_at_least_one_data_point_per_state():
    """
    Test to ensure that there is at least one data point for each of the key states.
    """
    required_states = ['Arizona', 'Georgia', 'Michigan', 'Nevada', 'North Carolina', 'Pennsylvania', 'Wisconsin']
    missing_states = [state for state in required_states if state not in df['state'].unique()]
    assert not missing_states, f"Missing data points for states: {missing_states}"

def test_no_negative_percentages():
    """
    Test to ensure that polling percentages (Trump and Harris) are non-negative.
    """
    invalid_rows = df[(df['trump_pct'] < 0) | (df['harris_pct'] < 0)]
    assert invalid_rows.empty, f"Found rows with negative percentages: {invalid_rows}"

def test_no_future_dates():
    """
    Test to ensure that start_date and end_date are not in the future.
    """
    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
    df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')
    invalid_rows = df[(df['start_date'] > pd.Timestamp.now()) | (df['end_date'] > pd.Timestamp.now())]
    assert invalid_rows.empty, f"Found rows with future dates: {invalid_rows}"

def test_sample_size_nonzero():
    """
    Test to ensure that sample sizes are non-zero and positive.
    """
    invalid_rows = df[df['sample_size'] <= 0]
    assert invalid_rows.empty, f"Found rows with zero or negative sample size: {invalid_rows}"

def test_numeric_columns():
    """
    Test to ensure that numeric columns contain valid numeric data.
    """
    numeric_columns = ['numeric_grade', 'pollscore', 'trump_pct', 'harris_pct', 'sample_size']
    invalid_rows = df[numeric_columns].isna().sum().sum()
    assert invalid_rows == 0, "Found rows with missing numeric data"

# Run the tests
test_trump_harris_pct_sum()
test_valid_states()
test_at_least_one_data_point_per_state()
test_no_negative_percentages()
test_no_future_dates()
test_sample_size_nonzero()
test_numeric_columns()

print("All tests passed.")