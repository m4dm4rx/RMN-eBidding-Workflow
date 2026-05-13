"""
RMN e-Bidding Tracker — local dev server + API proxy
รัน: python server.py
เปิด: http://localhost:8181/rmn_ebidding_tracker_2.html
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote
import urllib.request, os, sys

PORT = 8181
API_KEY = 'pOZwkh6baWEOuhKOSksDcKxVozruHed7'

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/proxy?'):
            self._proxy()
        else:
            super().do_GET()

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')

    def _proxy(self):
        qs = parse_qs(urlparse(self.path).query)
        target = unquote(qs.get('url', [''])[0])
        if not target.startswith('https://opend.data.go.th/'):
            self.send_response(403)
            self.end_headers()
            return
        try:
            req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self._cors()
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(502)
            self._cors()
            self.end_headers()
            self.wfile.write(str(e).encode())

    def log_message(self, fmt, *args):
        if '/proxy?' in (args[0] if args else ''):
            print(f'  proxy → {args[0][:80]}')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f'Server running at http://localhost:{PORT}/')
print(f'Open: http://localhost:{PORT}/rmn_ebidding_tracker_2.html')
HTTPServer(('', PORT), Handler).serve_forever()
