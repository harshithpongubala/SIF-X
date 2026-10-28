# Project Memory: CIPHER-X Industrial Safety Intelligence Dashboard

**Project**: CIPHER-X — AI/NLP Engine & Safety Intelligence Dashboard  
**Hackathon**: Smart India Hackathon 2026 (SIH 2026)  
**Problem Statement ID**: 26165  
**Problem Statement Title**: AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in OIL's Unsafe-Act/Unsafe-Condition and Near-Miss Reports  
**Theme**: Smart Automation  
**Category**: Software  
**Team ID**: SIH-0099  
**Team Name**: CIPHER X (CIPHER-X)  
**Target Enterprise**: Oil India Limited (OIL)  
**Workspace Root**: `c:\Users\rahul\safety-intelligence-dashboard`  
**Primary Tech Stack**: React 18 / Next.js, Tailwind CSS, GSAP 3, HTML5 Canvas, Web Audio API, Python 3 HTTP Server / FastAPI  
**Design Reference**: RonDesignLab Spatial HUD Aesthetic & CIPHER-X Safety Knowledge Architecture  
**Core Motto**: *"BUILT FOR SAFETY. DESIGNED FOR TRUST. MADE FOR OIL. | From isolated reports to connected SIF intelligence. From reaction to prevention."*

---

## 1. Executive Summary & Purpose

**CIPHER-X** is an AI/NLP-powered Industrial Safety Intelligence Platform engineered to detect Serious Injury & Fatality (SIF) precursors in Oil India Limited's (OIL) Unsafe-Act/Unsafe-Condition (UA/UC) and Near-Miss reports.

The platform addresses the critical industry limitation where low-severity incidents mask high-potential catastrophic outcomes. By combining a RonDesignLab spatial glassmorphic HUD layout with hybrid AI, safety knowledge graphs, and real-time CCTV computer vision feeds, CIPHER-X transitions industrial safety management from reactive post-incident triage to proactive, evidence-grounded precursor intervention.

---

## 2. Problem Statement & Solution Paradigm

### The Problem
- **Massive Report Volumes**: High frequency of unstructured UA/UC and Near-Miss documentation scattered across operational sites.
- **Manual, Periodic Triage**: Time-lagged human review causes critical safety precursors to be overlooked until incidents escalate.
- **The Iceberg Trap**: Low-severity consequences frequently conceal high SIF potential (e.g., an uncontrolled high-energy release that narrowly missed personnel).
- **Scattered Data**: Precursor signals remain disconnected across diverse sites, drilling rigs, and shifts over time.

### The CIPHER-X Solution Pipeline
```
OIL HSSE Report ➔ SIF Potential Scoring ➔ Precursor Extraction ➔ Barrier Analysis ➔ IOGP Mapping ➔ Pattern Discovery ➔ SIF Hotspot Clustering ➔ Combined Deterministic Approach ➔ Workers Review ➔ Camera Module
```

### The Precursor Fingerprint Formulation
CIPHER-X breaks down every incident report into an explainable 6-dimensional safety vector:
$$\text{Precursor Fingerprint} = \text{Activity} + \text{Hazard} + \text{Energy} + \text{Exposure} + \text{Barrier} + \text{Consequence}$$

---

## 3. Technical Architecture & Implementation Flow

### 7-Stage Hybrid AI Implementation Flow
1. **OIL HSSE Reports**: Ingestion of raw text, site identifier, timestamp, activity classification, UA/UC designation, and Near-Miss reports.
2. **Data Processing**: Preprocessing, text cleaning, entity normalization, and tokenization.
3. **Safety NLP Engine**: Transformer-based models paired with fine-tuned Safety Named Entity Recognition (Safety NER).
4. **Precursor Extraction**: Automated tagging of Hazard types, Energy forms, Exposure duration, and Barrier status.
5. **SIF Engine**: Calculation of SIF Probability backed by highlighted textual evidence spans.
6. **Intelligence Layer**: Alignment to IOGP Life-Saving Rules, semantic vector similarity, temporal trend analysis, and precursor knowledge graphs.
7. **HSE Dashboard**: Interactive visualization of SIF Scores, Evidence Spans, Failed Barriers, Trend Clusters, and Geospatial Hotspots.

### Technology Stack & Architecture Allocation
- **Frontend (20%)**: React 18 / Next.js, Tailwind CSS, GSAP 3 (Fluid micro-interactions & spatial transitions).
- **Backend (15%)**: Python + FastAPI (Async RESTful endpoints & model serving).
- **Safety NLP Engine (15%)**: Transformers + Domain-Specific Safety NER.
- **Machine Learning (10%)**: Document Embeddings + XGBoost Classifier.
- **Semantic Similarity (10%)**: Vector Search + Unsupervised Pattern Clustering.
- **Database Layer (10%)**: PostgreSQL + `pgvector` for high-dimensional semantic search.
- **Analytics & Visualizations (20%)**: Python / Plotly & SVG predictive forecasting curves.
- **Deployment**: Docker containerization / On-Premise air-gapped deployment for OIL data sovereignty.

---

## 4. Feasibility, Reliability & Active Learning Loop

