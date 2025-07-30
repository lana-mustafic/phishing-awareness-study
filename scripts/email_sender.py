import smtplib
from email.mime.text import MIMEText

def send_reservation_alert():
    html = """<html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
        <div style="background: #003580; color: white; padding: 15px; margin-bottom: 20px;">
            <h2 style="margin:0;">HOTEL RESERVATION SYSTEM</h2>
        </div>
        <p>Dear Valued Guest,</p>
        <p>We noticed unusual activity on reservation <strong>#A12B34</strong>. Verify within <span style="color:red;">24 hours</span> to avoid cancellation.</p>
        <a href="http://localhost:5000/track_click" style="background: #003580; color: white; padding: 10px 15px; text-decoration: none; border-radius: 3px; display: inline-block; margin: 15px 0;">Verify Reservation</a>
        <p style="color: #777; font-size: 12px; border-top: 1px solid #eee; padding-top: 15px;">
            <em>Simulated email for security training</em>
        </p>
    </body>
    </html>"""
    
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'Action Required: Reservation #A12B34'
    msg['From'] = 'security@notbooking.com'
    msg['To'] = 'recipient@test-hotel.com'
    
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)

def send_password_alert():
    html = """<html>
    <body style="font-family: 'Segoe UI', sans-serif; max-width: 600px; margin: auto;">
        <div style="background: #f8f8f8; padding: 20px; border-left: 4px solid #d32f2f;">
            <h2 style="margin-top: 0; color: #d32f2f;">SECURITY NOTICE</h2>
            <p>Password expires in <strong>3 days</strong> for account <span style="font-family: monospace;">staff@test-hotel.com</span></p>
            <a href="http://localhost:5000/track_click" style="background: #d32f2f; color: white; padding: 12px 20px; text-decoration: none; border-radius: 4px; display: inline-block; font-weight: bold;">Reset Password</a>
        </div>
        <p style="font-size: 11px; color: #999; text-align: center; margin-top: 30px;">
            © 2024 NotBooking Partner Portal
        </p>
    </body>
    </html>"""
    
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'URGENT: Password Reset Required'
    msg['From'] = 'noreply@notbookingportal.com'
    msg['To'] = 'staff@test-hotel.com'
    
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)

def send_payment_alert():
    html = """<html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
        <div style="background: #003580; color: white; padding: 15px;">
            <h3 style="margin:0;">PAYMENT PROCESSING CENTER</h3>
        </div>
        <h4>Declined Transaction</h4>
        <p>Reservation <strong>#XYZ789</strong> will cancel in <span style="color:red;">2 hours</span> unless payment is updated.</p>
        <a href="http://localhost:5000/track_click" style="background: #d32f2f; color: white; padding: 12px 25px; text-decoration: none; border-radius: 4px; display: inline-block;">Update Payment</a>
        <div style="font-size: 11px; color: #777; border-top: 1px solid #eee; margin-top: 20px;">
            <p>Transaction ID: BP-<span style="letter-spacing: 2px;">F4K3</span></p>
        </div>
    </body>
    </html>"""
    
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'CRITICAL: Payment Failed - Reservation #XYZ789'
    msg['From'] = 'payments@bookingpartner.com'
    msg['To'] = 'accounting@test-hotel.com'
    
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)

if __name__ == '__main__':
    # Uncomment ONE at a time to test
    send_reservation_alert()  # Basic
    # send_password_alert()   # Intermediate 
    # send_payment_alert()    # Advanced
