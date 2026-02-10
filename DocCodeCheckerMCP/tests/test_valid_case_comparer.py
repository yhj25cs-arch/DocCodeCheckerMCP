from core.comparer import compare_keywords

def test_compare_keywords():
    spec = ["GET /users", "POST /login"]
    code = ["GET /users"]

    result = compare_keywords(spec, code)

    assert "POST /login" in result["only_in_spec"]