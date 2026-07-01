from flask import Flask, jsonify
import platform
import os
import socket
import time

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():
    return jsonify({
        "application": "devops-system-api",
        "status": "running",
        "message": "System Diagnostics API is operational"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/system")
def system():
    return jsonify({
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": platform.python_version()
    })


@app.route("/app-info")
def app_info():
    return jsonify({
        "application": "devops-system-api",
        "framework": "Flask",
        "version": "1.0.0",
        "ci_platform": "GitHub Actions",
        "containerized": True
    })


@app.route("/environment")
def environment():
    return jsonify({
        "port": os.environ.get("PORT", "5000"),
        "hostname": os.environ.get("HOSTNAME", "Unknown")
    })


@app.route("/uptime")
def uptime():
    return jsonify({
        "uptime_seconds": round(time.time() - START_TIME, 2)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
