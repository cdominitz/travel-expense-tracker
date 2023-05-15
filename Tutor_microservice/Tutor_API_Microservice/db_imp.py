import sqlite3


def conn_to_db():
    conn = sqlite3.connect('tutorials.db')
    return conn


def create_table():
    conn = conn_to_db()
    conn.execute("""CREATE TABLE IF NOT EXISTS links(
            subject,
            outcome,
            link
            )""")

    conn.commit()
    conn.close()


def get_link(info):
    conn = conn_to_db()
    cur = conn.cursor()
    get = "Select link from links where subject=? and outcome=?;"
    cur.execute(get, (info[0], info[1]))
    my_link = cur.fetchone()
    return my_link


def add_link(info):
    conn = conn_to_db()
    cur = conn.cursor()
    add = "insert into links (subject, outcome, link) values(?,?,?);"
    cur.execute(add, (info[0], info[1], info[2]))
    with open('links.txt', 'w') as writeFile:
        writeFile.write('added')
    conn.commit()
    conn.close()
    return 0


def edit_link(info):
    conn = conn_to_db()
    cur = conn.cursor()
    edit = "update links set link=? where subject=? and outcome=?;"
    cur.execute(edit, (info[2], info[0], info[1]))
    with open('links.txt', 'w') as writeFile:
        writeFile.write('edited')
    conn.commit()
    conn.close()
    return 0


def deleteAll():
    conn = conn_to_db()
    cur = conn.cursor()
    cur.execute("delete from links")
    conn.commit()
    conn.close()
    return 0
