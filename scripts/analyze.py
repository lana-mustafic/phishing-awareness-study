# Simple Data Analyzer - scripts/analyze.py
import pandas as pd

print("📊 Basic Phishing Results Analysis")

# Load data
data = pd.read_csv('../data/sample_results.csv')

# Calculate stats
click_rate = data['clicked_link'].mean() * 100
login_rate = data['attempted_login'].mean() * 100
detection_rate = data['flagged_as_phishing'].mean() * 100

# Print results
print(f"\n🔗 Click Rate: {click_rate:.1f}%")
print(f"🔐 Login Attempt Rate: {login_rate:.1f}%")
print(f"🛡️ Detection Rate: {detection_rate:.1f}%")
