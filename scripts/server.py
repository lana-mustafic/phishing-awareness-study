# server.py (fixed)
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import csv
import urllib.parse

class ClickTracker(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/track'):
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)  # Fixed: Added closing )
            email = params.get('email', [''])[0]
            tracking_id = params.get('id', [''])[0]
            
            with open('results/responses.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().isoformat(), email, 'clicked', tracking_id])
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Click logged')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), ClickTracker)
    print("Click tracker running on port 8000...")
    server.serve_forever()