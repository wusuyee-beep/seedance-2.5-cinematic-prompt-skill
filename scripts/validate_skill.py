#!/usr/bin/env python3
"""Validate the repository's Skill structure and local Markdown links."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def fail(message: str) -> None:
    errors.append(message)

skill = ROOT / "SKILL.md"
if not skill.exists():
    fail("SKILL.md is missing")
else:
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")
    else:
        frontmatter = match.group(1)
        for field in ("name", "description"):
            if not re.search(rf"(?m)^{field}:\s*\S", frontmatter):
                fail(f"SKILL.md frontmatter is missing {field}")
    for required in ("无 BGM，无配乐！", "references/duration-recommendation.md", "推荐时长"):
        if required not in text:
            fail(f"SKILL.md is missing required rule: {required}")

old_cases = ROOT / "prompt-library" / "test-cases-v1.md"
if old_cases.exists():
    fail("Withdrawn prompt-library/test-cases-v1.md must not be present")

test_cases = ROOT / "prompt-library" / "test-cases-v2.md"
if not test_cases.exists():
    fail("prompt-library/test-cases-v2.md is missing")
else:
    case_text = test_cases.read_text(encoding="utf-8")
    headings = re.findall(r"(?m)^## Case \d+：", case_text)
    if len(headings) != 2:
        fail(f"The live-action test set must contain exactly two cases, found {len(headings)}")
    sections = re.split(r"(?m)^## Case \d+：", case_text)[1:]
    for index, section in enumerate(sections, start=1):
        if "无 BGM，无配乐！" not in section:
            fail(f"Test Case {index} is missing the exact no-BGM rule")
    prompt_blocks = "\n".join(re.findall(r"```text\n(.*?)\n```", case_text, re.S))
    for forbidden in ("动漫", "二维手绘", "赛璐璐", "卡通", "游戏 CG"):
        if forbidden in prompt_blocks:
            fail(f"Live-action test prompts contain forbidden non-live-action style: {forbidden}")
    for placeholder in ("几人自然交谈", "继续争论", "说了几句", "背景有人说话"):
        if placeholder in prompt_blocks:
            fail(f"Test prompts contain summarized dialogue placeholder: {placeholder}")

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in ROOT.rglob("*.md"):
    if ".git" in markdown.parts:
        continue
    content = markdown.read_text(encoding="utf-8")
    for target in link_pattern.findall(content):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local = target.split("#", 1)[0]
        if local and not (markdown.parent / local).resolve().exists():
            fail(f"Broken local link in {markdown.relative_to(ROOT)}: {target}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Skill structure, required rules, and local Markdown links are valid.")
