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

raw_df = pd.read_csv("data/raw_data/president_polls.csv")

print(raw_df.dtypes)
# restrict to wuality polls only
df = raw_df.loc(raw_df['numeric_grade'] > 2.7)
