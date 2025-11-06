from src.chains import initial_responder_chain
from src.schema import QuestionResponse
from unittest import TestCase
import pytest


class TestInitialResponderChain(TestCase):
    def test_initial_responder_chain_structure(self):
        self.assertIsNotNone(initial_responder_chain)

    def test_initial_responder_chain_prompt(self):
        # Check that the prompt template contains the expected instructions
        prompts = initial_responder_chain.get_prompts()
        self.assertGreater(
            len(prompts), 0, "No prompts found in the initial responder chain."
        )

    @pytest.mark.skip(
        "Requires LLM response, implement with mocking if needed",
    )
    def test_initial_responder_chain_execution(self):
        # This is a placeholder test to ensure the chain can be executed
        # In a real scenario, you would mock the LLM response
        user_query = "What is the capital of France?"
        response = initial_responder_chain.invoke(
            {"messages": [{"role": "user", "content": user_query}]}
        )
        self.assertIsInstance(response[0], QuestionResponse)
        self.assertEqual(len(response), 1)
