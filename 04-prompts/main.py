from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)

messages = [
    SystemMessage(content="You are a helpful Python tutor."),
    HumanMessage(content="Explain Python decorators simply.")
]


prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language with an example."
)

formatted_prompt = prompt.format(topic="Machine Learning")

print(formatted_prompt)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {subject} tutor."),
    ("human", "Explain {topic} with a practical example.")
])

messages = prompt.format_messages(
    subject="Python",
    topic="Decorators"
)

# response = model.invoke(messages)
# print(response.content)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Respond in a {style} style."),
    ("human", "{question}")
])

messages = prompt.format_messages(
    role="software engineer",
    style="beginner-friendly",
    question="Explain REST APIs."
)

# response = model.invoke(messages)
# print(response.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "Classify the sentiment as positive or negative."),
    ("human", "This product is amazing."),
    ("ai", "Positive"),
    ("human", "The service was terrible."),
    ("ai", "Negative"),
    ("human", "{review}")
])

messages = prompt.format_messages(
    review="I really enjoyed using this application."
)

response = model.invoke(messages)
print(response.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    Answer the question using only the provided context.

    Context:
    {context}
    """),
    ("human", "{question}")
])

messages = prompt.format_messages(
    context="FastAPI is a Python framework for building APIs.",
    question="What is FastAPI?"
)

response = model.invoke(messages)
print(response.content)
