import logging
from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename="sherlock_app.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger().addHandler(logging.StreamHandler())

# Directory for output files
BASE_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# State to track if a scan is running
scan_in_progress = False

@app.route("/")
def index():
    logging.info("Index page accessed.")
    return render_template("index.html")

@app.route("/run_sherlock", methods=["GET"])
def run_sherlock():
    global scan_in_progress
    username = request.args.get("username")
    if not username:
        logging.warning("No username provided.")
        return jsonify({"error": "No username provided"}), 400

    if scan_in_progress:
        logging.warning("Scan already in progress.")
        return jsonify({"error": "A scan is already in progress. Please wait."}), 400

    logging.info(f"Starting scan for username: {username}")
    scan_in_progress = True
    try:
        output_dir = os.path.join(OUTPUT_DIR, username)
        os.makedirs(output_dir, exist_ok=True)

        command = [
            "python3",
            "-m",
            "sherlock_project",
            username,
            "--folderoutput", output_dir
        ]

        # Add additional options dynamically based on frontend input
        if request.args.get("csv") == "true":
            command.append("--csv")
        if request.args.get("xlsx") == "true":
            command.append("--xlsx")
        if request.args.get("print_all") == "true":
            command.append("--print-all")
        if request.args.get("print_found") == "true":
            command.append("--print-found")

        process = subprocess.run(command, text=True, capture_output=True)

        if process.returncode != 0:
            logging.error(f"Sherlock failed: {process.stderr}")
            scan_in_progress = False
            return jsonify({"error": f"Error running Sherlock: {process.stderr}"}), 500

        logging.info(f"Scan completed successfully for username: {username}")
        json_report = f"/output/{username}/{username}.txt"
        
        return jsonify({
            "message": f"Scan completed for {username}",
            "json_report": json_report
        })

    except Exception as e:
        logging.exception("Unexpected error during scan.")
        scan_in_progress = False
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
    finally:
        scan_in_progress = False

@app.route("/output/<username>/<path:filename>")
def serve_report(username, filename):
    logging.info(f"Serving file: {filename} for username: {username}")
    user_output_dir = os.path.join(OUTPUT_DIR, username)
    return send_from_directory(user_output_dir, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
