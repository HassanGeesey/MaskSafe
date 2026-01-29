# IndabaX Somalia 2025: Project Presentation - MaskSafe

## Project Overview: MaskSafe
**Title:** MaskSafe  
**team Members:** [Hassan Geesey, abdullahi ibrahim, moahmed ahmed,camir abbas,abdisalan jaka ]  
**Objective:** To enhance public health safety through automated, real-time compliance monitoring.

---

## 1. Problem Statement
Despite the global recovery from the COVID-19 pandemic, respiratory health remains a critical priority in healthcare settings, airports, and crowded public spaces. 
*   **Manual Enforcement Challenges:** Relying on human personnel to monitor mask compliance is inefficient, expensive, and creates unnecessary contact risk.
*   **Human Error:** Constant monitoring leads to fatigue, resulting in missed violations or improper mask-wearing (e.g., mask below the nose).
*   **Data Scarcity:** Organizations lack real-time data on compliance rates to make informed safety decisions.

---

## 2. Targeted Sustainable Development Goals (SDGs)
Our project aligns with two key global goals:
*   **SDG 3: Good Health and Well-being:** By preventing the spread of communicable respiratory diseases through automated monitoring.
*   **SDG 9: Industry, Innovation, and Infrastructure:** Utilizing cutting-edge AI (YOLOv3) to create smarter, safer public infrastructure and health systems.

---

## 3. Proposed Solution
**The Approach:**
We developed **MaskSafe**, an end-to-end computer vision solution capable of detecting three distinct states:
1.  **Mask:** Correct mask-wearing.
2.  **Improperly Masked:** Mask worn but not covering nose/mouth (crucial for health safety).
3.  **No Mask:** Absence of a face mask.

**AI/ML Methodology:**
*   **Architecture:** Employed **YOLOv3 (You Only Look Once)** with a Darknet-53 backbone for a balance between speed and precision.
*   **Performance:** Achieved a **94.04% mAP (mean Average Precision)**, with a specific **96.96% AP** for correct mask detection.
*   **Real-time Optimization:** The system processes live video streams at high frame rates, allowing for immediate feedback in high-traffic environments.

---

## 4. Technology Stack Used
The project is built on a robust and scalable open-source stack:
*   **Backend:** Python 3.7+, Flask (for web server and routing)
*   **Computer Vision:** OpenCV (for image/video capture and processing)
*   **Deep Learning Framework:** Darknet / YOLOv3 (for mask detection inference)
*   **Frontend:** Modern HTML5, CSS3 (Glassmorphism design), and Vanilla JavaScript
*   **Data Handling:** NumPy (for efficient matrix operations on image frames)

---

## 5. Expected Impact
**Somalia Context & Beyond:**
*   **Institutional Safety:** In Somalia, where healthcare resources are focused on building resilience, MaskSafe provides a low-cost, high-impact tool for hospitals and government offices.
*   **Efficiency:** Automating compliance allows security and health staff to focus on more complex tasks rather than constant observation.
*   **Public Awareness:** Visual feedback (live feeds displaying "Mask" or "No Mask") serves as a gentle reminder to the public, fostering a culture of safety.
*   **Data-Driven Decisions:** The **Metrics Dashboard** provides administrators with clear statistics (F1-Score, AP) to validate the system's reliability before full-scale deployment.

---

## Key Success Factors
*   **Originality:** Custom-trained YOLOv3 model tailored for granular detection (including 'improper' usage).
*   **Citations:** Face Mask Detection YOLO dataset; YOLOv3 by Joseph Redmon & Ali Farhadi.
*   **Focus:** Designed for real-world deployment on standard CPUs, making it practical for local hardware environments.

---

## Live Demo Preparation
*   [ ] Show **Live Camera Feed** (Direct detection)
*   [ ] Demonstrate **Image Upload** analysis
*   [ ] Show **Metrics Dashboard** and clarify the meaning of mAP in this context.
