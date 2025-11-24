# ⚡ Arduino PushBlink & Switcher

Two milestones in my journey into **physical computing** —  
two small but meaningful projects where **software, electricity, and curiosity** finally meet.

It started with **Python** and a single LED.  
It grew into **C++ logic** running directly on the hardware.  
Each step felt like discovering a deeper layer of engineering —  
from blinking light to thinking machine.

This repo captures that evolution:  
**from Push & Blink (Python + PyFirmata)** →  
**to Switcher (pure C++ running inside the Arduino).**

---

## 🌟 Project Overview

This repository contains two independent but connected modules:

### 🔵 1. Push_and_Blink  
My first real interaction with hardware:  
a button, an LED, a breadboard — and Python acting as the bridge.

- Hold the button → LED ON  
- Release → LED OFF  

Simple, clean, and absolutely magical the first time you see it happen.  
A moment where code stops being abstract and becomes **alive**.

### 🟢 2. Switcher (C++ Arduino Logic)  
The next level: pushing logic onto the microcontroller itself.  
No Python in the loop.  
No serial link.  
Just C++, embedded thinking, and raw electric behavior.

A button now becomes a **toggle switch**:
- First press → LED ON  
- Second press → LED OFF  

A true state machine running at microsecond scale.  
This is where hardware stops being “a board” and becomes “a system.”

---

## 📂 Repository Structure


```
ARDUINO_PUSHBLINK/
│
├── Push_and_Blink/
│   ├── ARDUINO_kod.py
│   ├── diagram.drawio.png
│   ├── real_system_photo.jpg
│   └── requirements.txt
│
├── Switcher/
│   ├── 2D_model.jpg
│   └── ARDUINO_switcher.cpp
│
├── LICENSE
└── README.md
```

---

## 🔧 Push_and_Blink (Python + PyFirmata)

This folder contains the **first version** of the project.  
A minimal feedback loop:

**human → hardware → Python → Arduino → hardware**

The LED responds instantly to the button input.  
No state machine, no toggling, no logic — just raw interaction.

### 📸 Diagram & Real Hardware
- `diagram.drawio.png` — the breadboard schematic I drew manually in Draw.io  
- `real_system_photo.jpg` — a photo of the real setup running on a physical Arduino

### 🧠 Python Script  
This code runs on the computer.  
Arduino becomes a “remote-controlled I/O device.”

```python
from pyfirmata import Arduino, util
...
```

### 🔌 Requirements

```bash
pip install pyfirmata==1.1.0
```

Compatible only with **Python 3.10 or lower**  
(PyFirmata does not support 3.11+).

---

## ⚙️ Switcher (C++ Embedded Logic)

This is where things get interesting.

The `Switcher/` folder contains:

- `ARDUINO_switcher.cpp` — the C++ program written for the Arduino  
- `2D_model.jpg` — my schematic of the new toggle-switch circuit (made in Tinkercad)

Here, the Arduino is no longer just listening —  
it is **thinking**.

This project uses:

- button as a digital input  
- LED as a digital output  
- a pull-down resistor  
- state variables (`on_off`, `last_state`, `current_state`)  
- logic that detects **transitions**, not just levels  

That transition-detection is the key.  
It makes the LED behave like a real household switch — ON/OFF with each press.

---

## 🔌 How the Hardware Works

### Power rails  
- **+5V** from Arduino → red rail  
- **GND** from Arduino → blue rail  

### Button (D2 input)  
- One side of the button → +5V rail  
- Other side → D2  
- D2 → 10kΩ resistor → GND  
  (this creates a clean pull-down)

When the button is pressed:  
D2 goes HIGH → Arduino detects the transition → toggles LED state.

### LED (D13 output)  
- D13 → LED (anode)  
- LED (cathode) → 220Ω resistor → GND  

D13 HIGH = LED ON  
D13 LOW = LED OFF  

A classic, safe current-limited LED circuit.

---

## 🧠 What I Learned

This repo represents my first steps into:

- Python-based hardware control  
- physical breadboarding  
- reading digital inputs  
- using pull-down resistors  
- writing embedded C++  
- implementing state machines  
- handling input transitions  
- understanding how loops in microcontrollers work  
- building 2D schematics  
- debugging logic in real time  

It started as  
“Why is my LED blinking?”  
and became  
“I can design logic systems that run directly on silicon.”

---

## 🚀 Why This Repository Matters to Me

This project symbolizes the moment I stopped being “a person who writes Python scripts”  
and became “a person who can make electrons obey logic.”

It’s not about the button or the LED.  
It’s about the feeling when hardware responds to your mind.  
It’s the realization:

> You are not just coding anymore.  
> You are communicating with matter.

---

## 🔮 Future Work

- move toward full embedded system practice  

This repo is the foundation for bigger builds:  
sensors, motors, robotics projects — everything starts with a button and an LED.

---

## 📜 License

This project is released under the **MIT License**.  
See the `LICENSE` file for details.