

## 🗿 LLM 모듈형 인스트럭션 프로젝트 구조

이 프로젝트의 핵심은 \*\*모듈(instructions)\*\*과 이를 지능적으로 \*\*조합하는 엔진(engine)\*\*입니다.

### 📁 디렉토리 구조 (Directory Structure)

```
prompt-assembler/
├── instructions/               # 📜 모든 인스트럭션 .md 파일 저장소
│   ├── lang_python/            # 언어: 파이썬 관련
│   │   ├── style_pep8.md
│   │   ├── style_google.md
│   │   ├── rule_security_basic.md
│   │   └── rule_docstring_numpy.md
│   │
│   ├── lang_javascript/        # 언어: 자바스크립트 관련
│   │   ├── style_prettier.md
│   │   └── rule_es6_features.md
│   │
│   ├── lib_pandas/             # 라이브러리: Pandas 관련
│   │   ├── rule_performance.md
│   │   └── rule_best_practice.md
│   │
│   └── general/                #  범용 규칙
│       ├── tone_formal.md
│       └── output_format_json.md
│
├── engine/                     # ⚙️ 프롬프트 조합을 담당하는 핵심 로직
│   ├── __init__.py
│   ├── combiner.py             # .md 파일들을 읽고 조합하는 로직
│   └── templates.py            # 프롬프트 템플릿 관리 (헤더, 푸터 등)
│
├── presets/                    # 📚 자주 사용하는 조합을 미리 정의한 파일
│   ├── python_default.json     # 예: ["lang_python/style_pep8", "lang_python/rule_security_basic"]
│   └── data_analysis_pandas.json
│
├── main.py                     # 💻 사용자가 실행하는 메인 스크립트 (CLI)
├── config.yaml                 # 🔧 프로젝트 설정 파일 (모듈 경로 등)
├── examples/                   # 💡 사용 예시 스크립트 또는 결과물
│   └── create_pandas_function.sh
└── README.md                   # 📖 프로젝트 설명서
```

-----

### 📝 각 구성 요소 설명

#### 1\. `instructions/`

  - **목적**: 재사용 가능한 모든 지시사항(규칙) 조각들을 마크다운(`.md`) 파일로 저장합니다.
  - **특징**:
      - **계층적 분류**: `언어/라이브러리/주제` 등으로 폴더를 나누어 관리의 용이성을 높입니다.
      - **네이밍 규칙**: `[분류]_[주제]_[세부].md` (예: `lang_python_rule_security_basic.md`) 와 같이 명확한 파일명을 사용해 어떤 규칙인지 쉽게 알 수 있도록 합니다.

#### 2\. `engine/`

  - **목적**: 실제 프롬프트 조합이 일어나는 핵심 부분입니다.
  - `combiner.py`:
      - 사용자로부터 키워드 리스트(예: `['lang_python/style_pep8', 'lib_pandas/rule_performance']`)를 입력받습니다.
      - `instructions` 디렉토리에서 해당 파일들을 찾아 순서대로 내용을 읽어옵니다.
      - 읽어온 내용들을 하나의 텍스트로 합쳐 최종 프롬프트를 생성하는 함수를 포함합니다.
  - `templates.py`:
      - 모든 프롬프트의 시작과 끝에 붙을 상용구(boilerplate)를 관리합니다.
      - 예시:
          - **Header Template**: "You are a helpful AI assistant. Follow all the rules below to complete the user's request. The user's primary task is: `{{TASK}}`"
          - **Section Template**: "\#\#\# Rule: `{{MODULE_NAME}}`\\n`{{MODULE_CONTENT}}`"

#### 3\. `presets/`

  - **목적**: 자주 사용하는 인스트럭션 조합을 미리 정의해두어, 매번 긴 명령어를 입력할 필요 없이 간단히 불러올 수 있게 합니다.
  - **형식**: JSON 또는 YAML 파일로 모듈 이름의 리스트를 저장합니다.
  - **예시** (`python_default.json`): `["lang_python/style_pep8", "lang_python/rule_security_basic", "general/tone_formal"]`

#### 4\. `main.py`

  - **목적**: 사용자와 상호작용하는 진입점(Entry Point)입니다. **CLI (Command-Line Interface)** 로 구현하는 것이 가장 직관적입니다.
  - **기능**:
      - 명령어 인자(arguments)를 파싱합니다. (예: `python main.py --task "데이터프레임 처리 함수 만들어줘" --modules lang_python/style_pep8 lib_pandas/rule_performance`)
      - 또는 프리셋을 사용합니다. (예: `python main.py --task "..." --preset python_default`)
      - 파싱된 정보를 `engine/combiner.py`에 전달하여 최종 프롬프트를 생성합니다.
      - 생성된 프롬프트를 터미널에 출력하거나, 클립보드에 복사합니다.

-----

### 🚀 개발 로드맵 (단계별 접근)

#### **1단계: 기본 CLI 도구 구현**

1.  `instructions` 폴더 구조와 샘플 `.md` 파일 몇 개를 만듭니다.
2.  `engine/combiner.py`에 특정 경로의 파일들을 읽어 단순히 텍스트로 합치는 기본 함수를 구현합니다.
3.  `main.py`에서 `argparse` 같은 라이브러리를 사용해 `--modules` 인자로 파일 경로를 직접 받아 조합하고, 결과를 `print()` 하는 기능을 만듭니다.

#### **2단계: 템플릿과 프리셋 기능 추가**

1.  `engine/templates.py`를 만들어 프롬프트에 헤더와 섹션 구분을 추가합니다.
2.  `main.py`에 `--preset` 옵션을 추가하고, `presets` 폴더의 `.json` 파일을 읽어 모듈 목록을 불러오는 기능을 구현합니다.
3.  사용자의 `--task` 내용을 프롬프트 헤더의 `{{TASK}}` 변수에 삽입하는 로직을 추가합니다.

#### **3단계: LLM을 이용한 자동 조합 (고급)**

1.  사용자의 자연어 요청(예: "보안과 성능을 고려한 판다스 코드 짜줘")을 분석할 **'에이전트'** 개념을 도입합니다.
2.  `main.py`에 `--auto` 와 같은 플래그를 추가합니다.
3.  이 플래그가 활성화되면, `instructions` 디렉토리의 파일명과 내용을 기반으로 LLM에게 "이 요청에 가장 적합한 모듈은 무엇이니?"라고 질문합니다.
4.  LLM이 추천해준 모듈 리스트를 받아, 1, 2단계에서 만든 조합기 엔진을 통해 최종 프롬프트를 생성합니다.

이 구조를 따르면, 처음에는 간단한 수동 조합 도구로 시작하여 점차적으로 지능적이고 자동화된 '프롬프트 엔지니어링 시스템'으로 발전시킬 수 있습니다.