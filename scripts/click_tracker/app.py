from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/track_click')
def track_click():
    """Logs simulated clicks without storing real data"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Simulated click recorded at {timestamp} from IP: {request.remote_addr}")
    
    # Show a fake "login page" (non-functional)
    return """
    <h1>Booking.com Partner Portal</h1>
    <p style="color:red;">This is a simulated page for security training.</p>
    <p>Study ID: HOTEL_PHISHING_STUDY_2024</p>
    """