### Practical Feasibility
- **Zero New Hardware Requirement**: Operates directly on OIL's existing text reports and historical metadata.
- **Data Sovereignty & On-Premise Execution**: Sensitive operational records remain securely within OIL's infrastructure.
- **Human-in-the-Loop (HITL)**: HSE safety officers validate uncertain or borderline classifications.

### Active Learning Loop
```
Historical Reports ➔ Weak / Heuristic Labels ➔ Initial Baseline Model ➔ HSE Expert Validation ➔ Retraining & Fine-Tuning ➔ Continuous Model Evolution
```

### Safety, Trust & Explainability
- **Confidence Tiers**: Categorized into `HIGH`, `MEDIUM`, and `REVIEW REQUIRED`.
- **Evidence-Grounded Predictions**: Every SIF score links directly to highlighted verbatim text spans within the report.
- **Recall-Focused Thresholds**: Tuned to minimize False Negatives (never missing a potential fatality precursor).
- **Controlled Safety Ontology**: Standardized taxonomy prevents arbitrary NLP hallucination.

### Risk & Mitigation Strategy Matrix
| Risk Vector | Impact | CIPHER-X Mitigation Strategy |
| :--- | :--- | :--- |
| **False Negatives** | Unflagged SIF risk | Recall-focused classification threshold |
| **False Positives** | Reviewer fatigue | HSE expert validation feedback loop & threshold tuning |
| **Limited Labelled Data** | Inaccurate supervised learning | Weak labelling rules + Active Learning framework |
| **Domain Jargon / Acronyms** | NLP misinterpretation | Custom OIL Safety Ontology & specialized NER |
| **AI Hallucination** | Erroneous safety advice | Strict evidence-grounded extractive output |

### Scalability Roadmap
$$\text{Pilot Testing} \longrightarrow \text{Single Installation} \longrightarrow \text{Multi-Site Rollout} \longrightarrow \text{Enterprise-Wide SIF Intelligence}$$

---

## 5. Strategic Impact & Organizational Benefits

### The Operational Paradigm Shift
- **Legacy Reactive Model**: `Report ➔ Periodic Triage ➔ Individual Review` *(Focus on "How many incidents happened?")*
- **CIPHER-X Proactive Model**: `Report ➔ AI Triage ➔ Precursor Detection ➔ Pattern Discovery ➔ Targeted Intervention` *(Focus on "Which SIF precursors are emerging — and where?")*

### Core HSE & Organizational Benefits
1. **Prioritise**: Automatically elevates high SIF-potential events to the top of the triage queue.
2. **Detect**: Pinpoints failing or absent critical physical/procedural barriers before catastrophic failure.
3. **Connect**: Links recurring precursor patterns across geographically separated drilling rigs and plant units.
4. **Monitor**: Tracks real-time velocity and volume changes in precursor clusters (e.g., Energy Isolation tracking +42%).
5. **Target**: Empowers leadership to deploy targeted barrier-verification interventions rather than generic audits.

---

## 6. Scientific Research Foundation & Standards

CIPHER-X is built upon peer-reviewed safety science and established industry frameworks:
- **Edison Electric Institute (EEI)**:
  - *Power to Prevent SIF*: Industry-standard framework for precursor identification.
  - *SIF Precursor Implementation Guide*: Methodologies for precursor scoring and classification.
- **Academic Research**:
  - *Martin & Black (2015)*: "Preventing Serious Injuries and Fatalities: Precursors and Paradigms".
  - *Parikh, Penfield & Juaire (2024)*, *Nature Scientific Reports*: "Automatic identification of potential SIF incidents: Transformers + XGBoost + Weak Labelling".
- **Industry Standards**:
  - **IOGP Report 459**: International Association of Oil & Gas Producers Life-Saving Rules & Critical Safety Controls.
  - **Oil India Limited (OIL)**: HSSE incident reporting protocols, UA/UC taxonomies, and CAPA workflows.
- **SIF-X Research Synthesis Formula**:
  $$\text{SIF Science} + \text{Safety NLP} + \text{Barrier Intelligence} + \text{IOGP Mapping} + \text{Precursor Graph} = \text{Connected SIF Intelligence}$$

---

## 7. Design System & UI Specifications

### Color Palette
- **Canvas / Graphite Background**: `#0d1823` and `#081018`
- **Active Telemetry & Neon Cyan**: `#6bc8ff` (`rgba(107, 200, 255, 0.45)` glow)
- **Safe Operating State**: `#10b981` (Safe Emerald)
- **Elevated Warning State**: `#f59e0b` (Industrial Amber)
- **Critical Alert State**: `#ef4444` (Danger Red with pulse alert)
- **Iconic Action Panel Cream**: `#edece4` (High-contrast card with dark text `#101922`)
- **Glass Borders**: `rgba(255, 255, 255, 0.1)` to `rgba(255, 255, 255, 0.22)`

### Typography
- **Dense Tabular Telemetry**: `JetBrains Mono` (`font-feature-settings: "tnum" 1, "zero" 1`)
- **Primary Interface**: `Plus Jakarta Sans`
- **Compact Badges**: Rounded capsules with uppercase tracking (`tracking-wider`, `tracking-widest`)

