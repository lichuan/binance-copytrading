#!/bin/bash

echo "启动币安K线图工具..."
echo "Starting Binance Chart Tool..."
echo ""

# 停止之前的服务器
pkill -f "python3 server.py" 2>/dev/null

# 启动服务器
python3 server.py &
SERVER_PID=$!

echo "✅ 服务器已启动 (PID: $SERVER_PID)"
echo ""
echo "请访问以下地址："
echo "----------------------------------------"
echo "http://localhost:8080/"
echo "或"
echo "http://localhost:8080/index.html"
echo "----------------------------------------"
echo ""
echo "按 Ctrl+C 停止服务器"

# 等待3秒后自动打开浏览器
sleep 3
open "http://localhost:8080/index.html"

# 等待用户按Ctrl+C
wait $SERVER_PID