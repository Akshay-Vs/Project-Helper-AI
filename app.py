import sys
import time
import os
import streamlit as st
import concurrent.futures
from random import randint

st.markdown("<h1 style='text-align: center; color: white;'>Generate intresting stories with GPT</h1>", unsafe_allow_html=True)
st.markdown('')
st.markdown('')

# initializing session_state
#os.system('pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu')
#os.system('pip install transformers')

#from transformers import pipeline, set_seed

#generator = pipeline('text-generation', model='openai-gpt')

def generate(initial_text, length=50, return_sequences=1): pass
    #set_seed(randint(1,1000))
    #result = generator(initial_text, max_length = length, num_return_sequences = return_sequences)
    #return result[0]["generated_text"]

def slice(text, mak_length=10):
    return text[-mak_length:]

def type_text(text):
    for letter in text:
        sys.stdout.write(letter)
        time.sleep(0)

#text = input("Enter something to begin with... ")
#print(".\n.\n.\nGenerating\n.\n.\n.")

text = st.text_input('Enter something to begin with...', placeholder='I looked at her eyes, then i realized...', key="value")
if text:
    st.write("Generating...")
    for _ in range(10):
        #result = generate(text)
        #out = result.replace(text,"")
        
        st.markdown(f"<h3><b>I looked at her eyes,  then i realized</b></h3>", unsafe_allow_html=True)
        #with concurrent.futures.ThreadPoolExecutor() as executor:
        #   executor.submit(type_text, result.replace(text,""))
    st.balloons()

