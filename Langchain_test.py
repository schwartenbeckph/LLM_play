# frontend
import streamlit as st
from langchain.llms import OpenAI

# title
st.title('🦜🔗 Quickstart App')


openai_api_key = st.sidebar.text_input('OpenAI API Key')

# OpenAI() method to generate AI-generated content
# Display text output inside a box using st.info()
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))


# st.form() to create text box (st.text_area()) accepting user-provided prompt input
# Once user clicks Submit button, generate-response() function is called with prompt input variable (text) as argument
with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)