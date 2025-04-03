import streamlit as st

# Streamlit App Title
st.title("Calculator App for students")

# User Input
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Operation Selection
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."

    st.write(f"Result: {result}")
