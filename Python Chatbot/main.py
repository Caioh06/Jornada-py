# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

import streamlit as st
import google.generativeai as genai 

google_api_key = "AIzaSyDN6ypJcsgWeXhlp0NWIzc-ELwFtNZOB1Q"
genai.configure(api_key= google_api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

st.write("# Chatbot com IA")

# Inicializa o histórico no session_state se não existir
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe as mensagens anteriores
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    # Exibe e salva a mensagem do usuário
    st.chat_message("user").write(texto_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})

    
    historico_gemini = []
    for msg in st.session_state["lista_mensagens"]:
        role_gemini = "user" if msg["role"] == "user" else "model"
        historico_gemini.append({
            "role": role_gemini,
            "parts": [msg["content"]]
        })

    # Inicia o chat com o histórico carregado e envia a nova mensagem
    
    chat = model.start_chat(history=historico_gemini[:-1]) 
    
    with st.spinner("Gemini está pensando..."):
        response = chat.send_message(texto_usuario)
        texto_resposta_ia = response.text

    # 4. Exibe e salva a resposta da IA
    st.chat_message("assistant").write(texto_resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta_ia})