### Depth of Field & Visual FX
- Photorealistic dark-mode industrial factory floor image (`assets/factory_bg.jpg`) positioned in a background layer (`.dof-stage`) with `filter: blur(14px) brightness(0.48) saturate(1.2)`.
- Multi-layer radial blur (`.dof-blur-layer`) providing warm amber tungsten and cyan lighting bokeh.
- Vignette overlay (`.dof-vignette`) concentrating focus on the central HUD card.

---

## 8. Directory Structure

```
safety-intelligence-dashboard/
├── assets/
│   └── factory_bg.jpg                     # Photorealistic factory DOF background image
├── components/
│   └── ui/                                # Standard shadcn UI component directory
│       ├── magnetic-cursor.tsx            # Physics-based GSAP magnetic cursor
│       ├── demo.tsx                       # Magnetic cursor demonstration component
│       ├── immersive-full-screen-nav.tsx  # GSAP clip-path reveal fullscreen navigation
│       └── immersive-nav-demo.tsx         # Fullscreen navigation demo
├── src/
│   ├── app.jsx                            # Main CIPHER-X dashboard application (React 18)
│   ├── style.css                          # Design tokens, DOF styles, and Tailwind extensions
│   └── components/
│       └── ui/                            # Mirrored components for @/components/ui resolution
├── build.py                               # Compiler inlining CSS & JSX into index.html
├── serve.py                               # Python HTTP server (Port 8080)
├── index.html                             # Compiled standalone bundle
└── memory.md                              # Project documentation & context memory
```

---

## 9. Key Application Features

### A. Top Command Bar
- **Plant Telemetry Header**: `Plant 04 · Autonomous Sentinel // Sector 7G`.
- **SIF Severity State Toggle**: Cycles through `NORMAL`, `ELEVATED`, and `CRITICAL` states with real-time Web Audio API frequency synthesis.
- **Real-Time FPS & Latency Ticker**: Live frame counter (60+ FPS) and low latency monitoring (16ms).
- **Header Navigation Trigger**: Accessible menu button (`☰`) that reveals the fullscreen navigation overlay.

### B. Centerpiece Floating Spatial HUD
- **Left Capsule Dock**: Quick-switch buttons for System Overview, Live Video Feeds, Precursor Hazard Matrix, and Emergency E-Stop.
- **Branding & Title**: `qb / SIF-INTEL` branding with headline **CIPHER-X // SIF PRECURSOR ENGINE**.
- **Navigation Pills**: `Dashboard`, `Sensors`, `Incident Feed`, `Risk Forecast`, `Interlocks`, `CCTV Feeds`, `Audit Logs`.
- **Safety Sentinel Gauge**: 11% Residual Risk Index radial gauge with dynamic SVG stroke animation.
- **Primary KPIs**:
  - `990,815 h` Safe Operating Hours
  - `170,520` SIF Precursors Mitigated
  - `64,520 pts` Active Monitored Sensors
- **Category Filter Pills**: `All`, `Forklift/AGV`, `PPE Compliance`, `Crane Zones`, `Thermal/Gas`, `Interlocks`.

### C. Bottom Panels
- **Live Optical Sentinel CCTV (Cols 1-8)**:
  - Multi-feed switcher (`CAM-01 Assembly Line`, `CAM-02 Robotic Welding Cell`, `CAM-03 Chemical Vault`).
  - Interactive HTML5 Canvas rendering moving workers, automated AGVs, and robotic arms with welding sparks.
  - Real-time overlay bounding boxes (`99% PPE COMPLIANT`, `CRIT 1.2m PROXIMITY ALERT`, `THERMAL ENVELOPE: 380°C`).
  - Incident calendar matrix with highlighted current day.
  - Protocol tier selector (`Level 1 Standard`, `Level 2 Enhanced`, `Enterprise Sentinel`).
- **Real-Time Event Feed (Cols 9-12 Top)**:
  - Dynamic optical inference event log with severity pills.
  - Interactive event detail modal with incident acknowledgment logging.
  - AI Bounding box dual toggle switch (`✕` / `✓`).
- **Quick Intervention Panel (Cols 9-12 Bottom Cream Card `#edece4`)**:
  - Emergency E-Stop interlock toggle button.
  - Evacuate Zone trigger button.
  - Audible siren armed/muted toggle switch (`✕` / `✓`).
- **Risk Forecasting Line Graph**:
  - 24-hour predictive incident curve with critical hazard thresholds.
  - Interactive point hover displaying projected risk percentage and active mitigation protocols.

### D. Integrated UI Components
- **Magnetic Cursor**: Physics-based lerp cursor with `exclusion` blending and `data-magnetic` hover snapping.
- **Immersive Fullscreen Nav**: Triggered from the top menu, wipes open via `clip-path` with staggered link reveals and factory visual tiles.

---

## 10. Execution & Operational Commands

### Compiling Application
```powershell
python build.py
```
*Reads `src/style.css` and `src/app.jsx` and outputs the standalone `index.html`.*

### Running Server
```powershell
python serve.py
```
*Serves the project on `http://127.0.0.1:8080`.*

### Opening in Default Browser
```powershell
Start-Process "http://127.0.0.1:8080"
```

---

## 11. Environment & Architectural Notes

