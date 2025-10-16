import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go

# -------------------------------------
# 🌌 PAGE CONFIG
# -------------------------------------
st.set_page_config(page_title="ARES - AI Rocket & Habitat Design", layout="wide")

# -------------------------------------
# 🎨 CUSTOM CSS ANIMATIONS
# -------------------------------------
st.markdown("""
<style>
/* Animated gradient background */
.stApp {
    background: linear-gradient(270deg, #0b0c10, #1f2833, #0b0c10);
    background-size: 400% 400%;
    animation: gradientShift 10s ease infinite;
}
@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glowing Title */
h1, h2, h3 {
    color: #66fcf1 !important;
    text-shadow: 0 0 15px #45a29e, 0 0 25px #66fcf1;
}

/* Glowing Buttons */
div.stButton > button:first-child {
    background: radial-gradient(circle, #1f2833, #0b0c10);
    border: 1px solid #66fcf1;
    color: white;
    padding: 0.6em 1.4em;
    border-radius: 8px;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0 0 10px #45a29e;
}
div.stButton > button:first-child:hover {
    background: #66fcf1;
    color: black;
    box-shadow: 0 0 30px #66fcf1, 0 0 60px #45a29e;
    transform: scale(1.05);
}

/* Sidebar flame glow */
[data-testid="stSidebar"] {
    background: radial-gradient(circle at top, #0b0c10, #1f2833);
    border-right: 2px solid #45a29e;
    box-shadow: inset 0 0 15px #45a29e;
}

/* Smooth section transitions */
.block-container {
    transition: all 0.6s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------
# 🏠 APP TITLE
# -------------------------------------
st.title("🚀 ARES - AI Rocket & Habitat Design Assistant")
st.markdown("### Welcome to ARES: Your intelligent AI for designing and visualizing space habitats and rockets.")

# -------------------------------------
# 🧭 SIDEBAR NAVIGATION
# -------------------------------------
page = st.sidebar.radio(
    "Navigate",
    ["🧠 AI Assistant", "🏠 Habitat Optimizer", "🎨 Rocket Visualization"]
)

# -------------------------------------
# 🧠 PAGE 1: AI ASSISTANT
# -------------------------------------
if page == "🧠 AI Assistant":
    st.header("🧠 ARES Interactive Knowledge Assistant")
    user_input = st.text_input("Type your question here:")

    if st.button("Ask ARES"):
        if user_input.strip() == "":
            st.warning("Please enter a question first.")
        else:
            text = user_input.lower()
            if "rocket" in text:
                st.success("A rocket is a vehicle that uses thrust to overcome gravity and reach space.")
            elif "fuel" in text:
                st.success("Rocket fuel provides chemical energy that’s converted into thrust through combustion.")
            elif "space" in text:
                st.success("Space is a vacuum — no drag, but rockets must carry both fuel and oxidizer.")
            elif "habitat" in text:
                st.success("A space habitat maintains oxygen, temperature, and comfort for astronauts.")
            else:
                st.success("ARES: I don’t have data on that yet, but you can train me on new topics later!")

# -------------------------------------
# 🏠 PAGE 2: HABITAT OPTIMIZER
# -------------------------------------
elif page == "🏠 Habitat Optimizer":
    st.header("🏠 AI Habitat Comfort Optimizer")

    np.random.seed(42)
    n_samples = 500
    data = pd.DataFrame({
        'crew_size': np.random.randint(2, 8, n_samples),
        'radius': np.random.uniform(3, 6, n_samples),
        'nhv_util': np.random.uniform(60, 120, n_samples),
        'sleep_vol': np.random.uniform(10, 16, n_samples),
        'social_vol': np.random.uniform(10, 20, n_samples),
        'exercise_vol': np.random.uniform(4, 8, n_samples),
    })
    data['comfort_score'] = (
        0.3 * (data['nhv_util'] / 100) +
        0.3 * (data['radius'] / 6) +
        0.2 * (data['social_vol'] / 20) +
        0.1 * (data['exercise_vol'] / 8) +
        np.random.normal(0, 0.05, n_samples)
    ) * 10
    data['comfort_score'] = data['comfort_score'].clip(0, 10)

    X = data[['crew_size', 'radius', 'nhv_util', 'sleep_vol', 'social_vol', 'exercise_vol']]
    y = data['comfort_score']
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)

    st.sidebar.header("Mission Parameters")
    crew_size = st.sidebar.slider("Crew Size", 2, 8, 4)
    radius = st.sidebar.slider("Cylinder Radius (m)", 3.0, 6.0, 4.0)
    nhv_util = st.sidebar.slider("NHV Utilization (%)", 60, 120, 95)

    if st.sidebar.button("🧠 Generate Optimal Layout"):
        candidates = pd.DataFrame({
            'crew_size': [crew_size] * 20,
            'radius': [radius] * 20,
            'nhv_util': np.random.uniform(nhv_util - 10, nhv_util + 10, 20),
            'sleep_vol': np.random.uniform(12, 15, 20),
            'social_vol': np.random.uniform(12, 18, 20),
            'exercise_vol': np.random.uniform(5, 7, 20),
        })
        candidates['comfort_score'] = model.predict(candidates)
        best = candidates.iloc[candidates['comfort_score'].idxmax()]

        st.subheader("✅ AI-Optimized Habitat Recommendation")
        st.metric("Predicted Crew Comfort", f"{best['comfort_score']:.2f}/10")
        st.write(f"- Sleep Volume: {best['sleep_vol']:.1f} m³")
        st.write(f"- Social Volume: {best['social_vol']:.1f} m³")
        st.write(f"- Exercise Volume: {best['exercise_vol']:.1f} m³")
        st.write(f"- NHV Utilization: {best['nhv_util']:.1f}%")
        st.success("Design achieves optimal comfort balance for mission parameters!")
    else:
        st.info("Adjust mission parameters and click *AI Recommend* to generate an optimized layout.")

# -------------------------------------
# 🎨 PAGE 3: ROCKET VISUALIZATION
# -------------------------------------
elif page == "🎨 Rocket Visualization":
    st.header("🎨 3D Rocket Visualization")

    height = 10
    body_radius = 1
    nose_height = 2

    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    Z, THETA = np.meshgrid(z, theta)
    X = body_radius * np.cos(THETA)
    Y = body_radius * np.sin(THETA)

    fig = go.Figure()

    # Rocket body
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        surfacecolor=Z,
        colorscale=[[0, "rgb(180,180,180)"], [1, "rgb(90,90,90)"]],
        showscale=False,
    ))

    # Nose cone
    nose_z = np.linspace(height, height + nose_height, 20)
    nose_r = np.linspace(body_radius, 0, 20)
    NoseZ, NoseTheta = np.meshgrid(nose_z, theta)
    NoseX = nose_r * np.cos(NoseTheta)
    NoseY = nose_r * np.sin(NoseTheta)
    fig.add_trace(go.Surface(
        x=NoseX, y=NoseY, z=NoseZ,
        surfacecolor=NoseZ,
        colorscale=[[0, "rgb(220,220,220)"], [1, "rgb(120,120,120)"]],
        showscale=False,
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Height (m)',
            aspectmode='data',
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        height=700,
        title="🔥 Interactive Metallic Rocket Model (Drag to Rotate)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧩 Rocket Component Breakdown")
    st.markdown("""
    - *Cylindrical Body:* Contains fuel tanks, avionics, and payload.  
    - *Nose Cone:* Aerodynamic tip to reduce drag during ascent.  
    - *Fins:* Stabilize flight during ascent.  
    - *Engine Section:* Provides thrust for liftoff.  
    """)

# -------------------------------------
# FOOTER
# -------------------------------------
st.markdown("---")
st.caption("ARES v2.2 | Built with Streamlit ✨ Scikit-Learn ✨ Plotly 🚀 | Animated by Caroline 💫")
