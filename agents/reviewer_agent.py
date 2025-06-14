def handle_review(task: str) -> str:
    return """\
# REVIEW NOTES:

✅ Tests check output type and structure.
✅ Test cases cover missing keys, format injection, and bad API tokens.

⚠️ Suggestions:
- Add test for template not found (FileNotFoundError)
- Add edge case where metrics is empty dict
- Consider mocking Telegram API rather than making real call in tests
"""
