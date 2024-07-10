import os
import subprocess
import requests
import time

def start_ngrok():
    # Ngrok'u başlat
    ngrok = subprocess.Popen(['ngrok', 'http', '5000'])
    time.sleep(5)  # Ngrok'un başlatılması için bekle

    # Tünel URL'sini al
    url = requests.get('http://localhost:4040/api/tunnels').json()['tunnels'][0]['public_url']
    print(f"Ngrok Tunnel URL: {url}")

if __name__ == "__main__":
    start_ngrok()
    os.system("flask run --host=0.0.0.0")
