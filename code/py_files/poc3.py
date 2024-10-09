from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
import datetime

# setup the tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def square(a: int) -> int:
    """Calculates the square of a number."""
    a = int(a)
    return a * a

@tool
def give_increment(a: int) -> float:
    """if the number is negative then make it postive number and then return the number * 1.25"""
    result = abs(a) * 1.25
    return result

@tool
def give_customise_increment(a: int, b: int) -> float:
    """if the number is negative then make it postive number and return the number * b/100"""
    result = abs(a) * b/100
    return result

@tool
def add_salution_to_name(name: str) -> str:
    """Modify then name with which starts with capital letter and prefix a salution before the name such as Mr. or Mrs.
    According to gender of the name, it will add Mr. or Mrs. before the name.
    If you unable to identify the name then return the name with Prefix 'Hello Dear'
    """

@tool
def extract_name_and_convert_to_numeric(name: str) -> str:
    """Extract the name from the given string and convert it to numeric value.
    numeric value is calculated as e.g a|A = 01 z|Z = 26
    e.g if the name is 'John' then the numeric value is 10081415
    """
    return "Unable to"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a mathematical assistant.
        Use your tools to answer questions. If you do not have a tool to
        answer the question, say so. 

        Return answer with description in a new line, e.g
        Human: What is 1 + 1?
        AI: Invoked Tool tool_name and the result is : 1 + 1 = 2
        """),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Choose the LLM that will drive the agent
# llm = ChatGroq(model="llama3-8b-8192", temperature=0.5)
llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.5)

# setup the toolkit
toolkit = [add, multiply, square, give_increment, give_customise_increment, add_salution_to_name]

# Construct the OpenAI Tools agent
agent = create_openai_tools_agent(llm, toolkit, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)
print(datetime.datetime.now())

print("-----------------")
result = agent_executor.invoke({"input": "what is 1 + 1?"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "how much to give on increment on -300 and 150"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "how much to give on increment on 1000 with 10%"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "my name is krishna bhunia and I need to address me properly"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "My friend name is priyanka and abhijit, what are its numeric value"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "My friend name is Alex, what are its numeric value"})
print(result['output'])
print("+++++++++++++++++")

print("-----------------")
result = agent_executor.invoke({"input": "My friend name is Alexa, what are its numeric value"})
print(result['output'])
print("+++++++++++++++++")