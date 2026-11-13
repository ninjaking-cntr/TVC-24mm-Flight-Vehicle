# TVC-24mm-Flight-Vehicle
# Active Thrust Vector Controlled (TVC) 24mm Flight Vehicle

![Status](https://img.shields.io/badge/Status-In%20Development-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/MCU-ESP32--S3-orange)

## Project Overview
This repository contains the complete mechanical CAD, custom avionics PCB layouts, flight dynamics simulations, and embedded C++ guidance firmware for a **finless, actively stabilized Thrust Vector Control (TVC) model rocket**. 

Engineered from the ground up as an independent aerospace systems project, the vehicle uses a 2-axis 3D-printed gimbal mount and closed-loop PID attitude control to maintain vertical stability throughout powered ascent without aerodynamic fins.

---

## System Engineering Constraints
To allow independent, solo-legal flight testing under **New Jersey Model Rocketry Regulations (N.J.A.C. 12:194)** and maximize manufacturing efficiency, the vehicle was designed around strict mass, impulse, and fabrication constraints:

* **Propulsion Limit:** 24mm **Estes C11-0 / C11-3** (Max 10.0 N·s total impulse, 22.1 N peak thrust).
* **Mass Ceiling:** Strictly **< 453 g (16 oz)** wet liftoff mass (target wet mass: **~275 g**).
* **Airframe Geometry:** 2.60" (66 mm) outer diameter BT-80 airframe, ~68 cm overall length.
* **Additive Manufacturing Budget:** All structural mounts, gimbal rings, and nose cone sections are topology-optimized for FDM printing within a `24.5 × 20.5 × 20.5 cm` build volume at **\$0.10/g** material cost.

---

## Hardware & Avionics Architecture

| Subsystem | Component | Specification / Role |
| :--- | :--- | :--- |
| **Flight Computer** | Custom KiCad PCB + **ESP32-S3** | 240 MHz dual-core MCU running 200 Hz sensor fusion & PID control loops; onboard flash telemetry logging. |
| **Inertial Sensing** | **MPU6050** (6-DoF IMU) | 3-axis gyroscope & accelerometer feeding a complementary/Madgwick attitude filter. |
| **Altitude Sensing** | **BMP280** Barometer | High-rate static pressure sampling for apogee detection. |
| **TVC Actuation** | 2× **MG90S / ES08MA II** Servos | All-metal-gear micro servos driving pitch and yaw gimbal axes (±7° mechanical deflection limit). |
| **Recovery System** | Non-Pyrotechnic Servo Latch | Mechanical nose-cone release deploying an 18" ripstop nylon parachute. |
| **Power System** | 2S (7.4V) 450mAh LiPo | Regulated 3.3V logic rail with 470µF decoupling capacitors and Schottky diode brownout protection. |

---

## Fault Tolerance & Redundancy
To support rapid iteration during field testing, the system incorporates software, electrical, and modular mechanical redundancy:
* **Triple-Redundant Apogee Detection:** Parachute deployment triggers via an `OR` logic gate combining barometric altitude drop (`BMP280`), inertial tip-over angle (`> 85°` pitch/yaw), and a hard liftoff countdown timer (`T + 4.2s`).
* **Modular Quick-Swap Architecture:** The 2-axis gimbal sled and avionics bay attach via removable M3 fasteners and brass heat-set inserts, allowing damaged structural components to be replaced in under 5 minutes without re-soldering electronics.
* **Continuous Flash Logging:** Flight telemetry is written incrementally to onboard non-volatile flash memory during ascent to preserve post-flight diagnostic data in the event of a hard impact.

---

## Repository Structure
```text
├── /CAD           # Autodesk Fusion parametric models, STEP assemblies, and print-ready STLs
├── /PCB           # KiCad schematics, custom PCB layouts, and Gerber manufacturing files
├── /Firmware      # Embedded C++ flight state machine, IMU sensor fusion, and PID controller
├── /Simulations   # OpenRocket (.ork) aerodynamic models and Python 6-DoF control scripts
└── /Test_Logs     # Static pivot-rig test data, inertia measurements, and flight telemetry plots
