from fastapi import FastAPI
from core.swagger_parser import extract_spec_keywords
from core.code_tokenizer import extract_code_tokens
from core.comparer import compare_keywords

app = FastAPI(title="DocCodeChecker MCP (HTTP)")

@app.post("/compare")
def compare(spec: dict, code: str):
    spec_keywords = extract_spec_keywords(spec)
    code_keywords = extract_code_tokens(code)

    return compare_keywords(spec_keywords, code_keywords)