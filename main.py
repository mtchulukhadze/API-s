from fastapi import FastAPI
import sqlite3

app = FastAPI()

db_path = "database.db"

def db():
    conn  = sqlite3.connect(db_path)
    conn.execute("""
        create table if not exists logs2 (
        id int,
        param_name varchar(32),
        param_value int
    )
    """)
    conn.commit()
    conn.close()


def insert(param_name, param_value):
    conn =sqlite3.connect(db_path)
    conn.execute(
        """insert into logs2 ( param_name, param_value ) values (?, ?)""",
        ( param_name, param_value )
    )
    conn.commit()
    conn.close()

db()


@app.get("/set_parameter")
def set_param(param_name, param_value):
    insert(param_name, param_value)

    return {"status": "ok", "name": param_name, "value": param_value}

@app.get("/logs")
def get_logs():

    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        "select param_name, param_value from logs2"
    ).fetchall()
    #conn.execute()
    conn.close()

    return [
        {"param_name": r[0], "param_value": r[1]}
        for r in rows
    ]

