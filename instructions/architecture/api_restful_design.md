## [API] RESTful API 설계 원칙

HTTP 기반 API를 설계할 때, REST(Representational State Transfer) 아키텍처 스타일의 핵심 제약 조건을 반드시 준수해야 한다.

### 핵심 규칙
1.  **자원(Resource) 중심 설계**:
    -   API의 모든 것은 '자원'으로 식별되어야 한다.
    -   자원의 이름은 URL 경로에 명사형(복수형 권장)으로 표현하라. (예: `/users`, `/orders`)
    -   동사(행위)는 URL 경로에 사용하지 마라. (예: `/getUsers` (X), `/createUser` (X))

2.  **HTTP 메서드를 통한 행위 표현**:
    -   `GET`: 자원 조회
    -   `POST`: 새로운 자원 생성
    -   `PUT` / `PATCH`: 기존 자원 전체 수정 / 부분 수정
    -   `DELETE`: 자원 삭제

3.  **명확한 HTTP 상태 코드 사용**:
    -   `2xx` (성공): `200 OK`, `201 Created`, `204 No Content`
    -   `4xx` (클라이언트 오류): `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`
    -   `5xx` (서버 오류): `500 Internal Server Error`

4.  **상태 비저장 (Stateless)**: 서버는 클라이언트의 상태를 저장하지 않아야 한다. 각 요청은 자신을 처리하는 데 필요한 모든 정보를 포함해야 한다(예: 인증을 위한 JWT 토큰).

5.  **일관된 응답 형식**:
    -   JSON 형식을 기본으로 사용하라.
    -   데이터 필드명의 네이밍 컨벤션(예: camelCase)을 일관되게 유지하라.
    -   성공 및 실패 응답의 구조를 일관되게 설계하라. (예: `{"data": ...}` 또는 `{"error": ...}`)

6.  **HATEOAS (Hypermedia as the Engine of Application State)** - (권장): 응답에 관련된 다음 행동을 할 수 있는 링크를 포함하여 API의 자체적인 탐색이 가능하도록 하라.