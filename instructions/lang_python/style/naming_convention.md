## [Style] 명명 규칙 (Naming Convention)

파이썬 코드 작성 시, PEP 8에 기반한 아래의 명명 규칙을 엄격하게 준수하여 가독성을 극대화해야 한다.

-   **변수 (Variables)**: `snake_case`
    -   소문자와 언더스코어(_)를 사용한다.
    -   예: `user_name`, `total_count`

-   **함수 (Functions)**: `snake_case`
    -   변수와 동일하게 소문자와 언더스코어를 사용한다.
    -   예: `calculate_sum()`, `get_user_info()`

-   **클래스 (Classes)**: `PascalCase` (또는 `CapWords`)
    -   각 단어의 첫 글자를 대문자로 사용하며 언더스코어는 사용하지 않는다.
    -   예: `UserAccount`, `HttpRequestHandler`

-   **상수 (Constants)**: `SNAKE_CASE_ALL_CAPS`
    -   모든 글자를 대문자로 하고, 단어 사이는 언더스코어로 연결한다.
    -   모듈의 최상단 레벨에서 정의한다.
    -   예: `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`

-   **모듈 (Modules)**: `short_snake_case`
    -   짧은 소문자 이름을 사용하며, 필요시 언더스코어를 사용한다.
    -   예: `db_utils.py`

-   **내부 사용 변수/함수 (Internal Use)**: `_single_leading_underscore`
    -   클래스 내부에서만 사용되는 `protected` 멤버나 모듈 내부용 변수/함수를 의미한다.
    -   `from module import *` 시에는 import 되지 않는다.
    -   예: `_internal_variable`, `def _helper_function():`