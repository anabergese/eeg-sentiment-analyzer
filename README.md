## 🧠 Emotional EEG Visualizer

Visual interface for analyzing synthetic EEG (electroencephalography) data to detect user mental states such as **relaxation** or **alertness**, using **brainwave frequency analysis**. This project combines **FastAPI** (Python) for backend EEG analysis and **React + Vite** for a modern, responsive frontend.

<br/>

### 📸 Preview

[UI Preview](./frontend/public/ui-preview.png)

---

## 📊 What It Does

* 🧪 Collects synthetic EEG signals (via BrainFlow SDK)
* 🔎 Computes **Power Spectral Density (PSD)** and **Spectrograms** per EEG channel
* 🧠 Detects the user's **general brainwave state** (Theta = relaxation / Beta = alertness)
* 🎨 Visualizes brain activity in 4 sections:

  * Static brain diagram with labeled EEG channels
  * PSD charts for each channel
  * Spectrograms with frequency over time
  * Final color-emotion state

---

## 🧰 Tech Stack

| Layer             | Technology                                    |
| ----------------- | --------------------------------------------- |
| **Backend**       | Python, FastAPI, BrainFlow, Matplotlib, SciPy |
| **Frontend**      | React, Vite, CSS Modules                      |
| **Visualization** | EEG charts via Matplotlib exported as PNG     |

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/anabergese/eeg-sentiment-analyzer.git
cd eeg-sentiment-analyzer
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

uvicorn api.main:app --reload
```

✅ The API will be available at: `http://localhost:8000/analyze`
🖼️ EEG charts are served from: `http://localhost:8000/static`

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

✅ The app runs on: `http://localhost:5173`
You must have a proxy set in `vite.config.js` for `/analyze` and `/static`.

---

## 🧠 How It Works (Simplified)

```text
[ EEG Data ] ---> [ Compute PSD & Spectrograms ] ---> [ Detect brainwave state ]
       ↓                         ↓                               ↓
[ plot_all_psds() ]      [ plot_all_spectrograms() ]     [ detect_user_state() ]
```

Theta: 4–8 Hz → Relaxation
Beta: 13–30 Hz → Alert/Focus

We compute averages per band and use thresholds to assign a mental state and associated color.

---

## 📁 Project Structure

```
backend/
│
├── application/        # Business logic (analysis orchestration)
├── domain/             # Core EEG logic and state detection
├── infrastructure/     # Signal processing & plotting
├── static/             # Output images (psd.png, spectrogram.png)
├── main.py             # FastAPI entrypoint
├── requirements.txt
└── ...
frontend/
├── components/
├── pages/
├── App.jsx
└── vite.config.js
```

---

## 📌 Notes

* This is an **early-stage prototype** using **synthetic data** only.
* Goal: Make mental states **visually accessible** to users.
* The detection logic is **basic** and will improve with real EEG input + ML techniques in the future.
* Need to expand the emotional states that can be detected to capture a broader range of human feelings/states related to brain waves.

---

## 🧠 Author

**Ana Belen Bergese**

---
