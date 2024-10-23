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
df = raw_df[selected_columns]

# Filter the raw data
df = df.loc[df['numeric_grade'] >= 2.5]
df = df[df['candidate_name'].isin(['Donald Trump', 'Kamala Harris'])]
#filter the recent 
df['poll_end_date'] = pd.to_datetime(df['end_date'], format='%m/%d/%y')
df = df.loc[df["poll_end_date"] > "2024-09-01"]

df_swing = df.loc[df["state"].isin(["Arizona","Pennsylvania", "North Carolina", "Georgia", "Nevada", "Michigan", "Wisconsin"])]

print(df.count())
unique_values = df_swing['state'].unique()

# Print unique values and their counts
print("Unique values:")
for value in unique_values:
    count = (df_swing['state'] == value).sum()
    print(f"{value}: {count}")

# Create an id for tracking which results match
id_columns = ["poll_id","question_id"]
df_swing['unique_id'] = df_swing[id_columns].astype(str).agg('-'.join, axis=1)
print(df_swing['unique_id'].nunique())

print(df_swing["numeric_grade"].min())
# save raw swing stat data
df_swing.to_csv("data/02-analysis_data/swing_state_polls.csv")

#creating data to be analysed (grouping by )
df_trump = df_swing[df_swing['candidate_name'] == "Donald Trump"]
df_harris = df_swing[df_swing['candidate_name'] == "Kamala Harris"]


df_by_poll = pd.merge(df_trump[['unique_id',
    'poll_id',
    'question_id',
    'pollster',
    'numeric_grade',
    'pollscore',
    'methodology',
    'transparency_score',
    'state',
    'start_date',
    'end_date',
    'sample_size',
    'population', 'pct']],
    df_harris[['unique_id', 'pct']], on='unique_id', how='inner')
df_merged = df_by_poll.rename(columns={'pct_x': 'trump_pct', 'pct_y': 'harris_pct'}, inplace=True)

df_by_poll.to_csv("data/02-analysis_data/merged_swing_state_data.csv")
