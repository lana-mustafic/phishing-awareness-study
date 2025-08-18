import yagmail
import argparse
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import quote

def send_phishing_email(target_email, template_path):
    """Send a tracked phishing simulation email."""
    # Load email credentials securely
    load_dotenv()
    yag = yagmail.SMTP(os.getenv('EMAIL'), os.getenv('APP_PASSWORD'))
    
    # Read and modify the template
    with open(template_path, 'r') as f:
        html_content = f.read()
    
    # Generate unique tracking tokens
    tracking_id = str(uuid.uuid4())
    encoded_email = quote(target_email)
    
    # Replace placeholders in the HTML
    tracked_html = html_content.replace(
        'href="https://your-fake-domain.com/phish-test"',
        f'href="http://localhost:8000/track?email={encoded_email}&id={tracking_id}"'
    ).replace(
        'reservation #12345',
        f'reservation #{tracking_id[:8].upper()}'
    )
    
    # Log the sent email
    log_action(target_email, "sent", tracking_id)
    
    # Send the email
    yag.send(
        to=target_email,
        subject="URGENT: Reservation Cancellation - Action Required",
        contents=tracked_html
    )
    print(f"Sent phishing test to {target_email} (Tracking ID: {tracking_id})")

def log_action(email, action, tracking_id=None):
    """Log all actions to CSV with proper escaping."""
    os.makedirs("results", exist_ok=True)
    
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'email': email.replace(',', ';'),
        'action': action,
        'tracking_id': tracking_id or ''
    }
    
    # Write headers if file doesn't exist
    file_exists = os.path.exists("results/responses.csv")
    
    with open("results/responses.csv", "a") as log:
        if not file_exists:
            log.write("timestamp,email,action,tracking_id\n")
        log.write(f"{log_entry['timestamp']},{log_entry['email']},{log_entry['action']},{log_entry['tracking_id']}\n")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Run a phishing awareness simulation",
        epilog="Example: python send_phishing.py --target test@example.com"
    )
    parser.add_argument("--target", required=True, help="Target email address")
    parser.add_argument("--template", default="data/booking_phish.html", 
                      help="Path to HTML template")
    args = parser.parse_args()
    
    # Validate template exists
    if not os.path.exists(args.template):
        print(f"Error: Template file not found at {args.template}")
        exit(1)
        
    send_phishing_email(args.target, args.template)