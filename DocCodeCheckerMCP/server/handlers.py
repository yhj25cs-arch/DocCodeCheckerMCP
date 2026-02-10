from adapters.file_loader import load_json, load_text
from core.swagger_parser import extract_spec_keywords
from core.code_tokenizer import extract_code_tokens
from core.comparer import compare_keywords

def read_swagger_spec(file_path: str) -> dict:
    try:
        swagger = load_json(file_path)
        keywords = extract_spec_keywords(swagger)
        return {"ok": True, "spec_keywords": keywords}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def extract_code_tokens_handler(file_path: str) -> dict:
    try:
        code = load_text(file_path)
        tokens = extract_code_tokens(code)
        return {"ok": True, "code_tokens": tokens}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def compare_spec_and_code(spec_path: str, code_path: str) -> dict:
    try:
        swagger = load_json(spec_path)
        code = load_text(code_path)

        spec_keywords = extract_spec_keywords(swagger)
        code_tokens = extract_code_tokens(code)

        diff = compare_keywords(spec_keywords, code_tokens)
        return {"ok": True, "diff": diff}
    except Exception as e:
        return {"ok": False, "error": str(e)}