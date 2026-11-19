
import streamlit as st

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Daily Health Checker",
    page_icon="💚",
    layout="centered"
)

# -----------------------------------
# APPLICATION TITLE
# -----------------------------------

st.title("💚 Daily Health Checker")
st.write("Welcome! Track your daily health habits and improve your lifestyle.")
st.markdown("---")

# -----------------------------------
# RESET FUNCTION
# -----------------------------------

def reset_inputs():
    keys = [
        "name", "age", "sleep", "water",
        "exercise", "screen", "mood"
    ]

    defaults = {
        "name": "",
        "age": 18,
        "sleep": 8.0,
        "water": 8,
        "exercise": 30,
        "screen": 4.0,
        "mood": "Happy 😊"
    }

    for key in keys:
        st.session_state[key] = defaults[key]


# -----------------------------------
# USER INPUT SECTION
# -----------------------------------

st.header("📝 Enter Your Daily Health Details")

name = st.text_input(
    "Enter Your Name",
    key="name",
    placeholder="Your name"
)

age = st.number_input(
    "Enter Your Age",
    min_value=1,
    max_value=120,
    value=18,
    step=1,
    key="age"
)

sleep = st.number_input(
    "Hours of Sleep",
    min_value=0.0,
    max_value=24.0,
    value=8.0,
    step=0.5,
    key="sleep"
)

water = st.number_input(
    "Glasses of Water Consumed",
    min_value=0,
    max_value=30,
    value=8,
    step=1,
    key="water"
)

exercise = st.number_input(
    "Daily Exercise Duration (minutes)",
    min_value=0,
    max_value=600,
    value=30,
    step=5,
    key="exercise"
)

screen = st.number_input(
    "Daily Screen Time (hours)",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.5,
    key="screen"
)

mood = st.selectbox(
    "How is your mood today?",
    ["Happy 😊", "Sad 😢", "Stressed 😟", "Energetic ⚡"],
    key="mood"
)

st.markdown("---")

# -----------------------------------
# WELLNESS SCORE FUNCTION
# -----------------------------------

def calculate_score(sleep, water, exercise, screen, mood):

    score = 0

    # Sleep score (25 points)
    if 7 <= sleep <= 9:
        score += 25
    elif 6 <= sleep < 7 or 9 < sleep <= 10:
        score += 18
    elif 5 <= sleep < 6:
        score += 10
    else:
        score += 5

    # Water score (20 points)
    if water >= 8:
        score += 20
    elif water >= 6:
        score += 15
    elif water >= 4:
        score += 10
    else:
        score += 5

    # Exercise score (25 points)
    if exercise >= 30:
        score += 25
    elif exercise >= 20:
        score += 18
    elif exercise >= 10:
        score += 12
    else:
        score += 5

    # Screen time score (15 points)
    if screen <= 3:
        score += 15
    elif screen <= 5:
        score += 12
    elif screen <= 7:
        score += 8
    else:
        score += 4

    # Mood score (15 points)
    if mood == "Happy 😊":
        score += 15
    elif mood == "Energetic ⚡":
        score += 15
    elif mood == "Sad 😢":
        score += 8
    elif mood == "Stressed 😟":
        score += 8

    return score


# -----------------------------------
# HEALTH ANALYSIS FUNCTION
# -----------------------------------

def health_analysis(sleep, water, exercise, screen, mood):

    st.header("📊 Your Personalized Health Analysis")

    # Sleep analysis
    st.subheader("😴 Sleep Analysis")

    if 7 <= sleep <= 9:
        st.success("Great! Your sleep duration is within the target range.")
    elif sleep < 7:
        st.warning("You may need more sleep. Try maintaining a regular sleep schedule.")
    else:
        st.info("You slept more than 9 hours. Consider whether this is typical for you.")

    # Water analysis
    st.subheader("💧 Water Consumption")

    if water >= 8:
        st.success("Good job! You have reached the app's daily water goal.")
    elif water >= 5:
        st.warning("Try drinking more water throughout the day.")
    else:
        st.warning("Your water intake is relatively low. Remember to stay hydrated.")

    # Exercise analysis
    st.subheader("🏃 Exercise Analysis")

    if exercise >= 30:
        st.success("Excellent! You completed at least 30 minutes of exercise.")
    elif exercise >= 15:
        st.info("Good effort! Try gradually increasing your daily activity.")
    else:
        st.warning("Try adding a short walk or light physical activity to your day.")

    # Screen time analysis
    st.subheader("📱 Screen Time Analysis")

    if screen <= 3:
        st.success("Great! Your screen time is relatively low.")
    elif screen <= 6:
        st.info("Try taking regular breaks from screens.")
    else:
        st.warning("Your screen time is high. Consider reducing unnecessary screen use.")

    # Mood analysis
    st.subheader("😊 Mood Analysis")

    if mood == "Happy 😊":
        st.success("Wonderful! Keep doing activities that make you happy.")
    elif mood == "Energetic ⚡":
        st.success("Great energy! Use it for positive activities.")
    elif mood == "Sad 😢":
        st.info("Take some time for yourself and consider talking to someone you trust.")
    elif mood == "Stressed 😟":
        st.warning("Try relaxation, deep breathing, or taking a short break.")


