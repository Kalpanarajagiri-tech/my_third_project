import streamlit as st

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🥗",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7f8;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #16a085;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.result-box {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #dddddd;
    text-align: center;
}

.calorie-number {
    font-size: 42px;
    font-weight: bold;
    color: #16a085;
}

.small-text {
    color: #666;
    font-size: 15px;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">🥗 CALORIE CALCULATOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Estimate your daily calorie requirement'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "ℹ️ This calculator provides an estimated calorie requirement "
    "for educational purposes."
)

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

input_col, result_col = st.columns([1.2, 1])

# ==================================================
# PERSONAL DETAILS
# ==================================================

with input_col:

    st.subheader("👤 Personal Details")

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name"
    )

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "🎂 Age",
            min_value=15,
            max_value=100,
            value=20
        )

    with col2:

        gender = st.selectbox(
            "🚻 Gender",
            ["Male", "Female"]
        )

    st.subheader("📏 Body Measurements")

    col1, col2 = st.columns(2)

    with col1:

        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=20.0,
            max_value=250.0,
            value=60.0,
            step=0.5
        )

    with col2:

        height = st.number_input(
            "📏 Height (cm)",
            min_value=100.0,
            max_value=230.0,
            value=165.0,
            step=0.5
        )

    st.subheader("🏃 Activity Level")

    activity = st.selectbox(
        "Select your daily activity",
        [
            "🛋️ Sedentary - Little or no exercise",
            "🚶 Lightly Active - Exercise 1-3 days/week",
            "🏃 Moderately Active - Exercise 3-5 days/week",
            "🏋️ Very Active - Exercise 6-7 days/week",
            "🔥 Extremely Active - Hard training/physical job"
        ]
    )

    st.subheader("🎯 Your Goal")

    goal = st.radio(
        "Choose your goal",
        [
            "⚖️ Maintain Weight",
            "📉 Lose Weight",
            "📈 Gain Weight"
        ]
    )

    calculate = st.button(
        "🔥 Calculate Calories",
        type="primary",
        use_container_width=True
    )

# ==================================================
# RESULT SECTION
# ==================================================

with result_col:

    st.subheader("📊 Your Result")

    if calculate:

        # --------------------------------------------------
        # BMR CALCULATION
        # Mifflin-St Jeor Equation
        # --------------------------------------------------

        if gender == "Male":

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                + 5
            )

        else:

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                - 161
            )

        # --------------------------------------------------
        # ACTIVITY MULTIPLIER
        # --------------------------------------------------

        if "Sedentary" in activity:
            multiplier = 1.2

        elif "Lightly Active" in activity:
            multiplier = 1.375

        elif "Moderately Active" in activity:
            multiplier = 1.55

        elif "Very Active" in activity:
            multiplier = 1.725

        else:
            multiplier = 1.9

        # --------------------------------------------------
        # DAILY CALORIES
        # --------------------------------------------------

        maintenance_calories = bmr * multiplier

        # --------------------------------------------------
        # GOAL CALORIES
        # --------------------------------------------------

        if "Lose" in goal:

            target_calories = maintenance_calories - 500

            interpretation = (
                "Your estimated target is lower than your "
                "maintenance level, which is commonly used "
                "as a calorie-deficit approach."
            )

        elif "Gain" in goal:

            target_calories = maintenance_calories + 300

            interpretation = (
                "Your estimated target is higher than your "
                "maintenance level, which creates a calorie surplus."
            )

        else:

            target_calories = maintenance_calories

            interpretation = (
                "Eating around your estimated maintenance level "
                "may help maintain your current weight."
            )

        # --------------------------------------------------
        # RESULT CARD
        # --------------------------------------------------

        st.markdown(
            f"""
            <div class="result-box">

                <div class="small-text">
                    Estimated Daily Calories
                </div>

                <div class="calorie-number">
                    {target_calories:.0f} kcal
                </div>

                <div class="small-text">
                    per day
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # --------------------------------------------------
        # BMR
        # --------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🔥 BMR",
                f"{bmr:.0f} kcal"
            )

        with col2:

            st.metric(
                "⚡ Maintenance",
                f"{maintenance_calories:.0f} kcal"
            )

        # --------------------------------------------------
        # INTERPRETATION
        # --------------------------------------------------

        st.markdown(
            f"""
            <div class="info-card">

            <h4>💡 Simple Interpretation</h4>

            <p>{interpretation}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # --------------------------------------------------
        # USER SUMMARY
        # --------------------------------------------------

        st.markdown("### 👤 Your Details")

        st.write(f"**Name:** {name if name else 'Guest'}")
        st.write(f"**Age:** {age} years")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Height:** {height} cm")
        st.write(f"**Goal:** {goal}")

    else:

        st.info(
            "👈 Enter your details and click "
            "**Calculate Calories** to see your result."
        )

# --------------------------------------------------
# RESET
# --------------------------------------------------

st.divider()

if st.button(
    "🔄 Reset Calculator",
    use_container_width=True
):

    st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    '🥗 Calorie Calculator • Built with Python & Streamlit ❤️'
    '</div>',
    unsafe_allow_html=True
)