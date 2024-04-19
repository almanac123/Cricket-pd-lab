import streamlit as st
from PIL import Image
import numpy as np

# Function to analyze pitch image
def analyze_pitch(image):
    # Placeholder function, replace with your own image analysis code
    # For demonstration, we'll just return some random values
    cracks_percentage = np.random.randint(0, 100)
    dew_factor = np.random.randint(0, 100)
    grass = np.random.choice(['Sparse', 'Moderate', 'Thick'])
    return cracks_percentage, dew_factor, grass

# Function to display weather conditions
def display_weather_conditions():
    # Placeholder function, replace with your own weather API integration or data
    # For demonstration, we'll just return some random values
    temperature = np.random.randint(10, 40)
    humidity = np.random.randint(0, 100)
    wind_direction = np.random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    return temperature, humidity, wind_direction

# Function to predict team combination
def predict_team_combination():
    # Placeholder function, replace with your own team prediction algorithm
    # For demonstration, we'll just return some sample team combinations
    team_combinations = {
        'Batting': ['Player1', 'Player2', 'Player3'],
        'Spin Bowling': ['Player4', 'Player5', 'Player6'],
        'Seam Bowling': ['Player7', 'Player8', 'Player9']
    }
    return team_combinations

def main():
    # CSS styling for the entire page
    page_style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Algerian&display=swap');
        .{
            font-family: 'Roboto','Arial', sans-serif;  
        }
        .st-emotion-cache-gh2jqd{
            background: none;
            color: #4CAF50;
        }
        .st-emotion-cache-uf99v8{
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHI8xGUxX0Q6O8aHnp6TEjh5yDz2NqkI5Dhk2DvBcdvA&s");
            background-size: cover;
            background-attachment: fixed;
        }
        .st-emotion-cache-1avcm0n{
            display: none;
        }
        .st-emotion-cache-ch5dnh{
            display: none;
        }
        .st-emotion-cache-6qob1r{
            background-color: #40E0D0;
        }
        .st-emotion-cache-cnbvxy p {
            color: blue;
            font-size: 30px;
        }
        .st-emotion-cache-16txtl3 h2{
            font-size: 40px;
        }
        body {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHI8xGUxX0Q6O8aHnp6TEjh5yDz2NqkI5Dhk2DvBcdvA&s");
            font-family: 'Roboto','Arial', sans-serif;
            background-size: cover;
            background-attachment: fixed;
        }
        .st-emotion-cache-gh2jqd {
            background-color: #f0ffff;
            color: #4CAF50;
        }
        .st-emotion-cache-16txtl3 h2{
            font-family: 'Algerian','Arial', sans-serif;
        }
        .stApp {
            max-width: 100vw;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(1, 0, 0, 0.1);
            background-color: #f0ffff;
        }
        .upload-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-top: 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .upload-btn:hover {
            background-color: #45a049;
        }
        .sidebar{
            background-color: #f0ffff;
        }
        .sidebar .sidebar-content {
            color: #333333;
            padding: 20px;
            font-size: 20px;
        }
        .sidebar .sidebar-content h2 {
            color: rgb(255,0,0);
            padding-left: 10px;
            margin-top: 20px;
        }
        .sidebar .sidebar-content p {
            color: #555555;
            padding-left: 10px;
            margin-top: 10px;
        }
        .st-emotion-cache-gh2jqd{
            background-color: #FFFDD0
        }
        </style>
    """

    st.markdown(page_style, unsafe_allow_html=True)

    # Title and Description
    st.markdown("<h1 style='text-align: center; color: #333333;'>CRICKET TEAM PREDICTION APP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555555; font-size: 18px;'>Upload a pitch image to get analysis and team predictions</p>", unsafe_allow_html=True)

    # Upload pitch image
    pitch_image = st.file_uploader('Upload pitch image', type=['jpg', 'png', 'jpeg'], key='file_uploader')

    if pitch_image is not None:
        # Display pitch image
        # st.image(pitch_image, caption='Uploaded pitch image', use_column_width=True)

        # Analyze pitch
        cracks_percentage, dew_factor, grass = analyze_pitch(pitch_image)
        st.sidebar.markdown("<h2 style='color: rgb(255,0,0);'>Pitch Analysis</h2>", unsafe_allow_html=True)
        st.sidebar.write(f'Cracks Percentage: {cracks_percentage}%')
        st.sidebar.write(f'Dew Factor: {dew_factor}')
        st.sidebar.write(f'Grass on Pitch: {grass}')

        # Display weather conditions
        temperature, humidity, wind_direction = display_weather_conditions()
        st.sidebar.markdown("<h2 style='color: rgb(255,0,0);'>Weather Conditions</h2>", unsafe_allow_html=True)
        st.sidebar.write(f'Temperature: {temperature}°C')
        st.sidebar.write(f'Humidity: {humidity}%')
        st.sidebar.write(f'Wind Direction: {wind_direction}')

        # Predict team combination
        team_combinations = predict_team_combination()
        st.markdown("<h2 style='color: #000000;'>Team Combination</h2>", unsafe_allow_html=True)
        for category, players in team_combinations.items():
            st.write(f'{category}: {", ".join(players)}')

if _name_ == "_main_":
    main()