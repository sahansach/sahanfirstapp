pip install -r requirements.txt

import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Create a text input for the user to enter a prompt
prompt = st.text_input('Enter a prompt for the GPT-3 model')

# When the user enters a prompt and hits Enter, call the OpenAI API
if prompt:
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)

    # Display the model's response
    st.write(response.choices[0].text.strip())
