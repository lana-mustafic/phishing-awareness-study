# scripts/analyze_results.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs(log_file="results/responses.csv"):
    # Load data (example format: email,action,timestamp)
    df = pd.read_csv(log_file)
    
    # Basic stats
    click_rate = df[df['action'] == 'clicked'].shape[0] / df.shape[0]
    print(f"Phishing Success Rate: {click_rate:.1%}")

    # Plot results
    df['action'].value_counts().plot(kind='bar', color=['red', 'green'])
    plt.title("Phishing Test Results")
    plt.ylabel("Count")
    plt.savefig("results/plot.png")  # Save for README

if __name__ == "__main__":
    analyze_logs()