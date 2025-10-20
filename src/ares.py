import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go


# PAGE CONFIG

st.set_page_config(page_title="ARES - AI Rocket & Habitat Design", layout="wide")


# CUSTOM CSS ANIMATIONS

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


# APP TITLE

st.title(" ARES - AI Rocket & Habitat Design Assistant")
st.markdown("### Welcome to ARES: Your intelligent AI for designing and visualizing space habitats and rockets.")


# SIDEBAR NAVIGATION

page = st.sidebar.radio(
    "Navigate",
    [" AI Assistant", " Habitat Optimizer", " Rocket Visualization"]
)


# PAGE 1: AI ASSISTANT

if page == " AI Assistant":
    st.header(" ARES Interactive Knowledge Assistant")
    user_input = st.text_input("Type your question here:")

    # Knowledge dictionary
    knowledge = {
        # 🚀 Rocket Basics
        "rocket": "A rocket is a vehicle designed to travel into space by producing thrust through fuel combustion.",
        "fuel": "Rocket fuel provides the chemical energy converted into thrust to propel the rocket.",
        "oxidizer": "An oxidizer provides oxygen to fuel in space, since there is no atmospheric oxygen.",
        "engine": "The rocket engine generates thrust to lift the rocket off the ground.",
        "thrust": "Thrust is the force that propels the rocket forward, overcoming gravity and drag.",
        "payload": "Payload is the cargo a rocket carries, like satellites, instruments, or crew.",
        "stages": "Rockets often have multiple stages that detach to reduce weight and improve efficiency.",
        "fin": "Fins stabilize the rocket during flight and help maintain proper orientation.",
        "nose cone": "The nose cone is the aerodynamic tip of the rocket that reduces drag during ascent.",
        "launch": "Launch is the process of sending a rocket from Earth into space.",
        "orbit": "An orbit is the path a spacecraft follows around a celestial body due to gravity.",
        "gravity": "Gravity is the force pulling objects toward each other; rockets must overcome it to launch.",

        # 🏠 Space Habitat Basics
        "habitat": "A space habitat is a structure designed to support life in space, providing air, water, temperature control, and space for activities.",
        "nhv": "NHV stands for Net Habitable Volume; it’s the usable living space in a habitat.",
        "crew": "Crew refers to the astronauts or people living in the habitat.",
        "sleep volume": "Sleep volume is the space allocated per person for sleeping and rest.",
        "social volume": "Social volume is the shared space for communal activities and recreation.",
        "exercise volume": "Exercise volume is the area allocated for physical activity to maintain health in microgravity.",

        # 🌌 Space & Physics
        "microgravity": "Microgravity is the condition in space where objects appear weightless.",
        "vacuum": "Space is a vacuum, meaning it has no atmosphere, air, or drag.",
        "life support": "Life support systems provide oxygen, remove CO2, regulate temperature, and manage water and waste.",
        "radiation": "Space radiation comes from the sun and cosmic rays; habitats must shield crew from it.",
        "spacewalk": "A spacewalk is when an astronaut exits the habitat to work outside in space with a suit.",

        # 🛠 Misc / App Terms
        "comfort score": "Comfort score is a numerical value predicting crew satisfaction based on habitat design.",
        "optimization": "Optimization means adjusting habitat parameters to maximize comfort or efficiency.",
        "layout": "Layout refers to how the habitat spaces are arranged, like sleep, social, and exercise areas.",
    }

    if st.button("Ask ARES"):
        if user_input.strip() == "":
            st.warning("Please enter a question first.")
        else:
            text = user_input.lower()
            found = False
            for key, ans in knowledge.items():
                if key in text:
                    st.success(ans)
                    found = True
                    break
            if not found:
                st.info("ARES: I’m still learning about this topic! You can ask about rockets, fuel, habitat design, or space terms.")


#  PAGE 2: HABITAT OPTIMIZER

elif page == " Habitat Optimizer":
    st.header(" AI Habitat Comfort Optimizer")

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


