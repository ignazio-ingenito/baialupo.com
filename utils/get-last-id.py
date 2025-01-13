import re
from pathlib import Path


def get_last_id() -> int:
    path = Path("./src/content/posts")
    ids: list[str] = [
        re.search(r"([0-9]+)\-\w*", p.stem).group(1) for p in path.rglob("*.md")
    ]
    last: int = max(map(int, ids))
    print("Last ID:", last)


if __name__ == "__main__":
    get_last_id()
