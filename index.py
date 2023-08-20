import streamlit as st

def main():
    st.title("Simple Streamlit Application")
    st.write("Hello, Streamlit!")

    # Add some interactivity
    user_input = st.text_input("Enter your name:")
    st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()
