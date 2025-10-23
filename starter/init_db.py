import sqlite3

with sqlite3.connect("blog.db") as con:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL);


    INSERT INTO posts (title, content) VALUES
        ("Første innlegg", "<p>Halloween</p>"),
        ("Andre innlegg", "<p>Skumle matforslag</p>"),
        ("Tredje innlegg", "<p>Kostymefavoritten</p>")
    """)
