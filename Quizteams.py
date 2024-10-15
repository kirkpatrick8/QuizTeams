import streamlit as st
import pandas as pd

# Define the data
data = [
    ["Davey, Michael", 1, "Finding Nemo"],
    ["Morris, Jonathan", 1, "Finding Nemo"],
    ["O Connor, Adrian", 1, "Finding Nemo"],
    ["OCallaghan, Lissa", 1, "Finding Nemo"],
    ["Pollock, Karen", 1, "Finding Nemo"],
    ["Sanders, Adam", 1, "Finding Nemo"],
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
    ["Joanne Titterington", 13, "The Pressure Pros"]
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["Name", "Team", "Team Name"])

# Function to search for a name
def search_name(name):
    name_parts = name.lower().split()
    for index, row in df.iterrows():
        full_name = row['Name'].lower()
        if all(part in full_name for part in name_parts):
            return row
    return None

# Streamlit app
st.set_page_config(page_title="AECOM Quiz Team Finder", page_icon="🔍", layout="wide")

st.title("AECOM Quiz Team Finder")

# Add information about random team generation and contact person
st.info("Note: Teams were generated randomly. For any queries, please contact Mark Kirkpatrick.")

# Input field for the name
name = st.text_input("Enter your name:")

if name:
    result = search_name(name)
    
    if result is not None:
        team_number = result['Team']
        team_name = result['Team Name']
        
        # Display team information
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

# Display the full team list
if st.checkbox("Show full team list"):
    st.dataframe(df)

# Add team statistics
if st.checkbox("Show team statistics"):
    st.subheader("Team Statistics")
    total_participants = len(df)
    total_teams = df['Team'].nunique()
    st.write(f"Total number of participants: {total_participants}")
    st.write(f"Number of teams: {total_teams}")
    st.write("Participants per team:")
    team_sizes = df['Team'].value_counts().sort_index()
    st.bar_chart(team_sizes)

# Add a search feature for team names
st.subheader("Search for a Team")
team_search = st.text_input("Enter a team name:")
if team_search:
    matching_teams = df[df['Team Name'].str.contains(team_search, case=False)]
    if not matching_teams.empty:
        st.write("Matching teams:")
        st.dataframe(matching_teams)
    else:
        st.write("No matching teams found.")

# Add a footer
st.markdown("---")
st.write("Created for AECOM Quiz Night")
