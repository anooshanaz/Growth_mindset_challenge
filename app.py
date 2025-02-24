# import streamlit as st
# import pandas as pd
# # import os from io 
# # import BytesIo


# #Color palatte
# colors=["Red","Black","Blue","Green","Pink","Purple","Gray","White"]
# # #setup our app
# st.set_page_config(page_title="📜 Data Sweeper!", layout='wide')
# st.title("Colour Peronality Test!")

# #Colour wheel


# #colour section box
# st.selectbox("Colors",colors)





# import streamlit as st

# # Title of the app
# st.title("Personality Color Test")

# # Function to calculate personality color based on user responses
# def calculate_personality_color(responses):
#     total_score = sum(responses)
    
#     if total_score <= 5:
#         return ("Blue", "Calm and Peaceful", "#0000FF")  # Blue
#     elif total_score <= 10:
#         return ("Green", "Growth and Harmony", "#00FF00")  # Green
#     elif total_score <= 15:
#         return ("Yellow", "Cheerful and Optimistic", "#FFFF00")  # Yellow
#     else:
#         return ("Red", "Energetic and Passionate", "#FF0000")  # Red

# # Initialize session state for responses
# if "responses" not in st.session_state:
#     st.session_state.responses = [3] * 4  # Default value for each question

# # Questions for the personality test
# questions = [
#     "1. Do you enjoy spending time alone? (1 = Rarely, 5 = Always)",
#     "2. Are you a naturally optimistic person? (1 = Rarely, 5 = Always)",
#     "3. Do you enjoy helping others? (1 = Rarely, 5 = Always)",
#     "4. Are you a risk-taker? (1 = Rarely, 5 = Always)"
# ]

# # Collect user responses
# st.header("Answer the following questions:")
# for i, question in enumerate(questions):
#     st.session_state.responses[i] = st.slider(
#         question, 1, 5, st.session_state.responses[i]  # Use session state to persist values
#     )

# # Calculate personality color
# if st.button("Find My Personality Color"):
#     color, meaning, hex_code = calculate_personality_color(st.session_state.responses)
    
#     # Display the result
#     st.success(f"Your Personality Color is **{color}**!")
#     st.write(f"**Meaning**: {meaning}")
    
#     # Show the color preview
#     st.write("**Color Preview**:")
#     st.markdown(
#         f'<div style="width: 200px; height: 200px; background-color: {hex_code};"></div>',
#         unsafe_allow_html=True
#     )
    
#     # Optional: Add a fun message
#     st.balloons()  # Celebrate the result with balloons!

# # Reset functionality
# if st.button("Reset Test"):
#     st.session_state.responses = [3] * 4  # Reset responses to default values
#     st.experimental_rerun()  # Rerun the app to reflect changes

import streamlit as st

# Title of the app
st.title("🌈Simple Color Picker")

# Sidebar for RGB sliders
st.sidebar.header("🌴Adjust RGB Values🌴")

# Sliders for Red, Green, and Blue
red = st.sidebar.slider("❤️Red", 0, 255, 128)
green = st.sidebar.slider("💚Green", 0, 255, 128)
blue = st.sidebar.slider("💙Blue", 0, 255, 128)

# Display the selected color
st.write(f"Selected RGB Color: ({red}, {green}, {blue})")

# Show a preview of the selected color
st.write("❄️Color Preview:")
st.markdown(
    f'<div style="width: 200px; height: 200px; background-color: rgb({red}, {green}, {blue});"></div>',
    unsafe_allow_html=True
)

# Optional: Add a hex color code display
hex_color = f"#{red:02X}{green:02X}{blue:02X}"
st.write(f"Hex Color Code: {hex_color}")