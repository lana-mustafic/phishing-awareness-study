# training/quiz.py
def run_quiz():
    questions = {
        "Urgent 'password reset' emails should always be trusted. (T/F)": False,
        "Hovering over links shows the real URL. (T/F)": True,
        "'paypal@security-service.com' is a legit sender. (T/F)": False
    }
    
    score = 0
    for q, ans in questions.items():
        while True:
            user_ans = input(f"\n{q} ").strip().upper()
            if user_ans in ('T', 'F'):
                if user_ans == str(ans)[0]: score += 1
                break
            print("Invalid input. Enter T/F.")
    
    print(f"\nScore: {score}/{len(questions)}")
    if score == len(questions):
        print("✅ Perfect! You're phishing-resistant.")
    else:
        print("❌ Training needed! Check https://phishing.org")

if __name__ == "__main__":
    print("=== Phishing Awareness Quiz ===")
    run_quiz()