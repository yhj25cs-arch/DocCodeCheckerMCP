import ast

# WHY:
# 실제 서버 코드에서 함수명과 변수명을 추출하여
# Swagger 명세와 비교 가능한 코드 토큰 집합을 만들기 위함이다.

# INPUT / OUTPUT:
# - input: code (str) → Python 코드 전체 문자열
# - output: list[str] → 함수명, 변수명 토큰 목록

def extract_code_tokens(code: str) -> list[str]:
    if not isinstance(code, str):
        raise TypeError("code must be a string")

    try:
        tree = ast.parse(code)
    except SyntaxError:
        raise

    tokens = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            tokens.add(node.name)
        elif isinstance(node, ast.Name):
            tokens.add(node.id)

    return sorted(tokens)