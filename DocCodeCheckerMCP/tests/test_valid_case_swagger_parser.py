from core.swagger_parser import extract_spec_keywords

def test_extract_spec_keywords():
    swagger = {
        "paths": {
            "/users": {
                "get": {
                    "parameters": [
                        {"name": "user_id"}
                    ]
                }
            }
        }
    }

    result = extract_spec_keywords(swagger)

    assert "GET /users" in result
    assert "user_id" in result
