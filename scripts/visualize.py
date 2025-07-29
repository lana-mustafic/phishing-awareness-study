# Simple Visualization Script - scripts/visualize.py
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
data = pd.read_csv('../data/sample_results.csv')

# 2. Calculate basic stats
stats = {
    'Clicked Link': data['clicked_link'].mean() * 100,
    'Attempted Login': data['attempted_login'].mean() * 100,
    'Flagged as Phishing': data['flagged_as_phishing'].mean() * 100
}

# 3. Create a simple bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(stats.keys(), stats.values(), color=['red', 'orange', 'green'])

# 4. Add labels and style
plt.title('Phishing Test Results (%)', pad=20)
plt.ylabel('Percentage of Employees')
plt.ylim(0, 100)

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom')

# 5. Save the image
plt.savefig('../docs/results_chart.png', bbox_inches='tight')
print("✅ Chart saved to docs/results_chart.png")