1. **Standalone Zero-Install Architecture**:
   - Because `node` and `npm` were not pre-installed in the host global PATH, the live application is built using React 18 UMD, ReactDOM, Babel Standalone, Tailwind CSS Play CDN, and GSAP 3 CDN.
   - This delivers a zero-dependency, immediate browser runtime.

2. **shadcn Directory Conventions**:
   - Component primitives strictly live in `/components/ui/` (`magnetic-cursor.tsx`, `immersive-full-screen-nav.tsx`, etc.).
   - This conforms to the shadcn CLI scaffolding schema and TypeScript `@/components/ui/*` path alias standards.

3. **External Dependencies for Production Migration (Vite / Next.js)**:
   - `gsap`
   - `vecteur`
   - `lucide-react`
   - `tw-animate-css`
   - `@tailwindcss/vite` / `tailwindcss`

---

## 12. Change Log

- **2026-09-16 / 2026-09-17**:
  - Rebranded title headline to **CIPHER-X // SIF PRECURSOR ENGINE**.
  - Integrated SIH 2026 Problem Statement 26165 parameters (OIL Unsafe-Act/Unsafe-Condition and Near-Miss SIF Detection).
  - Incorporated Precursor Fingerprint formulation: $\text{Activity} + \text{Hazard} + \text{Energy} + \text{Exposure} + \text{Barrier} + \text{Consequence}$.
  - Added 7-stage Hybrid AI Implementation Flow & technology breakdown (Transformers, Safety NER, XGBoost, pgvector, FastAPI).
  - Added Active Learning Loop, Feasibility, and Risk-Mitigation Matrix.
  - Added Scientific Research Foundation (EEI, IOGP Report 459, Martin & Black, Parikh et al. 2024 Nature Scientific Reports).
  - Implemented `components/ui/magnetic-cursor.tsx` and `components/ui/demo.tsx`.
  - Implemented `components/ui/immersive-full-screen-nav.tsx` and `components/ui/immersive-nav-demo.tsx`.
  - Upgraded `src/style.css` with graphite tokens, Tailwind 4 `@theme inline`, and DOF blur layers.
  - Recompiled standalone bundle via `python build.py` and served via `python serve.py` at `http://127.0.0.1:8080`.
  - Connected New Dashboard UI to Existing CIPHER-X Functionality (20-Point Operational Mapping, 21.5s Scripted Timeline, Live Backend Hooks, PathBreaker Activation, Multi-Camera Feeds).

---

## 13. 20-Point Operational Element Mapping Summary

| # | Element | Data Source | Controller / Logic | UI Update | Status |
|---|---------|-------------|--------------------|-----------|--------|
| 1 | SIF Status | Demo phase / `/api/assessment` | `DeterministicRuleEngine.evaluate()` | `NORMAL` -> `ELEVATED` (4.8s) -> `CRITICAL` (18.6s+) | Functional |
| 2 | FPS & Latency | Camera / RAF ticker | `CameraCapture.fps` / RAF loop | 60.2 FPS, 16ms latency | Functional |
| 3 | System Health | FastAPI backend | `GET /api/health` | `AI Live` vs `System Live` | Functional |
| 4 | KPI Statistics | `command-center.ts` | Health event telemetry | 990,815 Safe Hours, 170,520 Mitigated, 64,520 Sensors | Functional |
| 5 | Category Filters | `EventType` models | Predicate filter | All, Forklift/AGV, PPE Compliance, Crane Zones, Thermal/Gas, Interlocks | Functional |
| 6 | CCTV Feed | Vision runtime / canvas | `MiniCCTVCanvas` & `/api/vision/frame.mjpg` | CAM-07 (SIF zone), CAM-01 (Conveyor), CAM-02 (Welding), CAM-03 (Storage) | Functional |
| 7 | AI Detection Status | `health.vision.detectors` | Detector health | `ACTIVE · OPTICAL SENTINEL` | Functional |
| 8 | AI Bounding Boxes | Vision adapters | Bounding box renderer | Real-time dual toggle switch (`✕` / `✓`) | Functional |
| 9 | Incident Event Feed | `timelineEvents` | Phase reveal unrolling | `EVT-7840` through `EVT-7846` + click modal | Functional |
| 10 | Current Shift | Shift metadata | `Asia/Kolkata` clock | `18th / Delta` | Functional |
| 11 | Workers in Zone | Detector count | `person_entered_zone` count | `1` present -> `0` exited -> `5 PPE 100%` | Functional |
| 12 | PPE Status | PPE classifier | Vision inference | `PPE 100% COMPLIANT` | Functional |
| 13 | Zone Risk Score | Barrier health model | `correlations.json` | Progresses from `22/1000` to `750/1000` | Functional |
| 14 | Interlock Status | Invariant engine | `InvariantAssessment.broken` | `ARMED` -> trips to `ENGAGED` | Functional |
| 15 | Quick Intervention | Interventions | `handleEStopToggle` | E-Stop interlock toggle, Evacuate Zone, Siren toggle | Functional |
| 16 | PathBreaker State | `pathbreaker-panel.tsx` | Phase >= 10 trigger | `PB-01: ISOLATE + SECURE CHAMBER` (3/3 paths broken, 94% conf) | Functional |
| 17 | Risk Forecast | Risk forecast model | SVG risk curve algorithm | Dynamic 24-hour predictive curve | Functional |
| 18 | DEMO | `use-scripted-demo.ts` | 21.5s clock runner | Deterministic 11-phase sequence execution | Functional |
| 19 | Pause | `use-scripted-demo.ts` | Clock pause handler | Freezes timer and locks current phase | Functional |
| 20 | Reset | `use-scripted-demo.ts` | Clock reset handler | Rewinds to 0s, clears alerts, restores baseline safe | Functional |

