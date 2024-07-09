import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Definir patrones y respuestas para el chatbot
patterns = [
    (r'¿Quién eres?', ['Soy un chatbot generativo.']),
    (r'¿Cómo estás?', ['Estoy bien, ¿y tú?']),
    (r'¿Cuál es tu nombre?', ['Mi nombre es ChatBot.']),
    (r'¿Qué puedes hacer\?', ['Puedo responder preguntas simples.']),
    (r'Adiós', ['Hasta luego!', 'Nos vemos!']),
]

# Reflejos para transformaciones
reflections = {
    'yo': 'tú',
    'tú': 'yo',
    'mi': 'tu',
    'tu': 'mi',
    'eres': 'soy',
    'soy': 'eres',
}

# Crear el chatbot
chatbot = Chat(patterns, reflections)

# Función para interactuar con el chatbot
def chat(user_input):
    response = chatbot.respond(user_input)
    return response

# Configurar la interfaz de Streamlit
def main():
    st.title("Chatbot Generativo con NLTK y Streamlit")
    st.markdown("¡Hola! Soy un chatbot generativo. Escribe tus preguntas o mensajes para comenzar.")

    user_input = st.text_input("Tú:")
    if user_input:
        response = chat(user_input)
        st.text_area("ChatBot:", value=response, height=100)

if __name__ == "__main__":
    main()
