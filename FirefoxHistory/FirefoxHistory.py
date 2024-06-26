import sqlite3
import platform


def dump_cookies(path, should_dump_table_structure=False):
    con = sqlite3.connect(f"{path}cookies.sqlite")
    cur = con.cursor()

    if should_dump_table_structure:
        res = cur.execute("PRAGMA  table_info(moz_cookies)")
        print(res.fetchall())

    res = cur.execute("SELECT name, host, path, lastAccessed FROM moz_cookies ORDER BY host")
    for row in res.fetchall():
        print(row)

    con.close()


def dump_history(path, should_dump_table_structure=False):
    con = sqlite3.connect(f"{path}places.sqlite")
    cur = con.cursor()

    if should_dump_table_structure:
        res = cur.execute("PRAGMA  table_info(moz_places)")
        print(res.fetchall())

    res = cur.execute("SELECT url, title, visit_count, hidden, frecency, last_visit_date FROM moz_places ORDER BY url")
    for row in res.fetchall():
        print(row)

    cur.close()


if __name__ == "__main__":
    path = "C:\\Users\\mrajw\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gms2uh6q.default-release\\"

    dump_history(path)
    dump_cookies(path)
