from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
socketio = SocketIO(app)

# Cargar el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained("gpt2-large")
model = AutoModelForCausalLM.from_pretrained("gpt2-large")

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    # Ajustes de generación
    output = model.generate(
        input_ids, 
        max_length=100, 
        num_return_sequences=1, 
        temperature=0.7, 
        top_k=50, 
        top_p=0.95,
        no_repeat_ngram_size=2
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('send_message')
def handle_send_message_event(data):
    user_input = data['message']
    response = generate_response(user_input)
    emit('receive_message', {'message': response}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
