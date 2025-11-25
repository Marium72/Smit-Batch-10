import streamlit as st

print("MARIUM ALI")
print(50)
print(56.879)
print(True)
print(False)

print(type("ALI"))
print(type(67))
print(type(74.08))
print(type(False))

name = "Khadija"
print(name)
try:
    with open("greetings.txt", "r") as file:
        print(file.read())      
        file.seek(0)
        print(file.readlines(2))
except FileNotFoundError:
    print("File 'greetings.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

st.write("# Hello world")
