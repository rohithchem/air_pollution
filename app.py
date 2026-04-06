import streamlit as st

st.set_page_config(page_title="Air Quality Virtual Lab", layout="wide")

# Sidebar Navigation
section = st.sidebar.radio("Select Section", [
    "Aim & Theory", "Experiment", "Quiz", "Feedback"
])

# ---------------- AIM + THEORY ----------------
if section == "Aim & Theory":
    st.title("🎯 Aim & 📘 Theory")

    st.header("Aim")
    st.write("""
    To study air composition and classify air quality based on the percentage of gases present.
    """)

    st.header("Theory")
    st.write("""
    Air is a mixture of gases:
    
    - Oxygen (~21%) → essential for life  
    - Carbon dioxide (~0.04%) → increases due to pollution  
    - Carbon monoxide (CO) → highly toxic  
    - Sulfur dioxide (SO₂) → causes acid rain and irritation  
    - Nitrogen dioxide (NO₂) → harmful to lungs  

    Based on concentration levels, air can be classified as:
    Very Healthy, Safe, Moderate, Toxic, or Dangerous.
    """)

# ---------------- EXPERIMENT ----------------
elif section == "Experiment":
    st.title("🧪 Experiment")

    o2 = st.slider("Oxygen (O₂ %)", 0.0, 25.0, 21.0)
    co2 = st.slider("Carbon Dioxide (CO₂ %)", 0.0, 10.0, 0.04)
    co = st.slider("Carbon Monoxide (CO %)", 0.0, 5.0, 0.0)
    so2 = st.slider("Sulfur Dioxide (SO₂ %)", 0.0, 2.0, 0.0)
    no2 = st.slider("Nitrogen Dioxide (NO₂ %)", 0.0, 2.0, 0.0)

    def classify_air(o2, co2, co, so2, no2):
        if co > 1 or so2 > 0.5 or no2 > 0.5:
            return "☠️ Dangerous"
        elif co > 0.3 or so2 > 0.2 or no2 > 0.2:
            return "🚫 Toxic"
        elif co2 > 1 or o2 < 19:
            return "⚠️ Moderate"
        elif 20 <= o2 <= 22 and co2 < 0.1:
            return "🌿 Very Healthy"
        else:
            return "✅ Safe"

    if st.button("Analyze Air"):
        result = classify_air(o2, co2, co, so2, no2)
        st.success(f"Result: {result}")

# ---------------- QUIZ ----------------
elif section == "Quiz":
    st.title("🧠 Quiz (10 Questions)")

    score = 0
    answers = []

    answers.append(st.radio("1. Normal oxygen level in air is:", ["10%", "21%", "50%"]))
    answers.append(st.radio("2. Which gas is most toxic?", ["Oxygen", "Carbon Monoxide", "Nitrogen"]))
    answers.append(st.radio("3. High CO₂ causes:", ["Better air", "Breathing issues", "No effect"]))
    answers.append(st.radio("4. SO₂ mainly causes:", ["Acid rain", "Cooling", "No effect"]))
    answers.append(st.radio("5. NO₂ affects:", ["Skin only", "Lungs", "Hair"]))
    answers.append(st.radio("6. Safe oxygen range is:", ["5–10%", "20–22%", "30–40%"]))
    answers.append(st.radio("7. CO is dangerous because:", ["It smells nice", "It blocks oxygen in blood", "It cools air"]))
    answers.append(st.radio("8. Clean air has CO₂ around:", ["5%", "0.04%", "10%"]))
    answers.append(st.radio("9. Air with low oxygen is:", ["Healthy", "Dangerous", "Neutral"]))
    answers.append(st.radio("10. Pollution increases:", ["CO₂", "O₂", "Helium"]))

    if st.button("Submit Quiz"):
        if answers[0] == "21%": score += 1
        if answers[1] == "Carbon Monoxide": score += 1
        if answers[2] == "Breathing issues": score += 1
        if answers[3] == "Acid rain": score += 1
        if answers[4] == "Lungs": score += 1
        if answers[5] == "20–22%": score += 1
        if answers[6] == "It blocks oxygen in blood": score += 1
        if answers[7] == "0.04%": score += 1
        if answers[8] == "Dangerous": score += 1
        if answers[9] == "CO₂": score += 1

        st.success(f"Your Score: {score}/10")

# ---------------- FEEDBACK ----------------
elif section == "Feedback":
    st.title("💬 Feedback")

    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
