import sqlite3

conn = sqlite3.connect("../{{ cookiecutter.database }}.db")
conn.query("select 1;")
conn.close()
