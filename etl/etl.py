import os
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from typing import NamedTuple
from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def extract() -> pd.DataFrame:
    cache: Path = Path("etl/db/db.feather")
    if cache.exists():
        return pd.read_feather(cache.as_posix())

    conn: PooledMySQLConnection | MySQLConnectionAbstract = connect(
        host="localhost",
        user="root",
        password="root",
        database="db",
    )

    df: pd.DataFrame = pd.read_sql_query(
        """
            SELECT `nuvrj_content`.`id`,
                   `nuvrj_content`.`title`,
                   `nuvrj_content`.`alias`,
                   `nuvrj_categories`.`title` as category,
                   `nuvrj_content`.`introtext` as text,
                   `nuvrj_content`.`created`,
                   `nuvrj_content`.`created_by`,
                   `nuvrj_content`.`created_by_alias`,
                   `nuvrj_content`.`modified` as updated,
                   `nuvrj_content`.`featured`,
                   `nuvrj_users`.`name` as user
            FROM `nuvrj_content` 
            INNER JOIN `nuvrj_categories` 
               ON `nuvrj_content`.`catid` = `nuvrj_categories`.`id`
            INNER JOIN `nuvrj_users`
               ON `nuvrj_content`.`created_by` = `nuvrj_users`.`id`
            ORDER BY `nuvrj_content`.`id`
        """,
        conn,
    )
    df.to_feather("db/db.feather")
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df["created_by"] = list(
        df.apply(
            lambda r: (
                r["created_by_alias"] if r["created_by_alias"] != "" else r["user"]
            ),
            axis=1,
        )
    )
    df["category"] = df["category"].str.lower()

    df.loc[df.category == "non categorizzato", "category"] = "baialupo"
    df.loc[df.category == "eventi", "category"] = "news"
    df.loc[df.category == "dpr 133", "category"] = "news"
    df.loc[df.category == "novita'", "category"] = "news"
    df.loc[df.category == "notizie", "category"] = "news"
    df.loc[df.category == "avionica e strumenti", "category"] = "avionica"

    df.loc[df["updated"].isnull(), "updated"] = df.loc[df["updated"].isnull()][
        "created"
    ]

    df.loc[df.title.str.contains(":"), "title"] = df.loc[
        df.title.str.contains(":")
    ].title.apply(lambda x: '"' + x.replace('"', "'") + '"')

    df = df.drop(columns=["created_by_alias", "user"])
    print(f"{df.shape[0]} rows loaded")
    return df


async def load(rows: pd.DataFrame) -> None:
    tasks: list = [write_content(row) for row in rows.itertuples()]
    await asyncio.gather(*tasks)

    # specific page handlig
    source = Path("src/content/posts/privacy/195-cookie-policy.md")
    target = Path("src/pages/privacy.astro")
    target.unlink(missing_ok=True)
    source.rename(target)
    os.system(f'rmdir "{source.parent.as_posix()}"')
    source.parent.unlink(missing_ok=True)


async def write_content(data: NamedTuple) -> None:
    html = BeautifulSoup(data.text, "html.parser")
    path = Path(f"src/content/posts/{data.category}/{data.id}-{data.alias}.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        + f"id: {data.id}\n"
        + f"title: {data.title}\n"
        + f"category: {data.category}\n"
        + f"featured: {data.featured}\n"
        + f"created: {data.created.isoformat()}\n"
        + f"updated: {data.updated.isoformat()}\n"
        + f"created_by: {data.created_by}\n"
        + f"---\n{html.prettify(formatter='minimal')}",
        encoding="utf-8",
    )


async def main():
    rows: list = extract()
    rows = transform(rows)
    await load(rows)


if __name__ == "__main__":
    # import os
    # os.system("rm -Rf /Users/ignazio/baialupo.astro/src")
    asyncio.run(main())
