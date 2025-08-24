# engine/combiner.py
import os
from pathlib import Path

from .templates import MAIN_PROMPT_TEMPLATE, RULE_TEMPLATE


class PromptAssembler:
    """
    Instruction 모듈(.md)들을 조합하여 LLM을 위한 최종 프롬프트를 생성하는 클래스.
    확장성을 고려하여 설계되었습니다.
    - __init__에서 instruction 루트 디렉토리를 설정하여 유연성을 높임.
    - 모든 instruction 파일을 미리 스캔하여 매번 디렉토리를 탐색하는 비용을 줄임.
    - 향후 모듈 선택 전략(예: LLM 기반)을 새로운 메서드로 쉽게 추가 가능.
    """

    def __init__(self, instructions_root: Path = None):
        """
        PromptAssembler를 초기화합니다.
        Args:
            instructions_root (Path, optional): instructions 디렉토리의 경로.
                                                None이면 스크립트 위치 기준으로 자동 설정.
        """
        if instructions_root is None:
            self.instructions_root = Path(__file__).parent.parent / "instructions"
        else:
            self.instructions_root = instructions_root
        if not self.instructions_root.is_dir():
            raise FileNotFoundError(
                f"Instruction directory not found at: {self.instructions_root}"
            )
        # 초기화 시 모든 .md 파일의 경로를 미리 스캔하여 저장 (효율성 향상)
        self.all_instructions = list(self.instructions_root.rglob("*.md"))
        print(
            f"✅ Initialized PromptAssembler with {len(self.all_instructions)} instruction files found."
        )

    def _find_files_by_keywords(self, keywords: list[str]) -> list[Path]:
        """
        미리 스캔된 파일 목록에서 키워드와 일치하는 파일 경로를 찾습니다.
        """
        if not keywords:
            return []
        matched_files = set()
        for keyword in keywords:
            for file_path in self.all_instructions:
                if keyword.lower() in str(file_path).lower().replace(os.sep, "/"):
                    matched_files.add(file_path)
        return sorted(list(matched_files))

    def assemble(self, task: str, context: str, keywords: list[str]) -> str:
        """
        사용자의 과업, 맥락, 키워드를 받아 최종 LLM 프롬프트를 생성합니다.
        Args:
            task (str): LLM에게 시킬 주요 과업.
            context (str): 과업 수행에 필요한 추가적인 맥락 정보.
            keywords (list[str]): 조합할 instruction .md 파일을 찾기 위한 키워드.
        Returns:
            str: 모든 정보가 조합된 최종 프롬프트 문자열.
        """
        # 1. 키워드를 기반으로 관련 .md 파일 찾기 (전략 패턴 적용 가능 지점)
        instruction_files = self._find_files_by_keywords(keywords)
        if not instruction_files:
            print(
                "⚠️ Warning: No matching instruction files found for the given keywords."
            )
        # 2. 찾은 파일들의 내용을 읽어와 RULE_TEMPLATE에 맞춰 포맷팅
        formatted_rules = []
        for file_path in instruction_files:
            try:
                content = file_path.read_text(encoding="utf-8")
                formatted_rules.append(
                    RULE_TEMPLATE.format(
                        content=content,
                    )
                )
            except Exception as e:
                print(f"❌ Error reading file {file_path}: {e}")
        # 3. 포맷팅된 모든 규칙들을 하나의 문자열로 결합
        rules_string = "\n---\n".join(formatted_rules)
        # 4. 최종 템플릿에 모든 정보를 삽입하여 프롬프트 완성
        final_prompt = MAIN_PROMPT_TEMPLATE.format(
            task=task,
            context=context,
            rules=rules_string if formatted_rules else "적용할 특정 규칙이 없습니다.",
        )
        return final_prompt


# 이 스크립트를 직접 실행했을 때의 예시 (클래스 기반 사용법)
if __name__ == "__main__":
    # --- 사용자 입력 예시 ---
    user_task = "새로운 주문이 들어왔을 때, 주문 정보를 처리하고 데이터베이스에 저장하는 함수를 만들어줘."
    user_context = "이 함수는 FastAPI 애플리케이션의 일부로 동작할 예정이야. 데이터베이스는 PostgreSQL을 사용하고 있어."
    user_keywords = [
        "python/error",  # 'lang_python/error_handling.md'
        "docstring/google",  # 'lang_python/docstring/google_style.md'
        "style/naming",  # 'lang_python/style/naming_convention.md'
        "security/input",  # 'lang_python/security/input_validation.md'
        "architecture/api",  # 'architecture/api_restful_design.md'
    ]
    # -------------------------
    # 1. PromptAssembler 인스턴스 생성
    #    - 클래스가 생성될 때 모든 .md 파일을 미리 스캔합니다.
    assembler = PromptAssembler()
    # 2. assemble 메서드를 호출하여 프롬프트 조합
    #    - 이제 조합 행위는 assembler 객체의 책임입니다.
    generated_prompt = assembler.assemble(
        task=user_task, context=user_context, keywords=user_keywords
    )
    # 3. 결과 출력
    print("\n--- 📝 GENERATED PROMPT ---")
    print(generated_prompt)
    # 4. (참고) 찾은 파일 목록 확인
    print("\n--- 🗂️ MATCHED FILES ---")
    matched_files = assembler._find_files_by_keywords(user_keywords)
    for f in matched_files:
        print(f.relative_to(assembler.instructions_root))
