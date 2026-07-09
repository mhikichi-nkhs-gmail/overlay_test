from flask import Flask, jsonify, send_from_directory
import os
import time

app = Flask(__name__)

SERVER_URL = "http://localhost:5000"

FISH_LIST = [
    {
        "id": "fish1",
        "period": 22,
        "amplitude": 0.45,
        "ycenter": 0,
        "yamp": 0.3,
        "yseed": 1,
        "yperiod": 8,
        "scale": 0.1,
        "phaseoffset": 0,
        "escape": 0.2,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 1,
        "spawnx": 0,
        "image_url": f"{SERVER_URL}/images/fish1.png"
    },
    {
        "id": "fish2",
        "period": 23,
        "amplitude": 0.4,
        "ycenter": 0.2,
        "yamp": 0.25,
        "yseed": 2,
        "yperiod": 5,
        "scale": 0.13,
        "phaseoffset": 0.33,
        "escape": 0.1,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 2,
        "spawnx": 2,
        "image_url": f"{SERVER_URL}/images/fish2.png"
    },
    {
        "id": "fish3",
        "period": 25,
        "amplitude": 0.35,
        "ycenter": -0.3,
        "yamp": 0.4,
        "yseed": 3,
        "yperiod": 10,
        "scale": 0.11,
        "phaseoffset": 0.66,
        "escape": 0.12,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 3,
        "spawnx": -1.5,
        "image_url": f"{SERVER_URL}/images/fish3.png"
    },
    {
        "id": "fish4",
        "period": 20,
        "amplitude": 0.42,
        "ycenter": 0.4,
        "yamp": 0.3,
        "yseed": 4,
        "yperiod": 20,
        "scale": 0.14,
        "phaseoffset": 0.15,
        "escape": 0.1,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 2,
        "spawnx": 0,
        "image_url": f"{SERVER_URL}/images/fish4.png"
    },
    {
        "id": "fish5",
        "period": 19,
        "amplitude": 0.38,
        "ycenter": -0.1,
        "yamp": 0.35,
        "yseed": 5,
        "yperiod": 6,
        "scale": 0.16,
        "phaseoffset": 1,
        "escape": 0.2,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 4,
        "spawnx": 1,
        "image_url": f"{SERVER_URL}/images/fish5.png"
    },
    {
        "id": "fish6",
        "period": 24,
        "amplitude": 0.5,
        "ycenter": 0,
        "yamp": 0.4,
        "yseed": 6,
        "yperiod": 9,
        "scale": 0.2,
        "phaseoffset": 0.34,
        "escape": 0.3,
        "sensitivity": 2,
        "tiltmount": 10,
        "wave": 3,
        "spawnx": 1.2,
        "image_url": f"{SERVER_URL}/images/fish6.png"
    },
    
]


@app.route('/fish/list', methods=['GET'])
def list_fish():
    """URL にキャッシュバスターを付けて返す"""
    timestamp = int(time.time())
    fish_list = []
    for fish in FISH_LIST:
        fish_copy = dict(fish)
        fish_copy['image_url'] = f"{fish['image_url']}?t={timestamp}"
        fish_list.append(fish_copy)
    return jsonify(fish_list)


@app.route('/images/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('images', filename)


@app.route('/')
def index():
    return """
    <h1>Fish Server (Stub)</h1>
    <ul>
        <li><a href="/fish/list">/fish/list</a></li>
        <li><a href="/images/fish1.png">/images/fish1.png</a></li>
    </ul>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)