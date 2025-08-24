## [Idiom] 컴프리헨션 (Comprehensions)

리스트, 딕셔너리, 세트를 생성할 때, `for` 루프와 `.append()` 메서드를 사용하는 것보다 간결하고 파이썬다운 컴프리헨션(Comprehension) 구문을 우선적으로 사용해야 한다.

-   **List Comprehension**:
    -   `for` 루프를 사용하여 리스트를 생성하는 코드를 한 줄로 표현하라.
    -   `[expression for item in iterable if condition]`
    -   예: `[x*x for x in range(10) if x % 2 == 0]`

-   **Dictionary Comprehension**:
    -   키-값 쌍을 가진 딕셔너리를 효율적으로 생성하라.
    -   `{key_expression: value_expression for item in iterable if condition}`
    -   예: `{x: x*x for x in range(5)}`

-   **Set Comprehension**:
    -   중복을 허용하지 않는 세트를 효율적으로 생성하라.
    -   `{expression for item in iterable if condition}`
    -   예: `{s.lower() for s in ['Apple', 'Banana', 'Apple']}`

단, 로직이 지나치게 복잡해져 가독성을 해치는 경우에는 전통적인 `for` 루프를 사용하는 것이 더 나을 수 있다.