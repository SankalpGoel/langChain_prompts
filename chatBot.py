from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "moonshotai/Kimi-K2-Instruct-0905",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat...")
        break   
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("Bot:", result.content)

print(chat_history)