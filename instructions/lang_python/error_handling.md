## [Python] 에러 처리 모범 사례 (Error Handling Best Practices)

파이썬 코드 작성 시, 견고한 에러 처리 원칙에 따라 아래의 파이썬 관용구와 모범 사례를 준수해야 한다.

### 1. `try...except...else...finally` 구문을 적극 활용하라
- **`try`**: 예외가 발생할 가능성이 있는 코드 블록.
- **`except [예외 타입] as e`**: 명시된 예외 타입이 발생했을 때 처리할 코드 블록. `Exception` 대신 구체적인 `ValueError`, `TypeError` 등을 사용하라.
- **`else`**: `try` 블록에서 예외가 발생하지 않았을 때만 실행될 코드 블록. 성공 로직을 여기에 배치하여 `try` 블록을 최소화하라.
- **`finally`**: 예외 발생 여부와 상관없이 **항상** 실행될 코드 블록. 리소스 해제 등의 정리 코드를 여기에 배치하라.

### 2. 사용자 정의 예외를 만들어라 (Custom Exceptions)
- 애플리케이션의 특정 도메인에 맞는 예외 상황을 표현하기 위해 사용자 정의 예외 클래스를 만들어라.
- 내장 `Exception` 클래스를 상속받기만 하면 된다.
- 예: `class InvalidOrderError(Exception): pass`

### 3. 예외 다시 던지기 (Re-raising Exceptions)
- `except` 블록에서 잡은 예외를 로깅 등의 처리를 한 후, 상위로 다시 전달해야 할 때는 `raise` 키워드만 단독으로 사용하라. 이렇게 하면 원래의 스택 트레이스(stack trace)가 보존된다.
- 예:
  ```python
  except ValueError as e:
      log.error("잘못된 값으로 인한 오류 발생: %s", e)
      raise # 원래의 ValueError를 그대로 다시 발생시킴