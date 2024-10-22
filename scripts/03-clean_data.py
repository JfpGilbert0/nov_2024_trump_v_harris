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


# restrict to wuality polls only
df = raw_df.loc[raw_df['numeric_grade'] >= 2.5]
df['exam_date'] = pd.to_datetime(df['end_date'], format='%m/%d/%y')

df_swing = df.loc[df["state"].isin(["Arizona","Pennsylvania", "North Carolina", "Georgia", "Nevada", "Michigan", "Wisconsin"])]
print(df.count())
unique_values = df_swing['state'].unique()

# Print unique values and their counts
print("Unique values:")
for value in unique_values:
    count = (df_swing['state'] == value).sum()
    print(f"{value}: {count}")

print(df_swing["numeric_grade"].min())

df_swing.to_csv("data/raw_data/swing_state_polls.csv")


