from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])
chat_history = []
with open('chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())

prompts = chat_template.invoke({
    'chat_history': chat_history,
    'query':'Where is my refund?'
})

print(prompts)