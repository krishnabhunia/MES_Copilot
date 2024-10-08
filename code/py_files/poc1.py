from langchain_core.prompts import PromptTemplate

print("Prompting the user to tell a joke about a topic")
topic = "cats"
prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
print(prompt_template)

prompt_template.invoke({"topic": "cats"})
print("User propmted templet invoked")
