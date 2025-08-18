import yagmail
import argparse

def send_phishing_email(target_email, template_path):
    """Send a simulated phishing email."""
    with open(template_path, 'r') as f:
        html_content = f.read()
    
    yag = yagmail.SMTP('lanamustafic07@gmail.com', 'kyee zlob ntms rajw')  # Fixed indentation (4 spaces)
    yag.send(
        to=target_email,
        subject="URGENT: Reservation Cancellation",
        contents=html_content
    )
    print(f"Sent phishing test to {target_email}")  # Fixed: Use variable, not email string

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="Target email address", required=True)
    parser.add_argument("--template", help="Path to HTML template", default="data/booking_phish.html")
    args = parser.parse_args()
    send_phishing_email(args.target, args.template)