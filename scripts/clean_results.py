# scripts/clean_results.py
import pandas as pd

def clean_csv():
    # Read raw data with error handling
    try:
        df = pd.read_csv("results/responses.csv", error_bad_lines=False)
    except:
        # Manual cleanup if pandas fails
        with open("results/responses.csv", 'r') as f:
            lines = f.readlines()
        
        # Keep only properly formatted lines
        clean_lines = [line for line in lines if line.count(',') == 3]
        
        with open("results/clean_responses.csv", 'w') as f:
            f.writelines(clean_lines)
        
        df = pd.read_csv("results/clean_responses.csv")

    # Save cleaned data
    df.to_csv("results/clean_responses.csv", index=False)
    print("✅ Cleaned data saved to 'results/clean_responses.csv'")

if __name__ == "__main__":
    clean_csv()