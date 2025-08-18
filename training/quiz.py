# training/quiz.py
questions = [
    {
        "question": "Is 'support@booklng.com' a legitimate Booking.com address?",
        "answer": False,
        "hint": "Always check for typos in the domain (e.g., 'booklng' vs 'booking')"
    },
    {
        "question": "Should you click links in urgent 'password reset' emails?",
        "answer": False,
        "hint": "Legitimate services never ask for credentials via email links"
    }
]

def run_quiz():
    score = 0
    for q in questions:
        user_ans = input(f"\n{q['question']} (T/F): ").strip().upper()
        if user_ans == str(q['answer'])[0]:
            score += 1
        else:
            print(f"❌ Hint: {q['hint']}")
    
    print(f"\nScore: {score}/{len(questions)}")
    if score == len(questions):
        print("✅ Excellent phishing awareness!")
    else:
        print("💡 Review the hints and try again!")