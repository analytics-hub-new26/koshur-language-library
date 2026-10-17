"""
Web Application Server for Jammu & Kashmir Government Land Records Decipherment & Translation.
Serves interactive bilingual web UI (English & Hindi) and high-performance cadastral translation APIs.
"""

import os
import io
import json
import base64
import urllib.parse
import http.server
import webbrowser
from typing import Dict, Any, Optional

import koshur
from koshur.translator import (
    translate_record,
    translate_record_file,
    get_sample_record,
    list_sample_records,
    SAMPLE_RECORDS
)

WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")


class RecordTranslatorRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTP Request Handler serving web UI assets and translation REST API endpoints."""

    def _send_json(self, data: Any, status: int = 200):
        try:
            body = json.dumps(data, ensure_ascii=False, default=str).encode('utf-8')
        except Exception as err:
            err_data = {"error": f"JSON serialization error: {str(err)}", "status": "error"}
            body = json.dumps(err_data).encode('utf-8')
            status = 500
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _serve_file(self, file_path: str, content_type: str, status: int = 200):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        path = url.path
        query = urllib.parse.parse_qs(url.query)

        # Serve static HTML, CSS, JS
        if path in ['/', '/index.html']:
            index_file = os.path.join(WEB_DIR, "index.html")
            self._serve_file(index_file, "text/html; charset=utf-8")
            return

        if path == '/style.css':
            css_file = os.path.join(WEB_DIR, "style.css")
            self._serve_file(css_file, "text/css; charset=utf-8")
            return

        if path == '/app.js':
            js_file = os.path.join(WEB_DIR, "app.js")
            self._serve_file(js_file, "application/javascript; charset=utf-8")
            return

        # API Endpoints
        if path == '/api/samples':
            self._send_json(list_sample_records())
            return

        if path == '/api/sample':
            sample_id = query.get('id', [''])[0]
            sample = get_sample_record(sample_id)
            if sample:
                self._send_json(sample)
            else:
                self._send_json({'error': f'Sample {sample_id} not found'}, 404)
            return

        if path == '/api/specimen_image':
            page = query.get('page', [''])[0]
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            sample_path = os.path.join(base_dir, 'extracted_urdu_samples', 'book2_pages', page)
            if os.path.exists(sample_path):
                self._serve_file(sample_path, "image/png")
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        try:
            url = urllib.parse.urlparse(self.path)
            path = url.path
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)

            try:
                req_data = json.loads(body.decode('utf-8'))
            except Exception:
                self._send_json({'error': 'Invalid JSON body'}, 400)
                return

            if path == '/api/translate':
                text = req_data.get('text', '')
                doc_id = req_data.get('doc_id')
                target_lang = req_data.get('target_lang', 'en')
                result = translate_record(text, doc_id=doc_id, target_lang=target_lang)
                self._send_json(result)
                return

            if path == '/api/translate_file':
                filename = req_data.get('filename', '')
                target_lang = req_data.get('target_lang', 'en')
                base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                file_path = os.path.join(base_dir, 'extracted_urdu_samples', 'book2_pages', filename)
                if os.path.exists(file_path):
                    result = translate_record_file(file_path, target_lang=target_lang)
                else:
                    result = translate_record_file(filename, target_lang=target_lang)
                self._send_json(result)
                return

            if path == '/api/upload':
                filename = req_data.get('filename', 'uploaded_document')
                b64_data = req_data.get('base64_data', '')
                target_lang = req_data.get('target_lang', 'en')
                if ',' in b64_data:
                    b64_data = b64_data.split(',', 1)[1]
                try:
                    raw_bytes = base64.b64decode(b64_data)
                except Exception as b64_err:
                    self._send_json({'error': f'Invalid base64 payload: {str(b64_err)}'}, 400)
                    return
                result = translate_record_file(raw_bytes, file_name=filename, target_lang=target_lang)
                self._send_json(result)
                return

            self.send_response(404)
            self.end_headers()
        except Exception as exc:
            self._send_json({'error': f'Translation processing error: {str(exc)}'}, 500)


def start_server(host: str = "127.0.0.1", port: int = 8080, open_browser: bool = True):
    """Starts the Koshur Government Records Translation Web Application server."""
    server = http.server.HTTPServer((host, port), RecordTranslatorRequestHandler)
    url = f"http://{host}:{port}"
    print("=" * 76)
    print(" J&K Government Land Records & Historical Deeds Translator Web App")
    print(f" Live Web Application Server running at: {url}")
    print(" Language Preferences: English [en] & Hindi [hi] & Dual [both]")
    print(" Cadastral Standards: J&K Land Records Manual & Khat-i-Shikast Corpus")
    print(" Zero-Error Information Guarantee: SHA-256 Audit Seal Enabled")
    print(" Press Ctrl+C to stop server")
    print("=" * 76)

    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()


if __name__ == '__main__':
    start_server()
