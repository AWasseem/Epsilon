
import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from tensorflow.keras.layers import *
import numpy as np
import ast
import pandas as pd
import os
import json

def LoadModel():
    # Path to your saved model
    model_path = "full_model.keras"#"/kaggle/input/full-model/tensorflow2/default/1/sql_seq2seq_model/full_model.keras"
    model_path = "full_model.keras"
    # Check if the model file exists
    if os.path.exists(model_path):
        print("Model found — loading existing model...")
        model = tf.keras.models.load_model(model_path)
        return model
    else:
        print("Model not found — you may need to train and save it first.")
        return None

def load_vectorizer(name):
    with open(f"{name}_vocab.txt") as f:
        vocab = f.read().splitlines()
    with open(f"{name}_config.json") as f:
        config = json.load(f)
    vectorizer = TextVectorization.from_config(config)
    vectorizer.set_vocabulary(vocab)
    print(f"Loaded {name}")
    return vectorizer


model = LoadModel()
#loac text vectorizers

# Load Q_vectorizer
Q_vectorizer= load_vectorizer("Q_vectorizer")

# Load Sql_vectorizer
Sql_vectorizer= load_vectorizer("Sql_vectorizer")

#Encoder layers
encoder_inputs = model.input[0]
encoder_outputs, state_h_enc, state_c_enc = model.layers[4].output  # LSTM layer index may differ
encoder_states = [state_h_enc, state_c_enc]
encoder_model = tf.keras.Model(inputs =encoder_inputs,outputs= encoder_states)
encoder_model.summary()

#decoder layers
rnn_units =50
latent_dim = rnn_units

# Decoder  from encoder states
decoder_state_input_h = tf.keras.Input(shape=(latent_dim,))
decoder_state_input_c = tf.keras.Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

# Get embedding and LSTM layers from the trained model
dec_emb_layer = model.layers[3]  # decoder embedding
decoder_lstm = model.layers[5]   # decoder LSTM
decoder_dense = model.layers[6]  # final dense layer

# Use them to define step-by-step decoding
dec_inputs = model.input[1]  # decoder input placeholder
dec_emb2 = dec_emb_layer(dec_inputs)
dec_outputs, state_h_dec, state_c_dec = decoder_lstm(dec_emb2, initial_state=decoder_states_inputs)
dec_states = [state_h_dec, state_c_dec]
dec_outputs = decoder_dense(dec_outputs)

decoder_model = tf.keras.Model(
    inputs =[dec_inputs] + decoder_states_inputs,
    outputs=[dec_outputs] + dec_states
)
decoder_model.summary()



def decode_sequence(input_seq, max_len=50):
    # Encode the question
    states_value = encoder_model.predict(input_seq)

    # Create start token
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = Sql_vectorizer(['<start>']).numpy()[0][0]

    stop_condition = False
    decoded_sentence = []

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        # Get most probable token


        #(batch_size, sequence_length, vocab_size)
        #Part	Meaning
        #0	Take the first (and only) example in the batch (since batch size = 1 during inference).
        #-1	Take the last time step in the sequence (the most recent predicted token).
        #:	Take all vocabulary probabilities for that token (a vector of length vocab_size).
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_word = Sql_vectorizer.get_vocabulary()[sampled_token_index]
        decoded_sentence.append(sampled_word)

        # Stop if end token or max length
        if (sampled_word == '<end>' or len(decoded_sentence) > max_len):
            stop_condition = True

        # Update target sequence for next step
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update states
        states_value = [h, c]

    return ' '.join(decoded_sentence[:-1])  # remove <end>


st.set_page_config(layout= 'wide', page_title= 'Question to SQL Query Generator')
html_title = "<h1 style=color:white;text-align:center;> Question to SQL Query Generator </h1>"
st.markdown(html_title, unsafe_allow_html=True)

df = pd.read_csv('train.csv')
df.dropna(inplace=True)
st.dataframe(df.head(20))


user_question = st.text_input("Enter your question:")
if st.button("Generate SQL Query"):
    input_seq = Q_vectorizer([user_question])
    sql_query = decode_sequence(input_seq)
    st.write("Generated SQL Query:")
    st.code(sql_query)

