from pydantic import BaseModel, Field
from typing import List


class Reflection(BaseModel):
    missing: str = Field(
        ...,
        description="What important information is missing from "
        "the current response?",
    )
    superfluous: str = Field(
        ...,
        description="What information is unnecessary or redundant "
        "in the current response?",
    )
    misleading: str = Field(
        ...,
        description="What information in the current response could "
        "lead to misunderstanding or confusion?",
    )


class QuestionResponse(BaseModel):
    response: str = Field(
        description="The detailed and accurate response to the user's query."
    )
    reflection: Reflection = Field(
        description="A severe reflection and critique of the "
        "answer to maximize improvement.",
    )
    search_queries: List[str] = Field(
        description="A list of 1-3 search queries for research improvement."
    )


class RevisedResponse(QuestionResponse):
    """The improved response after considering the reflection
    and conducting additional research."""

    citations: List[str] = Field(
        description="A list of citations or references used to "
        "improve the response.",
    )
