from flask import Flask, render_template_string, jsonify
import subprocess
import servoCtrl

#┌────────────────┬────────────────┐
#│  1: 3.3V       │ 5V           2 │ ecu_reset5V
#│  3: GPIO2 SDA  │ 5V           4 │ speed_box5V
#│  5: GPIO3 SCL  │ GND          6 │ ecu_resetGnd
#│  7: GPIO4 GP   │ GPIO14 TXD   8 │
#│  9: GND        │ GPIO15 RXD  10 │
#│ 11: GPIO17 GP  │ GPIO18 PWM  12 │ ecu_resetPwm
#│ 13: GPIO27 GP  │ GND         14 │ speed_boxGnd
#│ 15: GPIO22 GP  │ GPIO23 GP   16 │
#│ 17: 3.3V       │ GPIO24 GP   18 │
#│ 19: GPIO10 MOSI│ GND         20 │
#│ 21: GPIO9 MISO │ GPIO25 GP   22 │
#│ 23: GPIO11 SCLK│ GPIO8 CE0   24 │
#│ 25: GND        │ GPIO7 CE1   26 │
#│ 27: GPIO0 ID_SD│ GPIO1 ID_SC 28 │
#│ 29: GPIO5 GP   │ GND         30 │
#│ 31: GPIO6 GP   │ GPIO12 PWM  32 │ speed_boxPwm
#│ 33: GPIO13 PWM │ GND         34 │
#│ 35: GPIO19 PWM │ GPIO16 GP   36 │
#│ 37: GPIO26 GP  │ GPIO20 GP   38 │
#│ 39: GND        │ GPIO21 GP   40 │
#└────────────────┴────────────────┘

app = Flask(__name__)

# Load HTML template
with open("reset.html") as f:
    page_html = f.read()

# Track states
reset_state = "released"
debugger_state = "off"

# Initialize PWMs
speed_box_servo_pin = 12
ecu_reset_servo_pin = 18
pwm_speed_box = servoCtrl.init_servos(speed_box_servo_pin,25)
pwm_ecu_reset = servoCtrl.init_servos(ecu_reset_servo_pin)
speed_box_servo_angle = 20
ecu_reset_servo_angle = 90

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
        servoCtrl.set_angle(pwm_ecu_reset,ecu_reset_servo_angle)
        #subprocess.Popen(["python3", "your_gpio.py", "press"])
    else:
        reset_state = "released"
        servoCtrl.set_angle(pwm_ecu_reset,0)
        #subprocess.Popen(["python3", "your_gpio.py", "release"])
    return jsonify({"state": reset_state})


@app.route("/toggle_debugger", methods=["POST"])
def toggle_debugger():
    global debugger_state
    if debugger_state == "off":
        debugger_state = "on"
        servoCtrl.set_angle(pwm_speed_box,3)
    else:
        debugger_state = "off"
        servoCtrl.set_angle(pwm_speed_box,speed_box_servo_angle)
    return jsonify({"state": debugger_state})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
