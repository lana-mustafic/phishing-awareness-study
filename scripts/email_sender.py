# Safe phishing email simulator for educational purposes
import smtplib
from email.mime.text import MIMEText

def send_test_email():
    """Sends a simulated phishing email to yourself for testing"""
    # Email content 
    html = """<html>
    <body>
        <p>Dear Hotel Staff,</p>
        <p>Your reservation #12345 requires verification:</p>
        <a href="http://localhost:5000/track_click">Click Here</a>
        <p style="color:#888;font-size:12px;">
            This is a security training simulation from phishing-awareness-study.
        </p>
    </body>
    </html>"""

    msg = MIMEText(html, 'html')
    msg['Subject'] = 'Action Required: Reservation Verification'
    msg['From'] = 'training@notbooking.com'  # Fake sender
    msg['To'] = 'llanamustafic@gmail.com'  # send to your email

    # Send using a TEST SMTP server (no real emails)
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)
        print("Simulated email sent (check MailHog interface)")

if __name__ == '__main__':
    send_test_email()
