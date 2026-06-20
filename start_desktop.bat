@echo off
chcp 65001 >nul 2>&1
title Pixelle-Video Desktop

cd /d "%~dp0"
echo 🚀 Đang khởi động Pixelle-Video Desktop...
echo.
echo ⓵ Đảm bảo đã tắt Streamlit cũ (nếu có)
taskkill /f /im streamlit.exe >nul 2>&1

echo ⓶ Khởi động app desktop...
call .venv\Scripts\python.exe desktop_app.py

pause