---

## 14. SIH Problem Statement 26165: SIF NLP Engine & Hotspot Intelligence Implementation

### A. Normalized Safety Report Data Contract
Directly aligned with OpenAPI 3.1 Swagger specification and Streamlit reference dashboard:
- `ReportType`: `Near-Miss`, `Unsafe-Act`, `Unsafe-Condition`, `Incident`
- `ReportRequest`: `site`, `activity`, `report_type`, `description`
- `PrecursorFingerprint`: `hazard`, `energy`, `exposure`, `failed_barrier`
- `Evidence`: `detected_keywords`, `summary`
- `AnalysisResult`: `sif_probability` ($0.0 \dots 1.0$), `confidence_level` (`HIGH`/`MEDIUM`/`LOW`), `iogp_category`, `precursor_fingerprint`, `evidence`
- `ReportResponse`: `timestamp`, `site`, `activity`, `report_type`, `analysis`
- `HotspotsResponse`: `sites_ranked`, `activities_ranked`, `iogp_distribution`, `barrier_failures`, `total_reports_analyzed`, `sif_precursor_count`, `sif_rate_percentage`, `precursor_patterns`

### B. IOGP Life-Saving Rules Taxonomy
1. **Working at Height**: scaffold, harness, lanyard, elevated, roof, fall arrest, ladder
2. **Energy Isolation (LOTO)**: lockout, tagout, breaker, valve, de-energize, residual pressure
3. **Line of Fire**: pinch point, rotating shaft, dropped object, pressurized hose, projectile
4. **Confined Space**: tank entry, vessel, pit, manhole, gas testing, oxygen deficiency
5. **Hot Work**: welding, cutting, grinding, torch, flammable, hydrocarbon zone
6. **Lifting Operations**: crane, hoist, rigging, sling, wire rope, suspended load
7. **Bypassing Safety Controls**: interlock bypassed, defeated sensor, bridged relay, override
8. **Toxic Gas & Hazardous Atmosphere**: H2S, sour gas, sulfur, SCBA, toxic vapor
9. **Driving & Heavy Mobile Equipment**: forklift, AGV, speeding, rollover, blind spot

### C. FastAPI Backend Endpoints (`c:\Users\rahul\Cipher\backend`)
- `GET /`: Swagger UI documentation redirect
- `POST /api/v1/reports/process`: Ingests and classifies individual free-text reports
- `GET /api/v1/analytics/hotspots`: Returns aggregated hotspot rankings across sites and activities

### D. Dual-Mode Studio Navigation
- Top navigation bar allows seamless switching:
  - **`Dashboard`**: Full spatial glassmorphic HUD with CAM-07 deterministic 21.5s optical demo, canvas kinematics, 24h risk projection, and PathBreaker interlocks.
  - **`SIF NLP Engine`** / **`Hotspots`**: Dual-column NLP Report Studio matching Streamlit reference UI:
    - Left Column: "Submit Safety Incident Report" with 6 one-click archetype presets, batch CSV/JSON ingestion, SIF classification badges, 4-tuple fingerprint, and interactive collapsible JSON inspector.
    - Right Column: "High-Risk Hotspot Analytics" with summary KPIs, Site Hotspot Density Ranking table, High-Risk Activities with top barrier failures, IOGP distribution, and recurring failure chains.

---

## 15. Multi-Tab Navigation Architecture & Dedicated Page Views

### A. State-Based View Router (`src/app.jsx`)
Replaced binary conditional with dedicated page renderers sharing top-level state:
```jsx
{activeNavTab === 'Dashboard' && <DashboardView />}
{activeNavTab === 'SIF NLP Engine' && <SIFNLPEngineView />}
{activeNavTab === 'Hotspots' && <HotspotsView />}
{activeNavTab === 'Sensors' && <SensorsView />}
{activeNavTab === 'Incident Feed' && <IncidentFeedView />}
{activeNavTab === 'Risk Forecast' && <RiskForecastView />}
{activeNavTab === 'Interlocks' && <InterlocksView />}
```

### B. Shared State & Demo Preservation
- All 7 views share state: `currentPhase`, `riskScore`, `visibleEvents`, `filteredEvents`, `interlockState`, `pathBreakerActive`, `demoPlayback`, etc.
- **Zero Reset**: Switching between tabs never pauses or destroys the 21.5-second CAM-07 demo.
- Every subpage contains a `"← Return to CAM-07 Sentinel"` button that smoothly restores the Command Center view.

---

## 16. Secondary Dashboard Filter System (`dashboardFilter`)

