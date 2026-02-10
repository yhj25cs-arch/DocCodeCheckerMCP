from core.code_tokenizer import extract_code_tokens

def test_extract_code_tokens_normal():
    code = """
def login(user):
    token = generate_token(user)
    return token
"""

    result = extract_code_tokens(code)

    assert "login" in result
    assert "user" in result
    assert "token" in result
    assert "generate_token" in result