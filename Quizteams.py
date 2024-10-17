import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random
from github import Github
import io

# GitHub repository details
GITHUB_TOKEN = st.secrets["QUIZ_SECRET"]
REPO_NAME = "kirkpatrick8/QuizTeams"  # Updated to match your actual repository name
BRANCH_NAME = "main"
FILE_PATH = "team_assignments.csv"

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Function to load existing team assignments
@st.cache_data(ttl=60)  # Cache for 60 seconds
def load_team_data():
    try:
        content = repo.get_contents(FILE_PATH, ref=BRANCH_NAME)
        df = pd.read_csv(io.StringIO(content.decoded_content.decode()))
        st.sidebar.write(f"Loaded {len(df)} team assignments")
        return df
    except Exception as e:
        st.sidebar.error(f"Error loading team data: {e}")
        return pd.DataFrame(columns=["Name", "Team", "Team Name"])

# Function to save new team assignment
def save_team_assignment(new_assignment):
    try:
        df = load_team_data()
        df = pd.concat([df, pd.DataFrame([new_assignment])], ignore_index=True)
        
        # Convert DataFrame to CSV string
        csv_string = df.to_csv(index=False)
        
        # Update the file in the repository
        contents = repo.get_contents(FILE_PATH, ref=BRANCH_NAME)
        repo.update_file(FILE_PATH, f"Update team assignments - {datetime.now()}", csv_string, contents.sha, branch=BRANCH_NAME)
        
        st.sidebar.success("Saved team assignment successfully")
        # Clear the cache to force a reload of the data
        load_team_data.clear()
    except Exception as e:
        st.sidebar.error(f"Error saving team assignment: {e}")

# Function to search for a name
def search_name(name, df):
    name_parts = name.lower().split()
    return df[df['Name'].apply(lambda x: all(part in x.lower() for part in name_parts))]

# Function to assign to a random team
def assign_random_team(name, df):
    teams = df['Team'].unique()
    team_sizes = df['Team'].value_counts()
    smallest_teams = team_sizes[team_sizes == team_sizes.min()].index
    assigned_team = random.choice(smallest_teams)
    team_name = df[df['Team'] == assigned_team]['Team Name'].iloc[0]
    return {"Name": name, "Team": assigned_team, "Team Name": team_name}

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

# Load existing team data
df = load_team_data()

# Name search functionality
name = st.text_input("Enter your name:")

if name:
    results = search_name(name, df)
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
        new_assignment = assign_random_team(name, df)
        save_team_assignment(new_assignment)
        st.success(f"You have been assigned to Team {new_assignment['Team']}: {new_assignment['Team Name']}")
        
        # Reload the data to include the new assignment
        df = load_team_data()
        
        # Display team members
        st.subheader("Your Team Members:")
        team_members = df[df["Team"] == new_assignment['Team']]["Name"].tolist()
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

# Add a download button for the team assignments
csv = df.to_csv(index=False)
st.download_button(
    label="Download Team Assignments CSV",
    data=csv,
    file_name='team_assignments.csv',
    mime='text/csv'
)
