import pytest
from core.swagger_parser import extract_spec_keywords

def test_extract_spec_keywords_empty_paths():
    swagger = {}

    result = extract_spec_keywords(swagger)

    assert result == []