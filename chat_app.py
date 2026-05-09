import streamlit as st
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="ChatGPT Style App",
    page_icon="💬",
    layout="centered"
)

# App title
st.title("💬 Dalia' Chat application")
st.markdown("This app simulates a chatbot.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Local response generator function
def generate_response(user_message):

    message = user_message.lower()

    greetings = [
        "Hello! How can I help you today?",
        "Hi there!",
        "Hey! Nice to chat with you."
    ]

    default_responses = [
        "Interesting! Tell me more.",
        "I understand.",
        "That's cool!",
        "Can you explain further?",
        "I'm responding locally using Python logic.",
        "This is a mock AI response generated without external APIs."
    ]

    # Rule-based responses
    if "hello" in message or "hi" in message:
        return random.choice(greetings)

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "your name" in message:
        return "I'm a simple local chatbot built with Streamlit."

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif "date" in message:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}"

    elif "bye" in message:
        return "Goodbye! Have a great day."

    elif "python" in message:
        return "Python is a powerful programming language."

    elif "streamlit" in message:
        return "Streamlit helps build web apps easily using Python."

    else:
        return random.choice(default_responses)


# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Optional timestamp
        if "time" in message:
            st.caption(message["time"])


# User input
user_input = st.chat_input("Type your message here...")

# Handle user input
if user_input:

    current_time = datetime.now().strftime("%H:%M:%S")

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(current_time)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = generate_response(user_input)

        st.markdown(response)
        st.caption(current_time)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": current_time
    })