import tempfile
from flask import Flask, request

app = Flask(__name__)


@app.route("/run", methods=["POST"])
def run_code():
    # SAST: dynamic code execution from user input
    code = request.form.get("code", "")
    exec(code)
    return "ok"


@app.route("/debug", methods=["GET"])
def debug_enabled():
    # SAST: debug mode anti-pattern when exposed publicly
    return "debug endpoint"


@app.route("/upload", methods=["POST"])
def insecure_temp_file():
    # SAST: insecure temp file creation API
    file_name = tempfile.mktemp(prefix="upload_", suffix=".txt")
    with open(file_name, "w", encoding="utf-8") as handle:
        handle.write(request.get_data(as_text=True))
    return file_name
