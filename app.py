import streamlit as st
import random

# --- 🚀 Title ---
st.title("🚀 Growth Mindset Challenge")
st.write("### Adopt a Growth Mindset and Unlock Your Potential! 🌟")

# Growth Mindset Quiz
st.subheader("📝 Growth Mindset Quiz")
st.write("Answer the questions honestly to check your mindset!")

# Questions and Options
questions = [
    ("When faced with a challenge, do you:", ["Give up easily", "Look for an easier way", "Try to find a way to overcome it", "Avoid it"]),
    ("If you fail at something, do you:", ["Believe you are not capable", "Blame external factors", "Take it as a learning experience", "Ignore it"]),
    ("How do you react to constructive criticism?", ["Ignore or feel bad", "Get defensive", "Use it to improve", "Take it personally"]),
    ("When learning something new, do you:", ["Think it's too hard", "Try but give up quickly", "Believe you can improve with practice", "Wait for someone to teach you"]),
    ("Do you set learning goals for yourself?", ["Never", "Rarely", "Sometimes", "Often"]),
    ("When facing a tough problem, do you:", ["Give up", "Complain about it", "Try different solutions", "Wait for help"]),
    ("Do you seek feedback on your work?", ["Never", "Only if forced", "Sometimes", "Yes, to improve"]),
    ("How do you handle failure?", ["Avoid trying again", "Feel discouraged", "Analyze and try again", "Blame luck"]),
    ("Do you believe intelligence is fixed?", ["Yes", "Maybe", "Not sure", "No, it can grow"]),
    ("Do you encourage others to adopt a growth mindset?", ["Never", "Rarely", "Sometimes", "Always"])
]

# Track progress
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0

if st.session_state.current_question < len(questions):
    question, options = questions[st.session_state.current_question]
    answer = st.radio(question, options, key=f'q{st.session_state.current_question}')
    
    if st.button("Next"):
        correct_answer_index = 2  # The correct answer index (adjust if needed)
        if options.index(answer) == correct_answer_index:
            st.session_state.score += 1
        st.session_state.current_question += 1
        st.rerun()
else:
    # Show final result
    st.success(f"🎉 Your Growth Mindset Score: {st.session_state.score}/{len(questions)}")
    if st.session_state.score == len(questions):
        st.write("🔥 Excellent! You have a strong growth mindset!")
    elif st.session_state.score > len(questions) // 2:
        st.write("💡 Good! Keep working on improving your mindset.")
    else:
        st.write("🚀 Time to shift your mindset! Believe in yourself.")
    
    # Reset button
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()

# Daily Motivational Quote
st.subheader("💡 Daily Growth Mindset Quote")
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "You can always improve; you are never stuck in one place.",
    "Challenges are what make life interesting; overcoming them is what makes life meaningful.",
    "Hard work and determination can outshine natural talent any day."
]
st.write(f"📢 *{random.choice(quotes)}*")

# 👇 Deployment Credit Footer with Social Media Icons 👇
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "🚀 Deployment by <b>Muhammad Anas</b><br><br>"
    "<a href='https://github.com/Anas-ahmed12' target='_blank'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='40' height='40'></a>"
    "&nbsp;&nbsp;"
    "<a href='https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit' target='_blank'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='40' height='40'></a>"
    "</div>", 
    unsafe_allow_html=True
)
