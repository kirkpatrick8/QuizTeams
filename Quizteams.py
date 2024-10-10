import streamlit as st
import pandas as pd

# Define the data
data = [
    ["Davey, Michael", 1, "Finding Nemo"],
    ["Morris, Jonathan", 1, "Finding Nemo"],
    ["O Connor, Adrian", 1, "Finding Nemo"],
    ["OCallaghan, Lissa", 1, "Finding Nemo"],
    ["Pollock, Karen", 1, "Finding Nemo"],
    ["Shaw, Peter (Belfast)", 1, "Finding Nemo"],
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
    ["Sam McManus", 5, "Pipe Pipers"],
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
    name = name.lower()
    for index, row in df.iterrows():
        if name in row['Name'].lower():
            return row
    return None

# Streamlit app
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
        st.success(f"You are on Team {team_number}: {team_name}")
        
        # Display team members
        st.subheader("Your Team Members:")
        team_members = df[df["Team"] == team_number]["Name"].tolist()
        for member in team_members:
            st.write(f"- {member}")
    else:
        st.error("Name not found. Please check the spelling and try again.")
        st.write("Tip: You can enter just part of your name, like your first name or last name.")

# Display the full team list
if st.checkbox("Show full team list"):
    st.dataframe(df)

# Add a footer
st.markdown("---")
st.markdown("Created for AECOM Quiz Night")
