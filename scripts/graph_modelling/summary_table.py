import pandas as pd
from tabulate import tabulate

# Load the data (replace with your parquet file path)
df = pd.read_parquet('data/02-analysis_data/merged_swing_state_data.parquet')

# Group by state and calculate summary statistics
summary_stats = df.groupby('state').agg(
    numeric_grade_mean=('numeric_grade', 'mean'),
    numeric_grade_std=('numeric_grade', 'std'),
    numeric_grade_min=('numeric_grade', 'min'),
    numeric_grade_max=('numeric_grade', 'max'),
    numeric_grade_count=('numeric_grade', 'count'),
    sample_size_mean=('sample_size', 'mean'),
    sample_size_std=('sample_size', 'std'),
    sample_size_min=('sample_size', 'min'),
    sample_size_max=('sample_size', 'max'),
    sample_size_count=('sample_size', 'count')
).reset_index()

# Reshape the summary table to long format
summary_long = pd.melt(
    summary_stats,
    id_vars='state',
    value_vars=[
        'numeric_grade_mean', 'numeric_grade_std', 'numeric_grade_min', 'numeric_grade_max', 'numeric_grade_count',
        'sample_size_mean', 'sample_size_std', 'sample_size_min', 'sample_size_max', 'sample_size_count'
    ],
    var_name='variable_stat', value_name='value'
)

# Split 'variable_stat' into 'variable' and 'stat'
summary_long[['variable', 'stat']] = summary_long['variable_stat'].str.rsplit('_', n=1, expand=True)

# Drop the original column
summary_long.drop('variable_stat', axis=1, inplace=True)

# Pivot the table to get desired output
summary_pivot = summary_long.pivot_table(
    index=['state', 'variable'], columns='stat', values='value', aggfunc='first'
).reset_index()

# Sort for better readability
summary_pivot = summary_pivot.sort_values(by=['state', 'variable'])

# Create a list of rows for tabulate (merging state rows visually)
rows = []
last_state = None
for _, row in summary_pivot.iterrows():
    state = row['state']
    variable = row['variable']
    mean, std, min_, max_, count = row['mean'], row['std'], row['min'], row['max'], row['count']
    
    # Only show state name on the first row of each group
    if state == last_state:
        state = ''
    else:
        last_state = state

    rows.append([state, variable, mean, std, min_, max_, count])

# Print the table using tabulate
print(tabulate(rows, headers=['State', 'Variable', 'Mean', 'Std', 'Min', 'Max', 'Count'], tablefmt='fancy_grid'))
