import re

CHECK = " ✓"

def fix_line(line):
    # Match lines starting with number + dot
    match = re.match(r"^(\d+\.)(\s*)(.*)", line)
    if not match:
        return line

    number, space, content = match.groups()

    # Ensure exactly one space after the number
    fixed = f"{number} {content.strip()}"

    # Add check mark if missing
    if not fixed.rstrip().endswith("✓"):
        fixed += CHECK

    return fixed + "\n"

with open("Week-15.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("Week-15.md", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(fix_line(line))
