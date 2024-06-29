import os
import contextlib
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


if __name__ == "__main__":
    # delete_thumbs()
    # delete_thumbs_db()
    # rename_jpeg()
    # rename()
    # check()
    build_collection()
