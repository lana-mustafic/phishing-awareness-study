from flask import Flask, request
from datetime import datetime
import csv
import os

app = Flask(__name__)

# Ensure log directory exists
os.makedirs('logs', exist_ok=True)

@app.route('/track_click')
def track_click():
    # Get tracking parameters
    campaign = request.args.get('campaign', 'unknown')
    sender = request.args.get('sender', 'unknown')
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Anonymize IP (GDPR compliance)
    anonymized_ip = '.'.join(ip.split('.')[0:3]) + '.xxx'
    
    # Log to CSV
    log_entry = [timestamp, anonymized_ip, campaign, sender]
    with open('logs/click_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)
    
    # Show fake error page
    return """
    <h1>404 Page Not Found</h1>
    <p>The requested URL was not found on this server.</p>
    <p style="color:#888;font-size:12px;">
        [This is a simulated page for security training]
    </p>
    """

if __name__ == '__main__':
    app.run(port=5000)
