from flask import Flask, jsonify
import platform
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "System Health API is running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/info")
def info():
    return jsonify({
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
        "hostname": platform.node()
    })


@app.route("/app-info")
def appinfo():
    return jsonify({
        "application": "devops-app",
        "framework": "Flask",
        "version": "1.0.0"
    })


@app.route("/random-image")
def random_image():
    return jsonify({
        "image_url": f"https://picsum.photos/400?seed={time.time_ns()}"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
