import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

modelset_response = model = ChatGroq(model="llama3-8b-8192")
print(f"Model set response = {modelset_response}")

prompt_to_chatbot = "Hi! I'm Bob"
response = model.invoke([HumanMessage(content=prompt_to_chatbot)])
print(f"Response is = {response}")
model.invoke([HumanMessage(content="What's my name?")])
print(f"Response is = {response}")

model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)