### A. Purpose & Separation from Primary Navigation
The secondary filter bar directly below `CIPHER-X / SIF PRECURSOR ENGINE` operates strictly within the `DashboardView`:
- **Primary Navigation (`activeNavTab`)**: Switches whole application views (`Dashboard`, `SIF NLP Engine`, `Hotspots`, `Sensors`, `Incident Feed`, `Risk Forecast`, `Interlocks`).
- **Secondary Navigation (`dashboardFilter`)**: Filters events, invariants, and risk context *inside* the Dashboard without changing the active page or restarting the 21.5-second CAM-07 demo.

### B. Supported Filters & Deterministic Demo Invariants
1. **`All`**: Displays complete real-time event stream (`visibleEvents`).
2. **`Forklift/AGV`**: Filters to mobile equipment transit events; shows clean empty state `"No active demo events in this category"` with corridor context when not currently triggered.
3. **`PPE Compliance`**: Filters to worker ingress and PPE barrier events (e.g., `EVT-7840: Worker entered Pump Station B`).
4. **`Crane Zones`**: Filters to overhead rigging and lift operations; shows sensible empty state with Rig-04 catwalk exclusion context.
5. **`Thermal/Gas`**: Filters to chamber P-104 pressure containment, gas sensor, and thermal hotspot events (e.g., `EVT-7841`).
6. **`Interlocks`**: Filters to safety invariant violations, PathBreaker triggers, and autonomous physical mitigations.
7. **`+` Button**: Opens non-destructive "More Demo Filters" modal highlighting planned hazard categories (`Arc Flash`, `Confined Space`, `Hot Work`, `Working at Height`).

### C. Visual Styles & Context Banner
- Active filter pill receives `.filter-pill.active` (bright white background with dark text and neon cyan glow).
- Non-active pills retain `.filter-pill` (glassmorphic dark styling).
- When any filter other than `All` is active, an `Active Category Filter Context Banner` renders directly under the filter pills showing category icon, label, active demo event count, tagline, monitored invariant, and a quick `"✕ Reset Filter"` button.
- Empty states display:
  ```
  ℹ️ No active demo events in this category
  Camera CAM-07 is monitoring Pump Station B (Zone Focus)
  [Show All Events]
  ```
- Guaranteed zero resets: Filter state changes do NOT abort or restart the 21.5s CAM-07 demo.

---

## 17. Dynamic Safety Priority & Precursor Density Bar

### A. Purpose & Operational Rationale
Transformed the static secondary filter pill row into an industrial **Safety Priority / Precursor Density Bar** that gives safety marshals and plant operators immediate visual clarity into which hazard categories currently exhibit the highest concentration of safety reports and SIF precursors.

### B. Single Source of Truth & Reusable Aggregation
- **Unified Dataset**: `reports` state lifted to top-level `App` (`INITIAL_SYNTHETIC_REPORTS`, 20 normalized oilfield incident records from `OIL-SYN-001` through `OIL-SYN-020`, plus real-time user-submitted reports from `SIFNLPEngineView`).
- **Dynamic Aggregation (`computeCategoryPriority`)**:
  - Automatically parses free-text activity and incident narratives.
  - Categorizes into 5 hazard domains: `Thermal/Gas`, `Crane Zones`, `Forklift/AGV`, `PPE Compliance`, `Interlocks`.
  - Sorts categories automatically in **descending order** (`b.count - a.count`).
  - Computes dynamic priority tiers based on distribution:
    - `HIGH`: `count >= maxCount * 0.70`
    - `MEDIUM`: `count >= maxCount * 0.40`
    - `LOW`: remaining lower-density categories.
  - Automatically designates the leading category with a `#1 PEAK` micro-tag and glowing border accent (`.peak-priority`).

### C. Bar Layout & Visual Hierarchy
- **Pinned Global Control**: `[ ALL · 20 ]` remains pinned at index 0 as global reset.
- **Sorted Intelligence Badges**:
  - `[ 🔥 THERMAL/GAS #1 PEAK | 6 REPORTS | HIGH ]`
  - `[ 🔒 INTERLOCKS | 6 REPORTS | HIGH ]`
  - `[ 🦺 PPE COMPLIANCE | 4 REPORTS | MEDIUM ]`
  - `[ 🏗️ CRANE ZONES | 3 REPORTS | MEDIUM ]`
  - `[ 🚜 FORKLIFT/AGV | 1 REPORT | LOW ]`
- **Active State**: Selected category badge receives `.priority-badge.active` (high-contrast white glass, dark readable text, neon cyan glow).
- **Responsive Design**: Horizontal smooth scrolling with hidden scrollbar (`overflow-x-auto scrollbar-none max-w-full`).


---

## 18. Persistent Background Access & Windows Auto-Start Architecture

### A. Rationale & Problem Solved
Previously, the web server was run only as an interactive session child process or IDE agent task. Whenever the IDE was closed or Windows rebooted, the dashboard became unreachable until manually re-executed.

### B. Permanent Zero-Click Availability
1. **Windows User Startup Hook**:
   - Location: `C:\Users\rahul\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Start-CIPHER-X.bat` (and `.vbs`)
   - Behavior: Automatically invoked by Windows Shell whenever the user logs in or turns on the PC.
   - Windowless Execution: Uses `pythonw.exe` so zero command prompts or terminal windows pop up.
