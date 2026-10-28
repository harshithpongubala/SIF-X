# SIF-X // Industrial Safety Intelligence Command Center

> **From isolated reports to connected SIF intelligence. From reaction to prevention.**  
> *AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in Industrial Unsafe-Act / Unsafe-Condition and Near-Miss Reports.*

---

## 🎯 Executive Overview

**SIF-X (CIPHER-X)** is an industrial-grade Safety Intelligence Command Center built to break through the traditional safety reporting "Iceberg Trap" — where low-severity consequence reports mask catastrophic Serious Injury and Fatality (SIF) precursor events.

Engineered with a spatial HUD glassmorphic interface, SIF-X combines real-time CCTV computer vision feeds, safety telemetry, and explainable NLP decomposition to empower safety controllers, engineers, and plant marshals to identify and arrest hazards before an incident escalates.

---

## ✨ Core Features & Modules

### 1. 🎛️ Command Center & Unified Dashboard
- **Spatial HUD Interface**: High-contrast dark aesthetic (`#0d1823` graphite backdrop with neon cyan and amber status indicators) built using modern glassmorphism, responsive CSS grid, and GSAP micro-animations.
- **Top Command Bar**: Live system time, simulated shift telemetry, active hazard counter, and one-click quick isolation controls.
- **Real-Time Event Feed**: Automated live event stream with severity-coded alerts (Critical, Warning, Safe) and instantaneous action triggers.

### 2. 👷 Worker Review & Field Reports System
- **Executive Summary Panel**: Positioned directly on the main dashboard above the Risk Forecast graph for rapid inspection of pending worker alerts.
- **Dedicated Worker Review Module**: Full-featured inspection desk with multi-criteria filtering (Status, Priority, Site/Zone, Reporter Role), search indexing, and report details drawer.
- **Bi-directional Report Ingestion**: Integrated report submission form supporting field hazard logging with immediate state synchronization.

### 3. 🧠 SIF NLP Engine & Precursor Decomposition
- **IOGP Life-Saving Rules Taxonomy**: Automatic semantic mapping of incident narratives against international standards (Working at Height, Energy Isolation, Line of Fire, Confined Space, etc.).
- **Precursor Fingerprint Formulation**: Deconstructs every incident into a 6-dimensional safety vector:
  $$\text{Precursor Fingerprint} = \text{Activity} + \text{Hazard} + \text{Energy} + \text{Exposure} + \text{Barrier} + \text{Consequence}$$
- **SIF Potential Scoring**: Dynamic probability calculations backed by highlighted textual evidence spans and failed barrier detection.

### 4. 📈 SIF Risk Forecasting (40-Minute Horizon)
- **Predictive Horizon Graph**: Vector SVG curve mapping real-time risk scores against a 40-minute predictive lookahead horizon.
- **Dynamic Risk Markers**: Live `Now` baseline and `Peak` hazard badges that adapt dynamically to plant events and emergency actions.

### 5. 📹 5-Node Camera & Sensor Mesh
- **Complete Feed Coverage**:
  - `CAM-03`: Worker Fall Monitoring / Walkway P-07 Traction Zone
  - `CAM-04`: Bay B Overhead Crane & Active Conveyor Perimeter
  - `CAM-07`: Pump Station B - High Pressure Hydrocarbon Chamber (Primary SIF Focal Zone)
  - `CAM-11`: Liquid Chemical Spill Detection & Pump P-104 Seal
  - `CAM-16`: Restricted Access Gate & Autonomous AGV Traffic
- **Canvas Simulation Engine**: Real-time 2D HTML5 canvas simulation with animated worker kinematics, automated guided vehicles (AGV), chamber door states, and interactive emergency stops (E-Stop).
- **HUD & Detection Overlays**: Real-time AI tracking bounding boxes, scan-line sweep animations, optical zoom toggles, and live telemetry.

### 6. 🚨 Safety Interlocks, Hotspots & Emergency Isolation
- **E-Stop & Quick Interventions**: Single-click line stoppage, barrier reinforcement, ventilation override, and marshal dispatch logging.
- **High-Risk Hotspots**: Aggregated clustering of safety signals across plant sectors.
- **Safety Interlocks Matrix**: Real-time status monitoring of automated physical and digital interlocks.

---

## 🏗️ Architecture & Technology Stack

SIF-X is built using a clean, portable single-page architecture:

- **Frontend Core**: React 18, React DOM (UMD)
- **Styling**: Tailwind CSS, Custom Glassmorphic Design System (`src/style.css`)
- **Animations & Effects**: GSAP 3 (GreenSock Animation Platform)
- **Canvas & Visuals**: HTML5 2D Canvas Engine (`MiniCCTVCanvas`), Vector SVG Data Visualizations
- **Build & Assembly**: Lightweight Python assembler (`build.py`) that merges `src/app.jsx` and `src/style.css` into the standalone, deployable `index.html`
- **Zero-Dependency Runtime**: Completely deployable as a static web application to Vercel, Netlify, or GitHub Pages.

---

## 📁 Repository Structure

```
├── index.html                  # Standalone deployable SIF-X application entry point
├── build.py                    # Concatenation & build script (src/ -> index.html)
├── serve.py                    # Lightweight Python HTTP server for local hosting
├── launch_dashboard.bat        # Windows batch script to serve and launch dashboard
├── launch_dashboard.vbs        # Background launcher script
├── start_server.vbs            # Background server runner
├── stop_server.bat             # Process terminator for local server
├── memory.md                   # Comprehensive architectural specifications
├── assets/                     # Industrial camera feeds, backgrounds, and media
│   ├── cam-03-worker-walkway.jpg
│   ├── cam-04-bay-b.png
│   ├── cam-07-pump-station-b.jpg
│   ├── cam-07-pump-station-b-empty.jpg
│   ├── cam-07-pump-station-b-safe.jpg
│   ├── cam-11-pump-seal.jpg
│   ├── cam-16-restricted-gate.jpg
│   ├── factory_bg.jpg
│   └── ... (CCTV sample videos)
├── components/                 # Component UI templates
│   └── ui/
│       ├── demo.tsx
│       ├── immersive-full-screen-nav.tsx
│       ├── immersive-nav-demo.tsx
│       └── magnetic-cursor.tsx
└── src/                        # Modular source code
    ├── app.jsx                 # Complete React application & component tree
    └── style.css               # Design tokens, keyframe animations, glassmorphism
```

---

## 🚀 Getting Started

### Option 1: Direct File Open
Double-click `index.html` to open directly in any modern web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Local Python Server (Recommended)
Run the included lightweight HTTP server:

```bash
python serve.py
```

Then open `http://localhost:8080` in your browser.

### Option 3: Windows One-Click Launcher
Double-click `launch_dashboard.bat` to automatically spin up the server and open the browser.

---

## 🔐 Demo Credentials

When opening the dashboard authentication gateway:
- **Username**: `admin`
- **Password**: `admin`

---

## 📄 License & Attribution

Designed and developed for **Smart India Hackathon 2026** by Team **CIPHER-X**.  
*Target Enterprise: Oil India Limited (OIL).*
