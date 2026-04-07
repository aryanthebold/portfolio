# Portfolio Project — Context & Session Summary

## Project Overview
Building a personal portfolio website for **Aryan Pratap Singh**, a 2nd Year B.Tech CSE student. The session progressed through multiple design iterations, evolving a light glassmorphism theme with fully dark, space-themed portfolio with a live TON 618 black hole simulation.

---

## Personal Details

| Field | Detail |
|---|---|
| **Full Name** | Aryan Pratap Singh |
| **GitHub** | github.com/aryanthebold |
| **Institution** | GL Bajaj Group of Institutions, Mathura |
| **University** | AKTU (Dr. A.P.J. Abdul Kalam Technical University) |
| **Degree** | B.Tech — Computer Science & Engineering |
| **Year** | 2nd Year (2024–2028) |
| **Location** |Mathura, Uttar Pradesh, India |

---

## Positions of Responsibility

- **President** — Autotons Robotics Club, GL Bajaj Group of Institutions
- **Head Videographer & Photographer** — GL Bajaj Group of Institutions

---

## Skills

| Skill | Tools / Tags |
|---|---|
| Robotics | Arduino, Raspberry Pi, PID Control, Servo, ESP32 etc. |
| Hardware | Electronics, PCB Design, IoT, Computer Systems |
| Video Editing | Premiere Pro, Capcut , DaVinci Resolve |
| Kali Linux | Aircrack-ng, Metasploit, Wireshark |
| Development | React, Node.js, Python |
| AI / ML | TensorFlow, OpenCV, YOLOv8, Pytorch |

---

## Projects

### 1. PID-Based Line Following Robot
- Autonomous robot using PID (Proportional-Integral-Derivative) control algorithm
- Tuned for smooth navigation on curves and intersections
- Stack: Arduino, C++, IR Sensors, ESP32

### 2. RoboRace Competition Robot
- High-speed competition robot for RoboRace events
- Differential drive, tuned motor controllers, real-time sensor feedback
- Built under Autotons Robotics Club
- Stack: Arduino, C++, Motor Control, Chassis Design

### 3. CarbonChain
- Decentralised marketplace for trading carbon credits
- Based on verified carbon footprint reduction and plastic waste recycling
- Rewards eco-friendly behaviour with tradeable digital credits
- Stack: React, Blockchain, Node.js, Smart Contracts, MongoDB

### 4. The Eye
- Automatic weapon detection and terrorist identification system
- Real-time video feed analysis with instant law enforcement alerts
- Stack: YOLOv8, Python, OpenCV, Alert API, CCTV Integration

### 5. DeepShield (Current / In Progress)
- Real-time deepfake detection and protection system
- Guards users from AI-generated scams on WhatsApp, Telegram, video calls, and phone calls
- Uses facial landmark analysis, temporal inconsistency detection, audio deepfake fingerprinting
- Stack: Python, TensorFlow, OpenCV, WebRTC, FastAPI

### Side Project — Cinematic Event Reels
- Head Videographer role at GL Bajaj Group of Institutions
- Produced highlight reels and event coverage for annual tech fest and cultural events
- Stack: Premiere Pro, DaVinci Resolve, DSLR, Capcut

## Contact / Social Links

| Platform | Handle / URL |
|---|---|
| LinkedIn | https://www.linkedin.com/in/aryan-pratap-singh-12694a3b6/ |
| GitHub | github.com/aryanthebold |
| Discord | iaryan |
| Email | aryanpratapsingh2024@glbajajgroup.org |

---

## Design Decisions & Iterations

### Version 1 — Light Glassmorphism
- Light and clean theme with white glass cards
- Glassmorphism effects, anti-gravity floating chips
- Fonts: Google Sans, DM Sans, Helvetica fallback
- Ambient orbs, levitating avatar, scroll cue
- Rejected by user — wanted dark aesthetics

