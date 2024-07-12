import streamlit as st
import random

# Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Both chose the same: Match tie"
    
    if user_choice == "Rock":
        if comp_choice == "Paper":
            return "Paper covers Rock: You lose"
        else:
            return "Rock smashes Scissor: You win"
    
    if user_choice == "Scissor":
        if comp_choice == "Rock":
            return "Rock smashes Scissor: You lose"
        else:
            return "Scissor cuts Paper: You win"
    
    if user_choice == "Paper":
        if comp_choice == "Rock":
            return "Paper covers Rock: You win"
        else:
            return "Scissor cuts Paper: You lose"

# List of choices
choices = ["Rock", "Paper", "Scissor"]

# Streamlit app
st.title("Rock-Paper-Scissors Game")

# User input
user_choice = st.selectbox("Enter your move:", choices)

# Computer choice
comp_choice = random.choice(choices)

if st.button("Play"):
    st.write(f"User choice: {user_choice}")
    st.write(f"Computer choice: {comp_choice}")
    result = determine_winner(user_choice, comp_choice)
    st.write(result)
