import os
import re
import duckdb
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime, timedelta
from PIL import Image, ExifTags


def rename_jpeg():
    files = [file for file in Path("../").glob("**/*.JPG") if file.suffix == ".JPG"]
    for file in files:
        file.rename(file.with_suffix(".jpg"))


def rename():
    for file in Path("src/content/gallery/2023-08-sicilia").glob("*.*"):
        if file.is_dir():
            continue

        image = Image.open(file).getexif()
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in image.items()
            if k in ExifTags.TAGS and type(v) is not bytes
        }
        try:
            created = exif.get("DateTime").replace(":", "").replace(" ", "-")
            print(created)
        except:
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
            print("last modified: %s" % datetime.fromtimestamp(atime))
            print("last modified: %s" % datetime.fromtimestamp(mtime))
            print("last modified: %s" % datetime.fromtimestamp(ctime))
            print()

    #     hash = str(uuid.uuid4())[:8]
    #     print(f"{file} -> {file.parent}-{hash}{file.suffix}")


def fix_download_url(path: Path) -> tuple[str, str]:
    source: str = Path.read_text(path, encoding="utf-8")
    target: str = source
    soup = BeautifulSoup(source, "lxml", from_encoding="utf-8")

    # replace the url for the docs
    # dmdocuments -> /docs
    for a in soup.find_all("a"):
        fr: str = "dmdocuments/"
        to: str = "/docs/"

        tag_source: str = str(a)
        a["href"] = a["href"].replace(fr, to)
        tag_target: str = str(a)
        if tag_source != tag_target:
            target = target.replace(tag_source, tag_target)
            assert source != target

    target = re.sub(r"<br\s*\/>", "", target)
    Path(path).write_text(target, encoding="utf-8")
    print(path)


def get_db() -> duckdb.DuckDBPyConnection:
    # if os.path.exists("db.duckdb"):
    #     os.unlink("db.duckdb")

    if not os.path.exists("../db.duckdb"):
        conn = duckdb.connect("../db.duckdb")
        # Create a table with 2 fields, filename and content
        conn.query("CREATE TABLE posts (filename TEXT, content TEXT)")

        print("Loading files...")
        for file in sorted(Path("src/content").glob("**/*.md")):
            load_file(conn, file)

    return duckdb.connect("../db.duckdb")


def load_file(db: duckdb.DuckDBPyConnection, file: Path):
    # Insert filename and content into the table
    text: str = ""
    try:
        text = file.read_text(encoding="utf-8")
        text = text if isinstance(text, str) else text.decode("utf-8")
        text = text.replace("'", "")
        db.execute(f"INSERT INTO posts VALUES ('{file.name}', '{text}')")
    except Exception as e:
        print(e)


def check_docs():
    db = get_db()
    files: list[Path] = Path("public/docs").glob("**/*.pdf")
    missing: list = []
    for file in files:
        rows = db.execute(
            "select * from posts where content like ?", [f"%{file.stem}%"]
        ).fetchall()
        if len(rows) == 0:
            missing.append(file.as_posix())

    for m in missing:
        print(m)


if __name__ == "__main__":
    check_docs()
