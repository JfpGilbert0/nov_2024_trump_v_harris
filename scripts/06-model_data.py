#### Preamble ####
# Purpose: Models... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 11 February 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load the filtered swing state data
df_swing = pd.read_csv("data/raw_data/swing_state_polls.csv")

# Step 1: Create Binary Target (Trump Win or Lose)
# Pivot the data to compare Trump's and Harris's polling percentages side by side
swing_pivot = df_swing.pivot_table(
    values='pct', 
    index=['state', 'poll_end_date', 'poll_id'],
    columns='candidate_name'
).reset_index()

print(df_swing['candidate_name'].unique())
# Drop any rows with missing values for Trump or Harris
