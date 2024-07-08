import os
import re
import duckdb
import contextlib
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime, timedelta
from PIL import Image, ExifTags


def check() -> None:
    files = Path("public/gallery").glob("**/*")
    for file in files:
        if file.is_file() and file.suffix != ".jpg":
            print(file.as_posix())
        if file.is_dir() and file.name.endswith("/thumbs"):
            print(file.as_posix())


def delete_thumbs() -> None:
    for file in Path("public/gallery").glob("**/thumbs"):
        if not file.as_posix().endswith("/thumbs"):
            return
        os.system(f"rmdir /q/s {file.absolute()}")


def delete_thumbs_db() -> None:
    for file in Path("public/gallery").glob("**/Thumbs.db"):
        if not file.is_file() or file.name != "Thumbs.db":
            return
        file.unlink()


def rename_jpeg():
    files = [
        file
        for file in Path("public/gallery").glob("**/*.JPG")
        if file.is_file() and file.suffix.endswith(".JPG")
    ]
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


def get_dates_from_file(files: list[Path]) -> tuple[datetime, datetime]:
    dates: list[datetime] = [None] * len(files)
    for n, file in enumerate(files):
        stat = Path(file).stat()
        dates[n] = datetime.fromtimestamp(stat.st_mtime)
    dates = [d for d in dates if d]
    return min(dates), max(dates)


def get_dates_from_exif(files: list[Path]) -> tuple[datetime, datetime]:
    dates: list[datetime] = [None] * len(files)
    for n, file in enumerate(files):
        try:
            image = Image.open(file).getexif()
            exif = {
                ExifTags.TAGS[k]: v
                for k, v in image.items()
                if k in ExifTags.TAGS and type(v) is not bytes
            }
            cdate, ctime = exif.get("DateTime").split(" ")
            cdate = cdate.replace(":", "-")
            dates[n] = datetime.fromisoformat(f"{cdate}T{ctime}+01")
        except Exception as e:
            print(f"{file}: No exif info have been found")

    dates = [d for d in dates if d]
    return min(dates), max(dates)


def build_collection():
    for f in Path("src/content/gallery").glob("*"):
        if f.is_file():
            continue
        file: str = f"{f.parts[-1]}.yaml"
        title: str = f"{f.parts[-1]}".title()
        pics: list[Path] = [file for file in f.glob("*.jpg") if file.is_file()]
        cover: str = list(pics)[0].relative_to(f.parent).as_posix()

        try:
            created, updated = get_dates_from_exif(pics)
        except ValueError:
            created, updated = get_dates_from_file(pics)

        Path(f.parent / file).write_text(
            "\n".join(
                [
                    f"title: {title}",
                    f"cover: ./{cover}",
                    f"created: {created.isoformat()}",
                    f"updated: {updated.isoformat()}",
                ]
            )
        )


def fix_image_url(path: Path) -> tuple[str, str]:
    source: str = Path.read_text(path, encoding="utf-8")
    target: str = source
    soup = BeautifulSoup(source, "lxml", from_encoding="utf-8")

    # fix float left class
    for img in soup.find_all("img"):
        # replace the class baiaimgleft with the tailwind float-start in all images when present
        fr: str = "images/stories/"
        to: str = "/img/stories/"
        tag_source: str = str(img)
        img["class"] = "float-start mr-3 w-[300px]"
        with contextlib.suppress(KeyError):
            del img.attrs["style"]
        with contextlib.suppress(KeyError):
            del img.attrs["border"]
        with contextlib.suppress(KeyError):
            del img.attrs["width"]
        with contextlib.suppress(KeyError):
            del img.attrs["height"]

        img["src"] = img["src"].replace(fr, to)
        tag_target: str = str(img)
        if tag_source != tag_target:
            target = target.replace(tag_source, tag_target)

        matches: list = re.findall(r"^featured:\s*.*$", target, re.MULTILINE)
        for m in matches:
            target = target.replace(m, f"{m}\ncover: {img['src']}")

        if source != target:
            path.write_text(target, encoding="utf-8")
            print(f"{path.as_posix()} fixed")


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


def fix_date(path: Path):
    source: str = Path.read_text(path, encoding="utf-8")
    fr = re.findall(r"^created:\s*(.*)$", source, re.MULTILINE)
    to = re.findall(r"^updated:\s*(.*)$", source, re.MULTILINE)
    if fr and to:
        delta: timedelta = datetime.fromisoformat(to[0]) - datetime.fromisoformat(fr[0])
        if delta < timedelta(days=7):
            return
        target = source.replace(to[0], fr[0])
        if source != target:
            Path(path).write_text(target, encoding="utf-8")
            print(path)


def check_docs(path: Path):
    if path.suffix in [".png", ".jpg", ".gif"]:
        return
    print(path.as_posix())


def get_db() -> duckdb.DuckDBPyConnection:
    # if os.path.exists("db.duckdb"):
    #     os.unlink("db.duckdb")

    if not os.path.exists("db.duckdb"):
        conn = duckdb.connect("db.duckdb")
        # Create a table with 2 fields, filename and content
        conn.query("CREATE TABLE posts (filename TEXT, content TEXT)")

        print("Loading files...")
        for file in sorted(Path("src/content").glob("**/*.md")):
            load_file(conn, file)

    return duckdb.connect("db.duckdb")


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


def check_galleries():
    dirs = len([p for p in Path("src/content/gallery").glob("*") if p.is_dir()])
    files = len(list(Path("src/content/gallery").glob("*.yaml")))
    print(f"dirs: {dirs} / files: {files}")

    folders: list[Path] = []
    for f in Path("src/content/gallery").glob("*"):
        if f.is_file():
            continue
        folders.append(f)
    for f in folders:
        yaml = f.parent / f"{f.parts[-1]}.yaml"
        print(f"{f.as_posix()} -> {yaml}: {yaml.exists()}")


def heic_to_jpeg():
    for file in Path("src/content/gallery/2023-11-cannes").glob("**/*.HEIC"):
        os.system(f"heic-to-jpg -s {file.as_posix()}")


def main():
    # with get_db() as db:
    #     files: list[Path] = sorted(Path("public/img").glob("**/*.*"))
    #     for file in files:
    #         sql: str = f"select filename from posts where content like '%{file.stem}%'"
    #         rows = db.sql(sql).fetchall()
    #         if not rows:
    #             file.rename(Path("img_to_delete") / file.name)

    heic_to_jpeg()


if __name__ == "__main__":
    # delete_thumbs()
    # delete_thumbs_db()
    # rename_jpeg()
    # rename()
    # check()
    # build_collection()
    main()
