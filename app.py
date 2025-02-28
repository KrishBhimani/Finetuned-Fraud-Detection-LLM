import os
import streamlit as st
from lamini import Lamini
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

lamini_api_key = os.getenv('LAMINI_API_KEY')
model_id = os.getenv('MODEL_ID')

lamini_client = Lamini(api_key=lamini_api_key, model_name=model_id)

groq_llm = ChatGroq(model_name="qwen-2.5-32b")

# Function to get fraud prediction from Lamini
def query_model(prompt):
    response = lamini_client.generate(prompt=prompt)
    cleaned_response = response.strip().split("\n")[0]  # Take only the first relevant line
    return cleaned_response
    

# Function to generate explanation using Groq LLM
def generate_explanation(transaction_details, prediction):
    explanation_prompt = f"""
    Transaction Details: {transaction_details}
    Prediction: {prediction}

    Explain why this transaction is classified as {prediction}.
    Provide a clear, logical explanation considering transaction patterns, risk factors, and fraud detection insights.
    """
    
    messages = [
        SystemMessage(content="You are an AI fraud analyst."),
        HumanMessage(content=explanation_prompt)
    ]

    response = groq_llm.invoke(messages)
    return response.content.strip()

# Streamlit UI
st.title("💳 FineTuned Fraud Detection Model using Lamini")
st.subheader("Analyze transactions for fraud risk")

# User Input
user_input = st.text_area("Enter transaction details:")

if st.button("Analyze"):
    if user_input:
        with st.spinner("Analyzing..."):
            prediction = query_model(user_input)
            explanation = generate_explanation(user_input, prediction)

        st.success("Analysis Complete")
        st.write("**Prediction:**", prediction)
        st.write("**Explanation:**", explanation)
    else:
        st.warning("⚠️ Please enter transaction details!")
