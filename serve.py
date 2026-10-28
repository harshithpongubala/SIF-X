import http.server
import socketserver
import os
import sys
import socket

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (ConnectionResetError, BrokenPipeError):
            pass

    def do_GET(self):
        # Translate requested path to filesystem
        requested = self.translate_path(self.path)
        # If path does not exist and has no extension, fallback to index.html (SPA routing support)
        if not os.path.exists(requested) and '.' not in os.path.basename(self.path):
            self.path = '/index.html'
        return super().do_GET()

def main():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    lan_ip = get_lan_ip()
    try:
        with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), SPAHandler) as httpd:
            print(f"CIPHER_X_SERVER_READY: http://localhost:{PORT}/")
            print(f"CIPHER_X_LAN_READY:    http://{lan_ip}:{PORT}/")
            sys.stdout.flush()
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
