import smtplib
from email.mime.text import MIMEText

# List of sender variants to test
SENDER_VARIANTS = [
    "bookings@notbooking.com",      # Misspelled
    "support@booking-com.com",      # Hyphen trick
    "security@booking.secure.com",  # Fake subdomain
    "noreply@b00king.com",          # Char substitution
    "reservations@bookings.com",    # Plural domain
    "support@booking.com"           # Legitimate control
]

def send_test_email(sender_variant, recipient="staff@test-hotel.com"):
    """Sends email with tracking for a specific sender variant"""
    campaign = "hotel_phishing_study"
    
    html = f"""<html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
        <div style="background: #003580; color: white; padding: 15px;">
            <h2 style="margin:0;">RESERVATION SYSTEM</h2>
        </div>
        <p>Dear Staff,</p>
        <p>Your recent booking requires verification:</p>
        <a href="http://localhost:5000/track_click?campaign={campaign}&sender={sender_variant}" 
           style="background: #003580; color: white; padding: 10px 15px; text-decoration: none; border-radius: 3px; display: inline-block; margin: 15px 0;">
           Verify Account
        </a>
        <p style="color: #777; font-size: 12px; border-top: 1px solid #eee; padding-top: 15px;">
            <em>This is a security training simulation from IT Department</em>
        </p>
    </body>
    </html>"""
    
    msg = MIMEText(html, 'html')
    msg['Subject'] = f"Action Required: Account Verification ({sender_variant})"
    msg['From'] = sender_variant
    msg['To'] = recipient
    
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)
        print(f"Sent test email from: {sender_variant}")

if __name__ == '__main__':
    # Test all variants (or comment out ones you don't need)
    for sender in SENDER_VARIANTS:
        send_test_email(sender)
