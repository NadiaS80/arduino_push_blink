# Push & Blink

This project may look simple — a button and a single LED — but for me, it’s more than that.  
It’s where code meets real-world physics. It’s where I learned how to make something **alive** with just a few lines of Python and a board full of tiny miracles.  

This is not about complexity. It’s about curiosity. About seeing a light blink and realizing — *I made this happen.*  
This is the beauty of engineering.

---

## What it does

When you press the button, the LED turns on.  
When you release it, the LED turns off.  
That’s it — a minimalistic feedback loop between human and machine.

The schematic for the project is drawn by me in **Google Draw.io**, and you can find it here:  
**diagram.drawio.png** — it clearly shows how the button, LED, and resistors are connected to the Arduino Uno.

---

## ⚙️ How It Works

This project is a tiny “human → hardware → code → hardware” loop. Below is a clear, step-by-step explanation of the exact wiring you see on the diagram and how the signal flows.

### 1) Breadboard rails = shared power lines
- **Red rail** = **+5 V** from Arduino (power).
- **Blue rail** = **GND** (ground, the 0 V reference).  
All holes along each rail are internally connected, so anything you plug into the blue rail is tied to ground; anything into the red rail is tied to +5 V.

### 2) Pins used on the Arduino UNO
- **D2** — digital **input** (reads the button).
- **D8** — digital **output** (drives the LED).
- **5V** — powers the red rail.
- **GND** — connects the blue rail (ground) to Arduino.

### 3) The button circuit (D2 input)
- The **button** is placed **across the center gap** of the breadboard, so its two sides are **not** shorted together.
- **Upper-right leg of the button → red rail (+5 V).**
- **Lower-left leg of the button → Arduino D2.**
- **10 kΩ resistor (pull-down) between D2 and the blue rail (GND).**
  - One end of the 10 kΩ resistor goes to the same row as D2.
  - The other end goes to the blue rail (GND).

**Why this works:**  
- When the button is **released**, D2 is gently pulled to **0** (LOW) through the **10 kΩ** to ground → a clean, stable 0.  
- When the button is **pressed**, it connects D2 directly to **+5 V** from the red rail → D2 sees **1** (HIGH).

This is called a **pull-down** configuration: the resistor “pulls” the input down to 0 when the switch is open, preventing random noise.

### 4) The LED circuit (D8 output)
- **LED anode (long leg) → Arduino D8.**
- **LED cathode (short leg) → 220 Ω resistor → blue rail (GND).**

**Why the 220 Ω resistor:** it limits current through the LED so it doesn’t burn out. The current flows:
- When D8 is **HIGH**: **D8 → LED (anode→cathode) → 220 Ω → GND** → LED lights.
- When D8 is **LOW**: there’s no voltage across the LED → it stays off.

### 5) Power connections
- **Arduino 5V → red rail** (powers the breadboard).
- **Arduino GND → blue rail** (common ground for everything).

Having a **common ground** is essential: the Arduino must share the same 0 V reference with the button and LED circuits, otherwise readings and currents won’t make sense.

### 6) What the software does with this wiring
- The program continuously **reads D2**:  
  - **LOW (0)** = button released (thanks to the 10 kΩ pull-down).  
  - **HIGH (1)** = button pressed (D2 tied to +5 V through the switch).
- Based on that reading, it **writes to D8**:  
  - **1** → LED **on**  
  - **0** → LED **off**

### 7) Typical mistakes this layout avoids
- **Button not across the center gap** → both sides shorted → input always HIGH.  
- **Pull-down not tied to the same row as D2** → D2 “floats” and randomly flips.  
- **LED flipped** (cathode/anode swapped) or **no 220 Ω** → LED won’t light / may burn.

That’s the entire loop: **+5 V & GND rails → button + pull-down create a clean digital input (D2) → code reads it → output (D8) drives the LED through a safe current path.**


---

## 💻 Code

Here’s the main script that runs the project:

```python
import time
from pyfirmata import Arduino, util

board = Arduino('COM3')
it = util.Iterator(board)
it.start()

push_pin = board.get_pin('d:2:i')   
light_pin = board.get_pin('d:8:o')

push_pin.enable_reporting()

while True:
    if push_pin.read() == 1:
        light_pin.write(1)
    else:
        light_pin.write(0)
    time.sleep(0.05)
```

---

## 🧠 In Progress

The commented part of the code below is an experimental version.  
It’s meant to add a **toggle feature** — one press to turn the LED on, another to turn it off.  
However, due to hardware noise (a.k.a. “button bounce”), it currently behaves inconsistently.  
This part of the project is on hold for now, but I’ll come back to it later to stabilize it.

---

## ⚡ Why I’m sharing this

I started this as a small hobby — something like a digital LEGO set, where I could not only assemble but **bring life** to the parts I connect.  
I wanted to share my first working creation, even if it’s small.  
Because that first blink — that moment the LED responds to you — that’s when you realize:

> You’re no longer just coding.  
> You’re *communicating with matter.*

---

## 🔩 Requirements

- **Python 3.10 or lower** (PyFirmata doesn’t support 3.11+)  
- **PyFirmata 1.1.0**  
- **Arduino Uno R3**  
- **USB connection**

Install the dependency:
```bash
pip install pyfirmata==1.1.0
```

---

## 🚀 Author’s Note

This is my first step into physical computing —  
a small project that taught me how to mix hardware, code, and imagination.  
It’s not perfect, but it’s alive.  
And that’s what matters.

# **This is the beauty of engineering.**


---

## 🧾 License (MIT)

This project is released under the **MIT License** — a simple and open-source license.  
