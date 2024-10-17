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

# Function to assign to a random team
def assign_random_team(name):
    teams = df['Team'].unique()
    team_sizes = df['Team'].value_counts()
    smallest_teams = team_sizes[team_sizes == team_sizes.min()].index
    assigned_team = random.choice(smallest_teams)
    new_row = pd.DataFrame([[name, assigned_team, df[df['Team'] == assigned_team]['Team Name'].iloc[0]]], 
                           columns=["Name", "Team", "Team Name"])
    return pd.concat([df, new_row], ignore_index=True)

# Set up the Streamlit page
st.set_page_config(page_title="AECOM Quiz Team Finder", page_icon="🔍", layout="wide")

# Random fun facts
fun_facts = [
    "AECOM has been recognized as one of the World's Most Ethical Companies.",
    "The average person uses 80-100 gallons of water per day.",
    "AECOM has worked on projects in more than 150 countries.",
    "Only 3% of the Earth's water is freshwater.",
    "AECOM was founded in 1990.",
]

# Display random fact at the start
st.info(f"Did You Know? {random.choice(fun_facts)}")

# Welcome message and instructions
st.title("Welcome to AECOM Quiz Team Finder! 🎉")
st.markdown("""
This app helps you find your team for the upcoming AECOM Quiz Night. Here's how to use it:
1. Enter your name in the search box below
2. View your team information and teammates
3. If you didn't sign up on time, you'll be assigned to a random team
""")

# Countdown timer
quiz_date = datetime(2023, 10, 17, 17, 30)  # Adjust to your actual quiz date and time
now = datetime.now()
time_left = quiz_date - now

st.sidebar.header("Quiz Countdown")
st.sidebar.write(f"Days: {time_left.days}")
st.sidebar.write(f"Hours: {time_left.seconds // 3600}")
st.sidebar.write(f"Minutes: {(time_left.seconds % 3600) // 60}")

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
        st.warning("Name not found. Assigning you to a random team...")
        df = assign_random_team(name)
        new_team = df[df['Name'] == name].iloc[0]
        st.success(f"You have been assigned to Team {new_team['Team']}: {new_team['Team Name']}")
        
        # Display team members
        st.subheader("Your Team Members:")
        team_members = df[df["Team"] == new_team['Team']]["Name"].tolist()
        for member in team_members:
            st.write(f"- {member}")

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

# Footer
st.markdown("---")
st.write("Created for AECOM Quiz Night")
