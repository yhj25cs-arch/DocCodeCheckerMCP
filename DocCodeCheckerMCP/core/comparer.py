# WHY:
# Swagger 명세와 코드 구현 사이의 차이를 명확히 드러내어
# 문서-코드 불일치를 빠르게 확인할 수 있도록 한다.

# INPUT / OUTPUT:
# - input:
#   - spec: Swagger에서 추출한 키워드 목록
#   - code: 코드에서 추출한 토큰 목록
# - output:
#   - dict {
#       only_in_spec: list[str],
#       only_in_code: list[str]
#     }

# EDGE CASE:
# - 한쪽 리스트가 비어 있어도 정상 동작
# - 완전히 동일한 경우 빈 리스트 2개 반환

def compare_keywords(spec: list[str], code: list[str]) -> dict:
    spec_set = set(spec)
    code_set = set(code)

    return {
        "only_in_spec": sorted(spec_set - code_set),
        "only_in_code": sorted(code_set - spec_set)
    }