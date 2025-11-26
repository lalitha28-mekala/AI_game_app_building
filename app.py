import streamlit as st
import requests
import subprocess
import os
import json
import sys

st.title("GENERATE AI POWERED GAME OR APP")

options = st.multiselect("Select which application you want to develop!", ["Game", "APP"])
prompt = st.text_area("Describe about your selected application :")

# --- Generate Application ---
if st.button("Develop application"):
    if prompt:
        st.info("Generating application... please wait.")

        response = requests.post(
            url="https://lalithamekala.app.n8n.cloud/webhook/ebcc366f-213a-4ee4-82cc-7229413e2366",
            json={"prompt": prompt}
        )

        if response.status_code == 200:
            st.success("Code generated successfully!")

            # Extract generated code
            code = response.json().get("output", "")
            code = code.replace("```python", "").replace("```", "").strip()

            # Save as app1.py
            with open("app1.py", "w", encoding="utf-8") as file:
                file.write(code)

            st.code(code, language="python")
        else:
            st.error(f"Error generating code: {response.text}")
    else:
        st.error("Please enter a prompt first.")

# --- Run Application ---
if st.button("Run App"):
    if os.path.exists("app1.py"):
        st.write("Running application...")

        # Run the game/app in a separate process (so Streamlit doesn't freeze)
        try:
            if sys.platform.startswith("win"):
                subprocess.Popen(["python", "app1.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(["python3", "app1.py"])
            
            st.success("Application started! Check the new window.")
        except Exception as e:
            st.error(f"Error running app: {e}")
    else:
        st.error("No generated app found. Please click 'Develop application' first.")
