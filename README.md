# 🤖 Hexapod Robot Controller

This repository contains Python code to control a **hexapod robot** — a six-legged walking robot with 18 degrees of freedom (3 servo motors per leg). The robot runs on a Raspberry Pi and can be controlled via SSH after deployment.

## 📦 Features

- 🦿 Six legs, each with 3 servo motors (18 DOF total)
- 🐍 Python-based control logic
- 🎛️ Modular code for different walking gaits
- 📡 Easy deployment to Raspberry Pi via SSH

## 🧰 Hardware Requirements

- Raspberry Pi (any model with Wi-Fi and GPIO support)
- 18 servo motors (e.g., SG90, MG90S, or MG996R)
- External 5V power supply (2A+ recommended)
- Servo controller board (e.g., PCA9685) — optional but recommended
- Breadboard & jumper wires (if not using a controller board)

## 📂 Software Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `RPi.GPIO`
  - `adafruit-circuitpython-pca9685` _(if using PCA9685)_
  - `numpy` _(optional, for calculations)_

Install dependencies via `pip`:

```
pip install RPi.GPIO adafruit-circuitpython-pca9685 numpy
```

Or use the included `requirements.txt`:

```
pip install -r requirements.txt
```

## 🚀 Setup & Deployment

1. **Clone the repository (on your local machine):**

```
git clone https://github.com/your-username/hexapod-robot.git
cd hexapod-robot
```

2. **Transfer the code to your Raspberry Pi:**
   Use `scp` to securely copy all files:

```
scp -r . pi@<raspberry_pi_ip>:/home/pi/hexapod-robot/
```

Replace `<raspberry_pi_ip>` with your Raspberry Pi's IP address. Example:

```
scp -r . pi@192.168.1.100:/home/pi/hexapod-robot/
```

💡 Ensure SSH is enabled on the Pi: Run `sudo raspi-config` → Interface Options → SSH → Enable

3. **SSH into the Raspberry Pi:**

```
ssh pi@<raspberry_pi_ip>
cd ~/hexapod-robot
```

4. **Install dependencies:**

```
pip install -r requirements.txt
```

5. **Run the robot control script:**

```
python main.py
```

## 🧪 Testing Tips

- Run basic servo sweep tests before executing walking sequences.
- Use debug flags in the code to simulate movement without powering servos.
- Ensure your servo power supply is stable — voltage drops can cause erratic behavior or reboots.

## Unit Tests
```
pytest tests/ -v
/Users/cyrus/Library/Python/3.9/bin/pytest tests/ -v
```

## 🖼️ Demo

_(Add images or video links here showing the robot walking or performing tasks)_

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute improvements, bug fixes, or new features, feel free to fork the repository and open a PR.

---

Let me know if you'd like to include:

- Wiring diagrams
- A simulation environment
- Preconfigured Raspberry Pi images

These can all be added to enhance the documentation.