2. **Desktop 1-Click Launchers**:
   - Windows Desktop Shortcut: `C:\Users\rahul\OneDrive\Desktop\CIPHER-X Dashboard.lnk` (globe icon, runs minimized, checks port 8080, starts server if offline, opens browser)
   - Batch Launcher: `C:\Users\rahul\OneDrive\Desktop\CIPHER-X Dashboard.bat`
   - Project Launcher: `c:\Users\rahul\safety-intelligence-dashboard\launch_dashboard.bat`
   - Clean Shutdown Utility: `c:\Users\rahul\safety-intelligence-dashboard\stop_server.bat`
3. **Dual-Stack Socket Server**:
   - `serve.py` binds to `("0.0.0.0", 8080)` with `allow_reuse_address = True`.
   - Access URL: `http://localhost:8080` or `http://127.0.0.1:8080`.
   - Re-running the launcher is idempotent; if the port is already bound, subsequent launcher calls exit cleanly without conflicting.

---

## 19. SIF-X Demo Login Interface & Branding Alignment

### A. Demo Authentication Layer
1. **Pre-Dashboard Authentication Gate**:
   - New `LoginPage` renders before the dashboard on fresh visit.
   - Credentials:
     - **User ID**: `admin`
     - **Password**: `admin`
   - Rejection feedback: Displays high-contrast alert banner `⚠️ Invalid User ID or Password` on incorrect credentials and halts navigation.
   - 1-Click Demo Auto-fill button provided for convenience during hackathon jury evaluation.
2. **Session Persistence & State**:
   - Uses `sessionStorage.getItem('sifx_authenticated') === 'true'`.
   - Successfully authenticated sessions preserve dashboard state across tab reloads.
3. **Subtle Non-Disturbing Logout**:
   - Integrated a sleek `[LOGOUT]` pill into the top header next to the `Chief Safety Officer` profile.
   - Clearing the session returns the interface to the `LoginPage` immediately.

### B. Project Branding Migration ("CIPHER-X" ➔ "SIF-X")
- User-facing headline updated to **`SIF-X // SIF PRECURSOR ENGINE`**.
- Footer and modal branding updated to **`SIH 2026 // PS-26165 | SIF-X`**.
- Document title updated to **`SIF-X // Industrial Safety Intelligence Command Center`**.
- All internal models, event streams, CAM-07 21.5s deterministic sequences, and API handlers remain intact.

---

## 20. Live Visual Enhancements, Animated Risk Forecast & Worker Review (Stage 4)

### A. Live Camera — Scanning & Detection Zones (CAM-04 Bay B)
- **CCTV Scanning Beam**: Added continuous luminous horizontal scanning line (`animate-cctvScan`) and trailing gradient sweep (`animate-cctvSweep`).
- **4 Independently Animated Detection Zones**:
  - `WORKER · PPE OK · 97%` (Tone: `safe`, subtle natural human posture/breathing sway).
  - `NO HARD HAT · 91%` (Tone: `critical`, wandering technician tracking drift).
  - `RESTRICTED ZONE · 88%` (Tone: `warn`, perimeter boundary jitter).
  - `FORKLIFT · TRACKED · 95%` (Tone: `cyan`, translational vehicle path drift).
- **Edge Tracing Scanning Effect**: Each box features a top luminous ray (`box-edge-tracer`) and 4 industrial corner brackets.
- **Dynamic Confidence & Coordinates**: Smooth CSS transitions (`transition: all 1.2s cubic-bezier(0.25, 0.1, 0.25, 1)`) synchronized with demo playback state.

### B. Real-Time Event Feed Indicator Lights & Arrival Animation
- **Smooth Status Indicator Lights**:
  - Critical: `pulse-indicator-red` (rhythmic smooth breathing glow).
  - Warn: `pulse-indicator-amber` (warm amber glow).
  - Cyan: `pulse-indicator-cyan` (cool cyan glow).
  - Safe: `pulse-indicator-emerald` (smooth emerald glow).
- **New Event Arrival Highlight**: Newest stream entries softly illuminate (`animate-event-arrival`) upon arrival.

### C. SIF Risk Forecast — Illustrative Moving Graph (40 Min Horizon)
- **Expansive Plotting Area**: Height increased to `h-48 sm:h-52` with SVG `viewBox="0 0 620 185"`.
- **Catmull-Rom Cubic Spline**: Implemented smooth spline interpolation for observed risk curve and forecast projection.
- **Calibrated Domain & Proportions**: Baseline at `y=162` (0 risk), chart height `142px`, with Critical 70 threshold line accurately positioned at `y=62.6`.
- **Dynamic Derived Indicators**: `Now` and `Peak` metrics derive directly from plotted series values.
- **Continuous Rolling Window**: Shifts forward every 2s in lockstep with the demo timeline.

### D. Professional Interface Symbols
- Replaced emoji characters across Quick Intervention, SIF Risk Forecast, CAM-04, and Worker Review with clean, crisp SVG interface symbols (`IconZap`, `IconEstop`, `IconAlarm`, `IconPhone`, `IconMegaphone`, `IconLock`, `IconRadio`, `IconTrending`, `IconCamera`, `IconSearch`, `IconShieldAlert`, `IconCheckCircle`, `IconClock`, `IconFileText`, `IconUserCheck`, `IconExternalLink`).

