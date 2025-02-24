
import streamlit as st

#page setup
st.set_page_config(page_title='🎄Growth mindset', layout='centered')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        color: #FF6F61;
        text-align: center;
        font-weight: bold;
    }
    .header-text {
        font-size: 30px;
        color: #6B5B95;
        font-weight: bold;
    }
    .subheader-text {
        font-size: 24px;
        color: #88B04B;
        font-weight: bold;
    }
    .highlight-text {
        font-size: 18px;
        color: #FFA500;
        font-weight: bold;
    }
    .sidebar-title {
        font-size: 28px;
        color: #034F84;
        font-weight: bold;
    }
    .sidebar-subheader {
        font-size: 20px;
        color: #6B5B95;
        font-weight: bold;
    }
    .footer-text {
        font-size: 16px;
        color: #A52A2A;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar 
st.sidebar.markdown('<p class="sidebar-title">🦋 Anoosha Naz 🦋</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-subheader">Welcome to my Streamlit app!</p>', unsafe_allow_html=True)

st.sidebar.markdown('<p class="sidebar-title">🔰 Learning Hub 🔰</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-title">🌲 Growth Mindset Challenge 🌲</p>', unsafe_allow_html=True)

st.sidebar.write('What your challenge today?')
users_input = st.sidebar.text_input("Describe a challenge you're facing?")
#condition
if users_input:
    st.sidebar.success(f'You are facing: {users_input}. Keep pushing forwords to your goal💪')
else:
    st.sidebar.warning('Tell us about your challenge to get started!')

st.sidebar.write('Reflect on your learning')
users_area = st.sidebar.text_area("Describe your reflection here!")
#condition
if users_area:
    st.sidebar.success(f'💫Great inside your reflection: {users_area}')
else:
    st.sidebar.info('Reflecting on past experience help you grow! Share your difficulties')

st.sidebar.write('Keep celebrate your wins')
achive = st.sidebar.text_input("Share something you have recently accomplished")
#condition
if achive:
    st.sidebar.success(f'Amazing your acheived: {achive}🏆')
else:
    st.sidebar.warning('Big or small every acheivement count! share one now🥳')

# Main content
st.markdown('<p class="main-title">🌴 GROWTH MINDSET CHALLENGE! 🌴</p>', unsafe_allow_html=True)
st.write("A growth mindset is the belief that your abilities and intelligence can be developed through **hard work, perseverance, and learning from your mistakes**. ✈️")

# Motivational section
st.markdown('<p class="header-text">💫💫💫 Why Adopt A Growth Mindset? 💫💫💫</p>', unsafe_allow_html=True)

st.markdown('<p class="subheader-text">🔥 Embrace Challenges</p>', unsafe_allow_html=True)
st.write("View obstacles as opportunities to learn rather than setbacks.")

st.markdown('<p class="subheader-text">❄️ Learn from Mistakes</p>', unsafe_allow_html=True)
st.write("Making mistakes is a natural part of learning.")

st.markdown('<p class="subheader-text">💪 Persist Through Difficulties</p>', unsafe_allow_html=True)
st.write("Stay determined, even when things get tough.")

st.markdown('<p class="subheader-text">🥳 Celebrate Effort</p>', unsafe_allow_html=True)
st.write("Recognize and reward the effort you put into learning.")

st.markdown('<p class="subheader-text">🔎 Keep an Open Mind</p>', unsafe_allow_html=True)
st.write("Stay curious and be willing to adapt.")

# Footer
st.markdown("---")
st.markdown('<p class="footer-text">Remember: Your journey in education is not just about proving your intelligence — it\'s about developing it! 🌟</p>', unsafe_allow_html=True)
