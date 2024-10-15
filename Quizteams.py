import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Define the data
data = [
    ["Davey, Michael", 1, "Finding Nemo"],
    ["Morris, Jonathan", 1, "Finding Nemo"],
    ["O Connor, Adrian", 1, "Finding Nemo"],
    ["OCallaghan, Lissa", 1, "Finding Nemo"],
    ["Pollock, Karen", 1, "Finding Nemo"],
    ["Shaw, Peter", 1, "Finding Nemo"],
    ["Bradley, Kevin", 2, "Flow Force"],
    ["Clarke, Ryan", 2, "Flow Force"],
    ["Devlin, Caoimhe", 2, "Flow Force"],
    ["Jamgade, Deepak", 2, "Flow Force"],
    ["Knox, Seana", 2, "Flow Force"],
    ["Toner, Leon", 2, "Flow Force"],
    ["Cooper, Jane", 3, "Wave Wizards"],
    ["Hewes, Selene", 3, "Wave Wizards"],
    ["Kelly, Tess", 3, "Wave Wizards"],
    ["McCallion, Emma", 3, "Wave Wizards"],
    ["Millen, Emma", 3, "Wave Wizards"],
    ["Thomas, Kelly", 3, "Wave Wizards"],
    ["Cammock, Lauren", 4, "Splash Squad"],
    ["Glackin, Ellie", 4, "Splash Squad"],
    ["Goulding, Andrew", 4, "Splash Squad"],
    ["Lavery, Alan (Belfast)", 4, "Splash Squad"],
    ["McBride, Alastair", 4, "Splash Squad"],
    ["Mclaughlin, Shane", 4, "Splash Squad"],
    ["Agnew, David", 5, "Pipe Pipers"],
    ["Devlin, Arthur", 5, "Pipe Pipers"],
    ["Kirkpatrick, Mark", 5, "Pipe Pipers"],
    ["Mc Cambridge, Fergus", 5, "Pipe Pipers"],
    ["McKendry, Julie", 5, "Pipe Pipers"],
    ["McManus, Sam", 5, "Pipe Pipers"],
    ["Halliday, Andrew", 6, "Liquid Logic"],
    ["Hughes, James", 6, "Liquid Logic"],
    ["Killough, Jamie", 6, "Liquid Logic"],
    ["Mcconnell, Michael (Belfast)", 6, "Liquid Logic"],
    ["McEvoy, Orla", 6, "Liquid Logic"],
    ["Ritchie, Matthew", 6, "Liquid Logic"],
    ["Lawther, Sasha", 7, "H2O just add water"],
    ["McAleese, Paul", 7, "H2O just add water"],
    ["McCarron, Emma", 7, "H2O just add water"],
    ["McClean, Shane", 7, "H2O just add water"],
    ["Morgan, Connor", 7, "H2O just add water"],
    ["Wade, Joseph", 7, "H2O just add water"],
    ["Bell, Joel", 8, "G.I.Guessing"],
    ["Brown, Megan", 8, "G.I.Guessing"],
    ["Deakin, Lewis", 8, "G.I.Guessing"],
    ["Johnston, Gordon", 8, "G.I.Guessing"],
    ["Kelly, Grainne", 8, "G.I.Guessing"],
    ["Tohill, Therese", 8, "G.I.Guessing"],
    ["Cunningham, Keith", 9, "Wastewater trivia works"],
    ["Knox, Peter", 9, "Wastewater trivia works"],
    ["McEneaney, Sasha", 9, "Wastewater trivia works"],
    ["Mckillen, David", 9, "Wastewater trivia works"],
    ["Murray, John", 9, "Wastewater trivia works"],
    ["Sadowski, Damian", 9, "Wastewater trivia works"],
    ["Briggs, Gareth", 10, "The Filtration Faction"],
    ["Gould, Mark", 10, "The Filtration Faction"],
    ["Keys, Claire", 10, "The Filtration Faction"],
    ["Lough, Robbie", 10, "The Filtration Faction"],
    ["Christine McGrath", 10, "The Filtration Faction"],
    ["McGuigan, Dearbhla", 10, "The Filtration Faction"],
    ["Bain, Rowan", 11, "Reservoir Rangers"],
    ["Cheng, Andrew", 11, "Reservoir Rangers"],
    ["Lennon, Brian", 11, "Reservoir Rangers"],
    ["Martin, Stephanie", 11, "Reservoir Rangers"],
    ["McAuley, Finn", 11, "Reservoir Rangers"],
    ["Valentim Gomes, Ludmila", 11, "Reservoir Rangers"],
    ["Bell, David", 12, "Tide Team Six"],
    ["Berry, Seth", 12, "Tide Team Six"],
    ["Donaldson, Samuel", 12, "Tide Team Six"],
    ["Kerr, Michael", 12, "Tide Team Six"],
    ["McCune, David", 12, "Tide Team Six"],
    ["Brown, James", 12, "Tide Team Six"],
    ["Burleigh, Carrie", 13, "The Pressure Pros"],
    ["Finlay, Hannah", 13, "The Pressure Pros"],
    ["Heyburn, Philip", 13, "The Pressure Pros"],
    ["Mathew, Sherin", 13, "The Pressure Pros"],
    ["Reddy, Devan", 13, "The Pressure Pros"],
    ["Joanne Titterington", 13, "The Pressure Pros"],
    ["Fair, Shaun", 14, "Droplet Dynamos"],
    ["Teixeira Gomes, Edgar", 14, "Droplet Dynamos"],
    ["Bright, Robert", 14, "Droplet Dynamos"],
    ["PONGASSERIL SANTHOSH, SREE", 14, "Droplet Dynamos"],
    ["Sanders, Adam", 14, "Droplet Dynamos"]
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["Name", "Team", "Team Name"])

