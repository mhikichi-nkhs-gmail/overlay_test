"""
最小限の OSC 送信スクリプト
"""
from pythonosc import udp_client
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

# 5 秒ごとにランダムタッチ
import random
while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-0.5, 0.5)
    
    client.send_message("/touch", [1,x, y])
    time.sleep(0.5)
    client.send_message("/touch", [0,x, y])
    print(f'Touch at ({x:.2f}, {y:.2f})')
    
    time.sleep(1)