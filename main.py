"""
Kedilerde İntranasal Medetomidin – Sedasyon Analiz Sistemi
Windows masaüstü uygulaması — PyInstaller ile derlenir
"""
import sys
import os
import threading
import webbrowser
import time
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

APP_DIR = resource_path("app")

class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=APP_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def start_server(port):
    server = HTTPServer(('127.0.0.1', port), SilentHandler)
    server.serve_forever()

def main():
    port = find_free_port()
    url = f"http://127.0.0.1:{port}/index.html"

    t = threading.Thread(target=start_server, args=(port,), daemon=True)
    t.start()
    time.sleep(1.0)

    try:
        import webview
        webview.create_window(
            "Medetomidin Sedasyon Analiz Sistemi",
            url,
            width=1280,
            height=860,
            resizable=True,
            min_size=(900, 600)
        )
        webview.start()
    except Exception:
        webbrowser.open(url)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
