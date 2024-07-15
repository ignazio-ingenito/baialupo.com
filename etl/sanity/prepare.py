import re
import json
import pandas as pd
from pathlib import Path


def parse(path: Path) -> None:
    text: str = path.read_text()
    sections: list[str] = text.split("---")
    frontmatter: list[str] = [l for l in sections[1].split("\n") if l != ""]

    return {
        **{item.split(": ", 1)[0]: item.split(": ", 1)[1] for item in frontmatter},
        **{"content": sections[2], "alias": path.stem},
    }


def load(path: Path) -> None:
    rows: list[dict] = [
        parse(path) for path in Path("src/content/posts").glob("**/*.md")
    ]
    df: pd.DataFrame = pd.DataFrame.from_records(rows)
    df = df.rename(columns={"id": "_id", "alias": "slug", "created_by": "author"})
    df["_type"] = "post"
    df["featured"] = df["featured"].apply(lambda f: True if f else False)
    df["_id"] = df["_id"].astype(int)
    df = df.sort_values(by=["_id"])
    df["cover"] = df["cover"].fillna("/src/content/posts/no-cover.jpg")

    print(df["author"].unique().tolist())

    df.to_json(path, orient="records", lines=True)

    rows: list[str] = path.read_text().split("\n")
    rows = [transform(r) for r in rows if r]
    rows = [json.dumps(r) for r in rows]
    with path.open("w") as file:
        for row in rows:
            file.write(f"{row}\n")


def transform(row: str) -> str:
    r = json.loads(row)
    cover: str = r["cover"].replace("\/", "/").replace("/new", "/public")
    r["cover"] = {
        "_type": "image",
        "_sanityAsset": f"image@file://{cover}",
    }
    return r


def main() -> None:
    load(Path("toimport.ndjson"))


if __name__ == "__main__":
    main()
