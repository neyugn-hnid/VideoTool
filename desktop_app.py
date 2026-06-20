"""
Pixelle-Video Desktop App
Chạy Streamlit trong cửa sổ desktop riêng, không cần trình duyệt.
"""

import sys
import os
import threading
import time
import subprocess
import webview

# Đường dẫn gốc
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STREAMLIT_PORT = 8501
STREAMLIT_URL = f"http://localhost:{STREAMLIT_PORT}"


def start_streamlit():
    """Chạy Streamlit server trong background"""
    venv_python = os.path.join(ROOT_DIR, ".venv", "Scripts", "python.exe")
    app_path = os.path.join(ROOT_DIR, "web", "app.py")
    
    # Đảm bảo dùng đúng Python từ venv
    if not os.path.exists(venv_python):
        venv_python = sys.executable
    
    subprocess.run([
        venv_python, "-m", "streamlit", "run", app_path,
        "--server.port", str(STREAMLIT_PORT),
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false",
    ], cwd=ROOT_DIR)


class WebViewApp:
    def __init__(self):
        self.running = True
    
    def on_closing(self):
        self.running = False
        # Tắt Streamlit khi đóng app
        os._exit(0)


def main():
    print("🚀 Đang khởi động Pixelle-Video Desktop...")
    
    # Chạy Streamlit trong luồng riêng
    t = threading.Thread(target=start_streamlit, daemon=True)
    t.start()
    
    # Đợi Streamlit sẵn sàng
    import urllib.request
    for i in range(30):
        try:
            urllib.request.urlopen(STREAMLIT_URL)
            print(f"✅ Streamlit đã sẵn sàng tại {STREAMLIT_URL}")
            break
        except:
            time.sleep(1)
    else:
        print("❌ Không thể khởi động Streamlit")
        return
    
    # Tạo cửa sổ desktop (dùng PyWebView)
    app = WebViewApp()
    webview.create_window(
        title="Pixelle-Video",
        url=STREAMLIT_URL,
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
    )
    webview.start()


if __name__ == "__main__":
    main()
