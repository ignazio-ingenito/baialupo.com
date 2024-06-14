import os
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from html import escape
from pathlib import Path
from typing import NamedTuple
from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

def extract() -> pd.DataFrame:
    if Path("db/db.feather").exists():
        return pd.read_feather("db/db.feather")
    
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
                   `nuvrj_content`.`modified`,
                   `nuvrj_content`.`featured`,
                   `nuvrj_users`.`name` as user
            FROM `nuvrj_content` 
            INNER JOIN `nuvrj_categories` 
               ON `nuvrj_content`.`catid` = `nuvrj_categories`.`id`
            INNER JOIN `nuvrj_users`
               ON `nuvrj_content`.`created_by` = `nuvrj_users`.`id`
            ORDER BY `nuvrj_content`.`id`
        """,
        conn
    )
    df.to_feather("db/db.feather")
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df["created_by"] = list(df.apply(lambda r: r['created_by_alias'] if r['created_by_alias'] != "" else r['user'], axis=1))
    df["category"] = df["category"].str.lower()

    df.loc[df.category == "non categorizzato", "category"] = "baialupo"
    df.loc[df.category == "eventi", "category"] = "news"
    df.loc[df.category == "dpr 133", "category"] = "news"
    df.loc[df.category == "novita'", "category"] = "news"
    df.loc[df.category == "notizie", "category"] = "news"
    
    df = df.drop(columns=["created_by_alias", "user"])
    print(f"{df.shape[0]} rows loaded")
    return df

async def load(rows: pd.DataFrame) -> None:
    tasks: list = [write_content(row) for row in rows.itertuples()]
    await asyncio.gather(*tasks)

async def write_content(data: NamedTuple) -> None:
    html = BeautifulSoup(data.text, 'html.parser')
    path = Path(f"web/src/content/posts/{data.category}/{data.id}-{data.alias}.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        '---\n' +
        f'id: {data.id}\n' +
        f'title: {escape(data.title)}\n' +
        f'alias: {data.alias}\n' +
        f'category: {data.category}\n' +
        f'featured: {data.featured}\n' +
        f'created: {data.created.isoformat()}\n' +
        f'modified: {data.modified.isoformat()}\n' +
        f'created_by: {data.created_by}\n' +
        f"---\n{html.prettify(formatter='minimal')}",
        encoding="utf-8"
    )

async def main():
    rows: list = extract()
    rows = transform(rows)
    await load(rows)

if __name__ == "__main__":
    os.system("rm -Rf /Users/ignazio/baialupo.astro/src")
    asyncio.run(main())