# Function to search for a name
def search_name(name):
    name_parts = name.lower().split()
    return df[df['Name'].apply(lambda x: all(part in x.lower() for part in name_parts))]

# Set up the Streamlit page
st.set_page_config(page_title="AECOM Quiz Team Finder", page_icon="🔍", layout="wide")

# Dark mode toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.sidebar.button("Toggle Dark/Light Mode", on_click=toggle_dark_mode)

if st.session_state.dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Welcome message and instructions
st.title("Welcome to AECOM Quiz Team Finder! 🎉")
st.markdown("""
This app helps you find your team for the upcoming AECOM Quiz Night. Here's how to use it:
1. Enter your name in the search box below
2. View your team information and teammates
3. Explore other features like team statistics and the full team list
""")

# Countdown timer
quiz_date = datetime(2024, 10, 20, 19, 0)  # Adjust to your actual quiz date and time
now = datetime.now()
time_left = quiz_date - now

st.sidebar.header("Quiz Countdown")
st.sidebar.write(f"Days: {time_left.days}")
st.sidebar.write(f"Hours: {time_left.seconds // 3600}")
st.sidebar.write(f"Minutes: {(time_left.seconds % 3600) // 60}")

# Random fun facts
fun_facts = [
    "AECOM has been recognized as one of the World's Most Ethical Companies.",
    "The average person uses 80-100 gallons of water per day.",
    "AECOM has worked on projects in more than 150 countries.",
    "Only 3% of the Earth's water is freshwater.",
    "AECOM was founded in 1990.",
]

st.sidebar.header("Did You Know?")
st.sidebar.write(random.choice(fun_facts))

# Title and information
st.header("Find Your Team")
st.info("Note: Teams were generated randomly. For any queries, please contact Mark Kirkpatrick.")

# Name search functionality
name = st.text_input("Enter your name:")

if name:
    results = search_name(name)
    if not results.empty:
        for _, result in results.iterrows():
            team_number = result['Team']
            team_name = result['Team Name']
            st.success(f"You are on Team {team_number}: {team_name}")
            
            # Display team members
            st.subheader("Your Team Members:")
            team_members = df[df["Team"] == team_number]["Name"].tolist()
            for member in team_members:
                st.write(f"- {member}")
            
            # Display team information in a more visually appealing way
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Team Number", team_number)
            with col2:
                st.metric("Team Name", team_name)
    else:
        st.error("Name not found. Please check the spelling and try again.")
        st.write("Tip: You can enter your first name, last name, or both in any order. The search is case-insensitive.")
        st.warning("If your name doesn't appear, please see Mark Kirkpatrick for assistance.")

# Display the full team list
if st.checkbox("Show full team list"):
    st.dataframe(df)

# Team statistics
if st.checkbox("Show team statistics"):
    st.subheader("Team Statistics")
    total_participants = len(df)
    total_teams = df['Team'].nunique()
    st.write(f"Total number of participants: {total_participants}")
    st.write(f"Number of teams: {total_teams}")
    st.write("Participants per team:")
    team_sizes = df['Team'].value_counts().sort_index()
    st.bar_chart(team_sizes)

# Team name search
st.subheader("Search for a Team")
team_search = st.text_input("Enter a team name:")
if team_search:
    matching_teams = df[df['Team Name'].str.contains(team_search, case=False)]
    if not matching_teams.empty:
        st.write("Matching teams:")
        st.dataframe(matching_teams)
    else:
        st.write("No matching teams found.")

# Feedback form
st.header("We'd Love Your Feedback!")
feedback = st.text_area("Please share your thoughts or suggestions about the quiz night or this app:")
if st.button("Submit Feedback"):
    # In a real app, you'd save this feedback to a database or send it via email
    st.success("Thank you for your feedback! We appreciate your input.")

# Footer
st.markdown("---")
st.write("Created for AECOM Quiz Night")
