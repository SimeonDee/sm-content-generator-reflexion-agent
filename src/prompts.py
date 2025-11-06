from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from textwrap import dedent
from datetime import datetime


actor_agent_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=dedent(
                """
                You are an expert AI Researcher. Your task is to perform 
                actions based on user requests.
                current time: {time}.
                
                1. {first_instruction}
                2. Reflect and critique your answer. Be severe to
                maximize improvement.
                3. After the reflection, **list 1-3 search queries
                separately** for research improvement. Do not include
                them inside the reflection.
            """
            )
        ),
        MessagesPlaceholder(variable_name="messages"),
        SystemMessage(
            content="Answer the user's question above using the required \
                format."
        ),
    ]
).partial(time=datetime.now().isoformat())

initial_responder_prompt_template = actor_agent_prompt_template.partial(
    first_instruction="Provide a detailed and accurate response to the "
    "user's query.",
)

revisor_prompt_template = actor_agent_prompt_template.partial(
    first_instruction=(
        "Revise and improve the previous response based on the reflection "
        "and conduct additional research using the provided search queries."
        "to improve response."
        "Provide citations for any new information added."
    )
)
