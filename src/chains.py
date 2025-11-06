from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_openai import ChatOpenAI
from src.prompts import (
    initial_responder_prompt_template,
    revisor_prompt_template,
)
from src.schema import QuestionResponse, RevisedResponse
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

initial_output_parser = PydanticToolsParser(tools=[QuestionResponse])
revision_output_parser = PydanticToolsParser(tools=[RevisedResponse])

initial_responder_chain = (
    initial_responder_prompt_template
    | llm.bind_tools(tools=[QuestionResponse], tool_choice="QuestionResponse")
    | initial_output_parser
)

revisor_responder_chain = (
    revisor_prompt_template
    | llm.bind_tools(tools=[RevisedResponse], tool_choice="RevisedResponse")
    | revision_output_parser
)
