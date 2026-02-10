# DocCodeCheckerMCP
# MCP는 로컬 환경에 있는 API 설명 파일(swagger.json)을 읽고 문서에 정의된 API 요소들을 추출한다. 서버를 만드는 파이썬 코드 파일을 읽고 코드 내부에 실제 사용된 단어(함수명, 변수명 등)를 각각 추출한다. 두 결과를 비교하여 서로 일치하지 않는 항목만 출력한다. 명세된 내용과 구현된 코드 간의 불일치를 빠르게 확인할 수 있도록 돕는다.
# Tool 1. read_swagger_spec: swagger.json 파일을 읽고 API 관련 키워드 목록 추출
# Tool 2. extract_code_tokens: 파이썬 코드 파일을 읽고 내부 단어(토큰) 목록 추출
# Tool 3. compare_spec_and_code: swagger 키워드와 코드 토큰을 비교하여 차이점만 반환
# 구조 
doccodechecker/
├─ server/
│  ├─ main.py          # MCP 엔트리 (stdio)
│  └─ handlers.py      # MCP tool handler (dict 반환)
│
├─ core/
│  ├─ swagger_parser.py
│  ├─ code_tokenizer.py
│  └─ comparer.py
│
├─ adapters/
│  └─ file_loader.py   # 파일 I/O (mock 대상)
│
├─ tests/
│  └─ test_swagger_parser.py
│
└─ schemas/
   ├─ read_swagger_spec.json
   ├─ extract_code_tokens.json
   └─ compare_spec_and_code.json
