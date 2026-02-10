import pytest
from core.comparer import compare_keywords

def test_compare_keywords_invalid_input_none():
    spec = None
    code = ["GET /users"]

    with pytest.raises(TypeError):
        compare_keywords(spec, code)