# -----------------------------------
# RECOMMENDATION FUNCTION
# -----------------------------------

def recommendations(sleep, water, exercise, screen, mood):

    st.header("💡 Healthy Lifestyle Recommendations")

    suggestions = []

    if sleep < 7:
        suggestions.append("😴 Maintain a regular sleep schedule and aim for sufficient rest.")

    if water < 8:
        suggestions.append("💧 Drink water regularly throughout the day.")

    if exercise < 30:
        suggestions.append("🏃 Add a daily walk or another enjoyable physical activity.")

    if screen > 5:
        suggestions.append("📱 Reduce unnecessary screen time and take regular breaks.")

    if mood == "Sad 😢":
        suggestions.append("❤️ Connect with friends or family and make time for activities you enjoy.")

    if mood == "Stressed 😟":
        suggestions.append("🧘 Practice deep breathing, meditation, or another relaxing activity.")

    if len(suggestions) == 0:
        st.success("Excellent! Keep maintaining your healthy daily habits.")

    else:
        for suggestion in suggestions:
            st.write("• " + suggestion)


# -----------------------------------
# BUTTON SECTION
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    check_health = st.button(
        "🔍 Check My Health",
        use_container_width=True
    )

with col2:
    st.button(
        "🔄 Reset Inputs",
        use_container_width=True,
        on_click=reset_inputs
    )


# -----------------------------------
# DISPLAY RESULTS
# -----------------------------------

if check_health:

    if name.strip() == "":
        st.error("Please enter your name before checking your health.")

    else:

        st.markdown("---")

        st.header(f"Hello, {name}! 👋")

        st.write(f"**Age:** {age} years")

        # Calculate wellness score
        wellness_score = calculate_score(
            sleep, water, exercise, screen, mood
        )

        # Display score
        st.header("🏆 Your Daily Wellness Score")

        st.metric(
            label="Wellness Score",
            value=f"{wellness_score}/100"
        )

        st.progress(wellness_score / 100)

        # Score feedback
        if wellness_score >= 80:
            st.success("Excellent! You are maintaining healthy daily habits. 🌟")

        elif wellness_score >= 60:
            st.info("Good job! There is some room for improvement. 👍")

        elif wellness_score >= 40:
            st.warning("Your daily habits need some improvement. 💪")

        else:
            st.error("Focus on improving your daily health habits. ❤️")

        # Detailed analysis
        st.markdown("---")

        health_analysis(
            sleep, water, exercise, screen, mood
        )

        # Recommendations
        st.markdown("---")

        recommendations(
            sleep, water, exercise, screen, mood
        )

        # Summary
        st.markdown("---")

        st.header("📋 Daily Health Summary")

        summary = {
            "Name": name,
            "Age": f"{age} years",
            "Sleep": f"{sleep} hours",
            "Water": f"{water} glasses",
            "Exercise": f"{exercise} minutes",
            "Screen Time": f"{screen} hours",
            "Mood": mood,
            "Wellness Score": f"{wellness_score}/100"
        }

        for key, value in summary.items():
            st.write(f"**{key}:** {value}")

        st.markdown("---")

        st.info(
            "Remember: Small healthy habits every day can make "
            "a positive difference!"
        )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "💚 Daily Health Checker | Made with Python and Streamlit"
)

st.caption(
    "This app provides general lifestyle feedback, not medical advice."
)
