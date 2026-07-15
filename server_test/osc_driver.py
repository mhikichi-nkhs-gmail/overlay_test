"""
最小限の OSC 送信スクリプト
"""
from pythonosc import udp_client
import argparse
import random
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)


def send_touch(x, y):
    """指定した座標にタッチイベントを送信"""
    client.send_message("/touch", [1, x, y])
    time.sleep(0.5)
    client.send_message("/touch", [0, x, y])
    print(f'Touch at ({x:.2f}, {y:.2f})')


def main():
    parser = argparse.ArgumentParser(description="OSC タッチイベント送信スクリプト")
    parser.add_argument("--x", type=float, default=None, help="タッチする X 座標")
    parser.add_argument("--y", type=float, default=None, help="タッチする Y 座標")
    args = parser.parse_args()

    if args.x is not None and args.y is not None:
        send_touch(args.x, args.y)
        return

    # 座標が指定されていない場合は 5 秒ごとにランダムタッチ
    while True:
        x = random.uniform(-0.3, +0.3)
        y = random.uniform(-0.5, 0.5)

        send_touch(x, y)
        time.sleep(1)


if __name__ == "__main__":
    main()