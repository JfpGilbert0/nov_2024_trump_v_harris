import matplotlib.pyplot as plt
import numpy as np

# Step 1: Define the Electoral Votes for Each State
states = ['California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Hawaii', 'Illinois', 
          'Maryland', 'Massachusetts', 'Minnesota', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',  
          'Oregon', 'Washington', 'Arizona', 'Pennsylvania', 'North Carolina', 'Georgia', 'Nevada', 'Michigan', 
          'Wisconsin', 'Washington', 'Alabama', 'Alaska', 'Arkansas', 'Florida', 'Idaho', 'Indiana', 'Iowa', 
          'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 
          'North Dakota', 'Ohio', 'Oklahoma', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 
          'West Virginia', 'Wyoming']
print(len(states))
votes = [54, 10, 7, 3, 3, 4, 19, 10, 11, 10, 4, 14, 5, 28, 8, 11, 19, 16, 16, 6, 15, 10, 
         12, 9, 3, 6, 30, 4, 11, 6, 6, 8, 8, 4, 6, 10, 4, 5, 3, 17, 7, 9, 3, 11, 40, 6, 
         3, 10, 3]
print(len(votes))
# Step 2: Compute the Cumulative Electoral Votes
cumulative_votes = np.cumsum(votes)

# Compute Cumulative Votes in Reverse Order for Republicans
cumulative_votes_reversed = np.cumsum(votes[::-1])

# X-axis values (state index)
x = np.arange(len(cumulative_votes))

# Step 3: Plot the Step Function for Democrats (left to right)
plt.figure(figsize=(18, 8))
plt.step(x, cumulative_votes, where='post', color='navy', linewidth=2, marker='o')

# Reverse the x-axis for the Republican step function (right to left)
x_reversed = np.flip(x)
plt.step(x_reversed, cumulative_votes_reversed, where='post', color='red', linewidth=2, marker='o')

# Step 4: Customize the Plot
plt.xticks(range(len(states)), states, rotation=90, fontsize=8)
plt.yticks(np.arange(0, 550, 50))

# Fill the area under the curve with blue for Democrats (left to right)
threshold_index = np.argmax(cumulative_votes >= 226)  # First point where cumulative votes reach 270
plt.fill_between(x[:threshold_index + 1], cumulative_votes[:threshold_index + 1], 
                 step='post', color='blue', alpha=0.4)

# Fill the area under the curve with red for Republicans (right to left)
plt.fill_between(x_reversed, cumulative_votes_reversed, step='post', color='red', alpha=0.4)

# Add a horizontal line at 270 votes (threshold to win)
plt.axhline(270, color='purple', linestyle='--', linewidth=2)
plt.text(len(states) / 2, 275, '270 votes to win', horizontalalignment='center', color='purple', fontsize=12)

# Add lines for current Democratic and Republican thresholds
plt.axhline(225, color='blue', linestyle='--', linewidth=1.5)
plt.text(210, 220, '225 votes', horizontalalignment='center', color='blue', fontsize=12)

# Add Labels and Title
plt.xlabel('Electoral College Markets (electoral votes)', fontsize=12)
plt.ylabel('Total Electoral Votes', fontsize=12)
plt.title('Step Function of Total Electoral Votes\nwith States Ordered by Vote Share', fontsize=15)

# Add Grid for Better Visibility
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust Layout for Better Fit
plt.tight_layout()

# Step 5: Show the Plot
plt.show()
