from pathlib import Path
from typing import Generator


def gallery(path: str) -> None:
    files: list[Path] = sorted([p for p in Path(path).glob("*")])

    p = Path(f"{path}.yaml")
    print(p.name)
    text: str = p.read_text()
    if "files :" in text:
        return

    text = text.replace("cover: ./", "cover: ")
    text += "\n".join(["", "files:", *[f"  - {(f.parents[-1]/f.name)}" for f in files]])
    p.write_text(text)


def main() -> None:
    paths: Generator[str, None, None] = (
        p.as_posix() for p in Path("src/content/gallery").glob("*") if p.is_dir()
    )

    for p in sorted(paths):
        gallery(p)


if __name__ == "__main__":
    main()
