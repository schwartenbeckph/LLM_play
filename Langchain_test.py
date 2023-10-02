# frontend
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# title
st.title('🦜🔗 Quickstart App')

# Create a function to generate AI-generated content
def generate_response(input_text):
    # Load the pre-trained GPT-3.5 model and tokenizer
    model_name = "EleutherAI/gpt-neo-1.3B"  # You can change the model as needed
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Generate text based on the input prompt
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)

    # Decode and display the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    st.info(generated_text)

# st.form() to create a text box (st.text_area()) accepting user-provided prompt input
# Once the user clicks the Submit button, the generate-response() function is called with the prompt input variable (text) as an argument
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
