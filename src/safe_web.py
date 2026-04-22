from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/echo", methods=["POST"])
def echo_payload():
    payload = request.get_json(silent=True) or {}
    # Safe behavior: return parsed JSON without dynamic evaluation.
    return jsonify({"received": payload}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200
