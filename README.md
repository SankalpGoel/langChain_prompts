Basic langChain prompts
Prompts are the input instructions or queries given to a model to guide its output.

A PromptTemplate in LangChain is a structured way to create prompts
dynamically by inserting variables into a predefined template. Instead of
hardcoding prompts, PromptTemplate allows you to define placeholders that can
be filled in at runtime with different inputs.
This makes it reusable, flexible, and easy to manage, especially when working
with dynamic user inputs or automated workflows.

Why use PromptTemplate over f strings?
Default validation
Reusable
LangChain Ecosystem

A MessagesPlaceholder in LangChain is a special placeholder used inside a
ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.
