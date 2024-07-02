import os
import re
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
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
    for file in Path("public/gallery").glob("**/*.jpg"):
        if not file.is_file():
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
            pass

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
        if img.has_attr("class") and "baiaimgleft" in img["class"]:
            img["class"].remove("baiaimgleft")
            img["class"].append("float-start")

        img["src"] = img["src"].replace(fr, to)
        tag_target: str = str(img)
        if tag_source != tag_target:
            target = target.replace(tag_source, tag_target)
            assert source != target

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

    for c in re.findall(r"created: .*$", target, re.MULTILINE):
        for u in re.findall(r"updated: .*$", target, re.MULTILINE):
            r = str(c).replace("created:", "updated:")
            target = target.replace(u, r)

    target = re.sub(r"<br\s*\/>", "", target)
    Path(path).write_text(target, encoding="utf-8")
    print(path)


def get_contents():
    path: Path = Path("src/content/posts/").glob("sicurezza/**/*.md")
    _ = list(map(fix_image_url, path))


if __name__ == "__main__":
    # delete_thumbs()
    # delete_thumbs_db()
    # rename_jpeg()
    # rename()
    # check()
    # build_collection()
    get_contents()