# PAGE 3: ROCKET VISUALIZATION

elif page == " Rocket Visualization":
    st.header(" 3D Rocket Visualization (Interactive)")

    # Sidebar parameters
    st.sidebar.header("Rocket Parameters")
    height = st.sidebar.slider("Rocket Body Height (m)", 5.0, 20.0, 10.0)
    body_radius = st.sidebar.slider("Body Radius (m)", 0.5, 3.0, 1.0)
    nose_height = st.sidebar.slider("Nose Cone Height (m)", 1.0, 5.0, 2.0)
    fin_count = st.sidebar.slider("Number of Fins", 0, 6, 3)
    fin_height = st.sidebar.slider("Fin Height (m)", 0.2, 2.0, 0.5)
    flame_radius = st.sidebar.slider("Flame Radius (m)", 0.2, 1.5, 0.5)
    flame_height = st.sidebar.slider("Flame Height (m)", 0.5, 2.0, 1.0)

    theta = np.linspace(0, 2 * np.pi, 30)

    # --- Rocket Body ---
    z = np.linspace(0, height, 50)
    Z, THETA = np.meshgrid(z, theta)
    X = body_radius * np.cos(THETA)
    Y = body_radius * np.sin(THETA)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z,
                             surfacecolor=Z,
                             colorscale=[[0, "rgb(180,180,180)"], [1, "rgb(90,90,90)"]],
                             showscale=False))

    # --- Nose Cone ---
    nose_z = np.linspace(height, height + nose_height, 20)
    nose_r = np.linspace(body_radius, 0, 20)
    NoseZ, NoseTheta = np.meshgrid(nose_z, theta)
    NoseX = np.outer(np.ones_like(theta), nose_r) * np.cos(NoseTheta)
    NoseY = np.outer(np.ones_like(theta), nose_r) * np.sin(NoseTheta)
    fig.add_trace(go.Surface(x=NoseX, y=NoseY, z=NoseZ,
                             surfacecolor=NoseZ,
                             colorscale=[[0, "rgb(220,220,220)"], [1, "rgb(120,120,120)"]],
                             showscale=False))

    # --- Fins ---
    for i in range(fin_count):
        angle = i * 2 * np.pi / fin_count
        fin_x = np.array([body_radius, body_radius + 0.5, body_radius + 0.5, body_radius])
        fin_y = np.array([-0.1, -0.1, 0.1, 0.1])
        fin_z = np.array([0, 0, fin_height, fin_height])
        finX_rot = fin_x * np.cos(angle) - fin_y * np.sin(angle)
        finY_rot = fin_x * np.sin(angle) + fin_y * np.cos(angle)
        fig.add_trace(go.Mesh3d(x=finX_rot, y=finY_rot, z=fin_z,
                                 color='red', opacity=0.8))

    # --- Flame ---
    flame_r = np.linspace(0, flame_radius, 10)
    flame_z = np.linspace(-flame_height, 0, 10)
    FR, FT = np.meshgrid(flame_r, theta)
    FZ, _ = np.meshgrid(flame_z, theta)
    FlameX = FR * np.cos(FT)
    FlameY = FR * np.sin(FT)
    FlameZ = FZ
    fig.add_trace(go.Surface(x=FlameX, y=FlameY, z=FlameZ,
                             surfacecolor=FlameZ,
                             colorscale=[[0, "yellow"], [0.5, "orange"], [1, "red"]],
                             opacity=0.6, showscale=False))

    # --- Layout ---
    camera = dict(eye=dict(x=1.5, y=1.5, z=1.2))
    fig.update_layout(scene=dict(
            xaxis=dict(title='X (m)'),
            yaxis=dict(title='Y (m)'),
            zaxis=dict(title='Height (m)'),
            aspectmode='data',
            camera=camera
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        height=700,
        title=" Interactive Rocket Model (Drag to Rotate)"
    )

    st.plotly_chart(fig, use_container_width=True)
