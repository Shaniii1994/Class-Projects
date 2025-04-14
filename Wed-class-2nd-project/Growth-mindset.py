#streamlit
import streamlit as st

# Set the page config
st.set_page_config(page_title="Growth Mindset Challenge 💻🌱")
st.title("Growth Mindset Challenge: 🚀✨ Web App with Streamlit! 💻🌱 Ready to level up?🌟")

st.header("Welcome to Your Growth Journey! 🌱✨ Let’s embark on a path of self-discovery, challenges, and endless possibilities! 🚀💡 Get ready to unlock your full potential! 🔓🌟")
st.write("Embrace challenges, learn from every step, and unlock your true potential! 💪✨ This AI-powered app is designed to help you build a growth mindset through reflection, challenges, and celebrating achievements! 🚀🌱 Let’s grow together! 🌟")

#quote

st.header("The Power of Growth Mindset 💡🌱 Believe in your ability to evolve and grow with every challenge! 💪🚀")
st.write("The power of a growth mindset lies in believing that change happens when we take action and work towards our goals. 💪🌱 By embracing this mindset, you'll realize you can achieve amazing things, no matter how hard you try! 🚀🎯 Keep pushing forward! 🌟✨")

st.header("What's your challenge today? 💪🔍 Let’s tackle it together! 🚀🌱")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward towards your goal! 💪🚀 Every step brings you closer! 🌟🎯")
else:
    st.warning("Tell us about your challenge to get started! Let’s break it down together! 💪🚀")


#reflection
st.header("Reflection on Your Learning 🧠✨")
reflection = st.text_area("What's the reflective outcome: 🌱💡 What insights have you gained from your journey? 🤔 What strengths have emerged? 💪")

if reflection:
    st.success(f"Great Insight! 🌟 Your reflection: 💭 {reflection}")
else:
    st.info("Reflection on past experiences helps you improve your journey, growth, and progress! 🌱💡 What challenges have you faced along the way? Share your difficulties")


#achievement

st.header("Celebrate Your Achievements 🎉🏆 Every milestone, big or small, is a victory! 🌟✨")
achievement = st.text_input("Describe an achievement you've made: 🌟🎉 What’s a moment you’re proud of? ✨")

if achievement:
    st.success(f"Congratulations! 🎉🏅 Your achievement: 🌟 �� {achievement}")
else:
    st.info("Celebrating your achievements helps you stay motivated and inspired! 🎉💪 Every step forward is worth recognizing! 🌟 Let’s keep the momentum going! 👏🚀✨")


#footer
st.write("_ _ _ ")
st.write("Success is the sum of small efforts, repeated day in and day out. 💪🌱 Keep going, even when it gets tough — your growth is inevitable! 🚀✨")
st.write("**©️ Created by Shanyal Siddiqui ✨🌟**")