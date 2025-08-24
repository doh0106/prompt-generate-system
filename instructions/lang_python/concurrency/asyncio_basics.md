## [Python] 비동기 프로그래밍 (Asyncio Basics)

파이썬의 `asyncio` 라이브러리를 사용하여 비동기 코드를 작성할 때, 아래의 핵심 원칙과 모범 사례를 반드시 준수해야 한다.

### 언제 사용해야 하는가?
- `asyncio`는 **I/O 바운드(I/O-bound)** 작업에 최적화되어 있다.
- 네트워크 요청(API 호출, DB 조회), 파일 읽기/쓰기 등 프로그램이 외부 자원의 응답을 기다리며 대기하는 시간이 긴 작업에 사용하라.
- 복잡한 수학 계산과 같은 **CPU 바운드(CPU-bound)** 작업에는 효과적이지 않으며, 이런 경우에는 `multiprocessing`을 고려해야 한다.

### 핵심 규칙 (Core Rules)
1.  **`async def`로 코루틴 정의**: 비동기적으로 실행될 함수는 반드시 `async def` 키워드를 사용하여 코루틴(coroutine) 함수로 정의하라.
2.  **`await`으로 코루틴 실행**: 다른 코루틴을 호출하거나, `awaitable` 객체를 기다릴 때는 반드시 `await` 키워드를 사용하라. `await` 없이 코루틴을 호출하면 아무 일도 일어나지 않는다.
3.  **동시 실행은 `gather` 또는 `create_task`**: 여러 코루틴을 동시에 실행하고 그 결과를 모으고 싶을 때는 `asyncio.gather()`를 사용하라. 특정 코루틴을 즉시 백그라운드에서 실행시키고 싶을 때는 `asyncio.create_task()`를 사용하라.

### 주의사항 (Cautions)
1.  **블로킹(Blocking) 코드 절대 금지**: `async def` 함수 안에서 `time.sleep()`, `requests.get()`과 같은 일반적인 동기(blocking) I/O 함수를 절대 사용하지 마라. 이는 전체 이벤트 루프를 멈추게 하여 비동기의 이점을 완전히 없앤다.
2.  **비동기 라이브러리 사용**: 동기 함수 대신, 비동기를 지원하는 라이브러리를 사용해야 한다.
    -   `time.sleep(1)` → `await asyncio.sleep(1)`
    -   `requests.get()` → `aiohttp.ClientSession().get()`
    -   `psycopg2` → `asyncpg`