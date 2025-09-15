from flask import Flask, render_template_string, jsonify
import subprocess

app = Flask(__name__)

# Load HTML template
with open("reset.html") as f:
    page_html = f.read()

# Track states
reset_state = "released"
debugger_state = "off"

# Dummy debugger function
def debuggerCtrl(state: str):
    print(f"Debugger control called with state={state}")
    # TODO: replace with real GPIO or process control later


@app.route("/")
def index():
    return render_template_string(page_html)


@app.route("/toggle_reset", methods=["POST"])
def toggle_reset():
    global reset_state
    if reset_state == "released":
        reset_state = "pressed"
        subprocess.Popen(["python3", "your_gpio.py", "press"])
    else:
        reset_state = "released"
        subprocess.Popen(["python3", "your_gpio.py", "release"])
    return jsonify({"state": reset_state})


@app.route("/toggle_debugger", methods=["POST"])
def toggle_debugger():
    global debugger_state
    if debugger_state == "off":
        debugger_state = "on"
        debuggerCtrl("on")
    else:
        debugger_state = "off"
        debuggerCtrl("off")
    return jsonify({"state": debugger_state})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
