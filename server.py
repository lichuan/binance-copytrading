#!/usr/bin/env python3
import json
import http.server
import socketserver
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler

class BinanceProxyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/chart':
            # 获取POST数据
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            params = urllib.parse.parse_qs(post_data.decode('utf-8'))

            symbol = params.get('symbol', ['BTCUSDT'])[0]
            period = params.get('period', ['15m'])[0]

            # 构建币安API URL
            binance_url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={period}&limit=500"

            try:
                # 请求币安API
                with urllib.request.urlopen(binance_url) as response:
                    data = response.read()
                    klines = json.loads(data)

                # 转换为前端期望的格式
                response_data = {
                    'retcode': 0,
                    'data': klines
                }

                # 返回数据给前端
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    PORT = 8080
    with socketserver.TCPServer(("", PORT), BinanceProxyHandler) as httpd:
        print(f"服务器运行在 http://localhost:{PORT}")
        print("按 Ctrl+C 停止服务器")
        httpd.serve_forever()