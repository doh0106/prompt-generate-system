## [Docstring] reStructuredText (Sphinx) 스타일

모든 함수와 클래스, 모듈에는 Sphinx 문서 자동 생성을 위해 reStructuredText(reST) 형식에 맞춰 독스트링(docstring)을 작성해야 한다.

### 구조
1.  **한 줄 요약**: 함수나 클래스의 역할을 한 줄로 명확하게 요약한다.
2.  **상세 설명 (선택 사항)**: 한 줄을 띄고 더 자세한 설명을 작성한다.
3.  **필드 리스트**: 한 줄을 띄고 아래의 필드 리스트를 사용하여 각 항목을 명시한다.

### 주요 필드 리스트
-   `:param <이름>:`: 파라미터에 대한 설명.
-   `:type <이름>:`: 해당 파라미터의 타입.
-   `:return:`: 반환 값에 대한 설명.
-   `:rtype:`: 반환 값의 타입.
-   `:raises <예외 타입>:`: 발생 가능한 예외에 대한 설명.

### 예시
"""함수의 역할을 한 줄로 요약합니다.

필요하다면 여기에 더 상세한 설명을 작성합니다.

:param param1: 첫 번째 파라미터에 대한 설명입니다.
:type param1: int
:param param2: 두 번째 파라미터에 대한 설명입니다.
:type param2: str
:return: 작업 성공 여부를 나타냅니다.
:rtype: bool
:raises ValueError: `param1`이 음수일 경우 발생합니다.
"""