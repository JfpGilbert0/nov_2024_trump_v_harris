#### Preamble ####
# Purpose: Simulates election polling data
# Author: Alexander Guarasci & Jacob Gilbert
# Date: November 4, 2024
# Contact: alexander.guarasci@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)
  # - `sklearn` must be installed (pip install sklearn)

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
