# 🚀 ARES - AI Rocket & Habitat Design Assistant

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

**ARES** is an interactive AI-powered web app for designing and visualizing rockets and space habitats. It provides AI-based recommendations for optimizing habitat comfort and includes an interactive 3D rocket visualization module.

---

## 🌟 Features

### 1️⃣ AI Assistant
- Ask questions about rockets, space habitats, and space science.
- Covers topics like:
  - Rocket components: engine, fuel, thrust, payload
  - Space habitats: crew, NHV, social & exercise volumes
  - Space physics: microgravity, life support, radiation
- Provides knowledge-based, easy-to-understand answers.

### 2️⃣ Habitat Comfort Optimizer
- AI-powered module using **Random Forest Regression**.
- Generates optimal habitat layouts based on mission parameters:
  - Crew size
  - Cylinder radius
  - NHV utilization (%)
- Recommends sleep, social, and exercise volumes.
- Predicts **comfort score** (0-10) for proposed habitat designs.

### 3️⃣ Rocket Visualization
- Interactive 3D rocket model using **Plotly**.
- Customize rocket parameters:
  - Rocket height & body radius
  - Nose cone height
  - Number & size of fins
  - Flame height & radius
- Explore your rocket model from any angle in real-time.

---

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ares.git
cd ares
pip install streamlit numpy pandas scikit-learn plotly
streamlit run app.py
