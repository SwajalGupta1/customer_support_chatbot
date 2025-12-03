import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import customer_support_chatbot.backend.rag_pipeline


st.set_page_config(page_title="Customer Support Chatbot", layout="wide")
st.title("🛍️ Customer Support Chatbot (Flipkart-Style)")

if("messages" not in st.session_state):
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your question")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response= answer_question(user_input)
        bot_reply = response['answer']
        st.write(bot_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.expander("Sources"):
        for doc in response['sources']:
            st.markdown(f"**Category:** {doc['category']}")
            st.markdown(f"**Q:** {doc['question']}")
            st.markdown(f"**A:** {doc['answer']}")
            st.markdown("---")