#### Preamble ####
# Purpose: Tests the simulated US election polling data
# Author: Alexander Guarasci & Jacob Gilbert
# Date: November 4, 2024
# Contact: alexander.guarasci@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install polars)
  # - `unittest` must be installed (pip install unittest)

import pandas as pd
import unittest

# Load the simulated dataset
df = pd.read_csv("simulated_polling_data.csv")

class TestSimulatedPollingData(unittest.TestCase):

    def setUp(self):
        # Define the valid states and candidates
        self.valid_states = ['Arizona', 'Georgia', 'Michigan', 'Nevada', 
                             'North Carolina', 'Pennsylvania', 'Wisconsin']
        self.valid_candidates = ['Donald Trump', 'Kamala Harris']
    
    def test_pct_below_100(self):
        """Test that no candidate's percentage exceeds 100%."""
        self.assertTrue((df['pct'] <= 100).all(), "One or more pct values exceed 100.")

    def test_valid_states(self):
        """Test that all states are valid."""
        self.assertTrue(df['state'].isin(self.valid_states).all(), "Found invalid states in the data.")

    def test_valid_candidates(self):
        """Test that all candidates are valid."""
        self.assertTrue(df['candidate_name'].isin(self.valid_candidates).all(), "Found invalid candidates in the data.")

    def test_equal_candidates_per_poll_id(self):
        """Test that there are equal numbers of Trump and Kamala for each poll_id."""
        # Group by poll_id and candidate_name, then count the occurrences
        candidate_counts = df.groupby(['poll_id', 'candidate_name']).size().unstack(fill_value=0)

        # Check if the counts for each candidate are equal for each poll_id
        self.assertTrue((candidate_counts['Donald Trump'] == candidate_counts['Kamala Harris']).all(),
                        "Not all poll IDs have equal counts for Donald Trump and Kamala Harris.")

if __name__ == "__main__":
    unittest.main()