### Version 2 — Dark with WebGL Black Hole
- Deep space dark theme (#080a10)
- 120 twinkling stars, shooting stars, cursor glow
- WebGL GLSL black hole shader (basic accretion disk + Doppler)
- Font: Space Grotesk + DM Mono
- Feedback: Fonts were bad; needed Coolvetica, more animation, real details

### Version 3 — Dark + Nebula Flow + Real Details
- Added nebula particle canvas (22 drifting glow blobs)
- Added upward flowing anti-gravity particle streams (80 particles)
- Improved WebGL black hole with Doppler beaming, gravitational redshift, plasma jets
- Font: Figtree (headings) + DM Sans (body)
- All real personal details incorporated
- Feedback: Fonts still not right; wants Coolvetica specifically for tiles/headings

### Version 4 — Coolvetica + Full Details (Current Best HTML File)
- Coolvetica via @font-face for all headings, hero name, card titles, nav logo, buttons
- DM Sans for body, descriptions, chips, tags
- SF Mono / Fira Code for eyebrows and code labels
- 6 anti-gravity floating glass chips on screen edges
- 160 stars, 30 nebula blobs, 90 flowing particles, shooting stars
- WebGL GLSL black hole with full physics
- All 5 real projects with accurate descriptions
- Real journey/timeline with GL Bajaj, Autotons, Head Videographer roles
- Downloadable as aryan_portfolio_v4.html

### Version 5 — TON 618 Cinematic Simulation (Latest)
- User requested a video-like TON 618 black hole instead of coded shader
- Clarified: no free-to-embed NASA/ESA video of TON 618 exists legally
- Built a Canvas 2D cinematic simulation that looks and behaves like a NASA visualization
- Physics implemented:
  - Keplerian orbital velocity (inner plasma faster, r^-1.5 law)
  - Relativistic Doppler beaming (approaching side brighter/bluer)
  - 6 temperature-layered accretion disk rings (blackbody colours)
  - Photon sphere bright ring at 1.5x RS
  - Pulsing X-ray corona
  - Polar relativistic jets with plasma blob ejection
  - Gravitational lensing of background stars
  - Cinematic lens flare
- Mouse interactivity: Cursor near BH pulls a glowing tendril; cursor expands/glows
- Scroll interactivity: BH shifts upward with parallax; scene dims as user scrolls into content
- Custom cursor that reacts to gravitational proximity

---

## Technical Stack (Portfolio Site)

- Pure HTML/CSS/JS — single file, no framework
- WebGL / Canvas 2D — black hole simulation
- GLSL — fragment shader for physics-based rendering
- Google Fonts — Figtree, DM Sans
- Coolvetica — via @font-face CDN
- IntersectionObserver — scroll reveal animations
- Canvas 2D — nebula, particle streams, TON 618 cinematic
- Hosted on — GitHub Pages (github.com/aryanthebold/portfolio)

---

## Pending / To Do

- Replace placeholder email with real email
- Confirm and update LinkedIn URL
- Confirm Discord handle
- Update GitHub links to correct repos per project
- Integrate TON 618 canvas engine into the actual index.html from the repo
- User to paste index.html from repo so Claude can surgically integrate the TON 618 background
- Add downloadable resume button
- Deploy to GitHub Pages with custom domain (optional)

---

## Files Produced This Session

| File | Description |
|---|---|
| aryan_portfolio_v4.html | Full portfolio — latest complete version with Coolvetica, all real details, WebGL BH |
| blackhole.js | Standalone physics-based WebGL black hole module (Schwarzschild metric, Doppler, lensing) |

---

## User Preferences & Notes

- Passionate about space — TON 618 is specifically requested; astrophysics references throughout
- Dislikes generic AI font choices (Inter, Space Grotesk)
- Wants Coolvetica for display text, DM Sans / Helvetica for body
- Wants large cards, smooth transitions, fully animated effects
- Loves dark aesthetics — deep space black, cyan + violet + purple palette
- Anti-gravity floating elements are a must
- Glassmorphism on cards with backdrop-filter blur
- GitHub repo: github.com/aryanthebold/portfolio (made public during session)
- Claude unable to fetch repo due to GitHub CSP restrictions on iframe/fetch from sandbox
- To integrate TON 618 into the live repo: user should paste index.html into chat