### E. Worker Review Section (`WORKER REVIEW · REPORTS & ALERTS`)
- **Main Dashboard Integration**: Embedded directly below Section 5 on the main dashboard view.
- **Structured Report List**: Features report IDs, timestamps, categories, privacy-preserved worker identifiers, zones, severity badges, and review status.
- **Search & Multi-Filters**: Filter by text, severity (`Critical`, `High`, `Medium`, `Low`), status (`New`, `Under Review`, `Resolved`), category, and sort.
- **Detail Inspection Panel**: Full description, submitter, location, evidence logs, linked CCTV quick-focus button, and audit trail.
- **Safety Team Actions**: Acknowledge & Review, Assign Lead (`J. Ramos`), Escalate to Critical (with alert dispatched to Real-Time Event Feed), Add Internal Notes, and Mark Resolved with two-step confirmation.
- **Backup Created**: `C:\Users\rahul\safety-intelligence-dashboard-backup-stage4`.

---

## 15. Final Dashboard Layout and Navigation Adjustments

### A. Repositioned Worker Review Above the SIF Risk Forecast Graph
- **Direct Placement**: Moved the existing `WORKER REVIEW · REPORTS & ALERTS` panel so that it is positioned directly ABOVE the SIF Risk Forecast line graph in the main dashboard layout.
- **Preserved Single Source of Truth**: All counters (`TOTAL PENDING`, `CRITICAL / HIGH`, `UNDER REVIEW`, `RESOLVED`), recent submissions, severity badges, and `VIEW ALL REPORTS` navigation action remain 100% synchronized with the dedicated Worker Review section.
- **Preserved Risk Forecast Graph**: The SIF Risk Forecast line graph remains directly below the Worker Review panel with Catmull-Rom cubic spline interpolation, rolling forecast horizon, and critical threshold 70 reference line.

### B. All 5 Video Cameras Supported in Sensors Tab
- **Multi-Camera Sentinel Network**: Updated the `Sensors` navigation tab to display and manage all 5 available camera feeds:
  1. `CAM-04`: Bay B Floor — Line 3 Conveyor (Conveyor & Walkway Perimeter)
  2. `CAM-07`: Pump Station B — Inspection Chamber (Primary SIF Invariant Node)
  3. `CAM-03`: Worker Walkway — Grid P-07 (Personnel Traction & Posture)
  4. `CAM-11`: Pump Seal Area — Drainage Trough (Liquid Spill & Puddle Scan)
  5. `CAM-16`: Restricted Gate LZ-03 & AGV Crossing (Line-of-Fire Proximity & AGV)
- **Active Camera Sentinels KPI**: Updated KPI card from 4 Nodes to `5 Nodes (CAM-04, 07, 03, 11, 16)`.
- **Interactive Camera Selection**: Clicking any of the 5 camera cards immediately selects that node for inspection, highlighting it and displaying its dedicated telemetry & detection overlays.
- **Rich Detection & Sensor Details**:
  - PPE Compliance Monitoring (Worker #412 No Hard Hat alert on CAM-04, Verified Compliant on CAM-07/03/16).
  - Restricted-Zone Monitoring (Exclusion LZ-03 on CAM-04/16, Open Chamber SIF Alert on CAM-07, Spill Puddle on CAM-11).
  - Forklift & Vehicle Tracking (Forklift FL-02 proximity on CAM-04, AGV-08 on CAM-16, Pedestrian Sanctuary on CAM-03).
  - Associated Hardware Transducers (Vibration, Noise, Pressure, LEL, H2S, Moisture, Lux).
- **Explicit Data Source Identification**: Clear badges differentiate simulated/demo feeds (`SIMULATED SENSOR`, `SIMULATED CV`, `SIMULATED OPTICAL SENTINEL`) from live hardware readings (`LIVE INVARIANT`, `LIVE TRANSDUCER`, `HARDWARE INTERLOCK`).
- **Quick Live HUD Jump**: Includes `VIEW IN LIVE HUD →` button to navigate directly to the main dashboard focused on the selected camera.
- **Preserved Safety Transducers**: Retained all Safety Barrier Health Transducers and Process & Atmospheric Transducers.

### C. Removed Emoji and Fixed Navigation Order
- **New Canonical Navigation Order**:
  1. `Dashboard` (Live Telemetry)
  2. `Worker Review` (Field hazard investigation pipeline)
  3. `SIF NLP Engine` (OIL free-text report triage)
  4. `Hotspots` (Site precursor density ranking)
  5. `Sensors` (Facility Telemetry Mesh & Optical Sentinels)
  6. `Incident Feed` (Fused Event Timeline & Invariant Stream)
  7. `Risk Forecast` (Predictive Horizon Analytics)
  8. `Interlocks` (Autonomous E-Stop Triggers)
- **Professional Icon Integration**: Removed the emoji and integrated Lucide's professional SVG `IconClipboardCheck` symbol matching project dimensions (`w-3.5 h-3.5 sm:w-4 sm:h-4`), stroke width, adaptive active/inactive color transitions, and preserved the pending-report count badge (`bg-red-500/80`).
- **Fullscreen Navigation Overlay**: Synchronized order across both the header pill navigation and the full-screen modal overlay.
- **Backup Created**: `C:\Users\rahul\safety-intelligence-dashboard-backup-layout-adjustments`.


