from pathlib import Path


def read_prompt(name: str) -> str:
    prompt_file = Path(__file__).parent / "advisor" / "prompts" / f"{name}.md"
    return prompt_file.read_text()
