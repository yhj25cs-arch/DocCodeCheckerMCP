import pytest
from core.code_tokenizer import extract_code_tokens

def test_extract_code_tokens_invalid_code():
    invalid_code = "def broken("

    with pytest.raises(SyntaxError):
        extract_code_tokens(invalid_code)