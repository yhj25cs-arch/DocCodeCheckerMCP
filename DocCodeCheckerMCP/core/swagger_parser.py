# WHY:
# Swagger(OpenAPI) 명세와 실제 코드 구현 간 불일치를 비교하기 위해
# API 명세에서 "비교 기준이 되는 키워드"를 추출한다.

# INPUT / OUTPUT:
# - input: swagger (dict) → OpenAPI JSON을 파싱한 Python dict
# - output: list[str] → "METHOD /path", parameter name 목록

# EDGE CASE:
# - paths가 없는 경우 빈 리스트 반환
# - parameters가 없는 endpoint는 method/path만 추출

def extract_spec_keywords(swagger: dict) -> list[str]:
    keywords = set()

    paths = swagger.get("paths", {})
    for path, methods in paths.items():
        for method, detail in methods.items():
            keywords.add(f"{method.upper()} {path}")

            for param in detail.get("parameters", []):
                name = param.get("name")
                if name:
                    keywords.add(name)

    return sorted(keywords)