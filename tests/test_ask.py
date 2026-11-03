from types import SimpleNamespace
from unittest.mock import patch

import app.ask as ask_module


def test_ask_prints_input_and_output_token_counts(capsys):
    response = SimpleNamespace(
        text="answer",
        usage_metadata=SimpleNamespace(prompt_token_count=11, response_token_count=7),
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )

    with patch("app.ask.get_api_key", return_value="test-key"), patch(
        "app.ask.genai.Client", return_value=client
    ):
        assert ask_module.ask("question") == "answer"

    assert "[tokens] input=11 output=7" in capsys.readouterr().out