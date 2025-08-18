# scripts/analyze_results.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    try:
        # Load the cleaned data with explicit column names
        df = pd.read_csv("results/clean_responses.csv", 
                        header=None,
                        names=['timestamp', 'email', 'action', 'tracking_id'])
        
        # Calculate metrics (case-insensitive check)
        total_sent = df[df['action'].str.lower() == 'sent'].shape[0]
        total_clicks = df[df['action'].str.lower() == 'clicked'].shape[0]
        
        # Generate report
        print("\n📊 Phishing Test Results:")
        print(f"- Emails Sent: {total_sent}")
        print(f"- Clicks Recorded: {total_clicks}")
        
        if total_sent > 0:
            click_rate = (total_clicks / total_sent) * 100
            print(f"- Click Rate: {click_rate:.1f}%")
        else:
            print("- No sent emails found in data")
        
        # Visualization (if we have both types)
        if not df.empty:
            value_counts = df['action'].value_counts()
            if len(value_counts) > 0:
                value_counts.plot(kind='bar', color=['red', 'green'])
                plt.title("Phishing Test Results")
                plt.ylabel("Count")
                plt.savefig("results/phishing_results.png")
                print("\n✅ Saved visualization to 'results/phishing_results.png'")
            else:
                print("\nℹ️ No action data to visualize")
        else:
            print("\nℹ️ No data available for analysis")

    except Exception as e:
        print(f"\n❌ Error during analysis: {str(e)}")
        print("Please check your clean_responses.csv format")

if __name__ == "__main__":
    analyze_data()