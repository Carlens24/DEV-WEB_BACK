import sqlite3

def show_app():
    con = sqlite3.connect("customers02.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT
                )""")

    many = [('Rose', 'Oslin', 'roseoslin@gmail.com'),
            ('Schneidine', 'Oslin', 'schneidineoslin@gmail.com'),
            ('carlens', 'Oslin', 'carlensoslin@gmail.com'),
            ('Maria', 'Rosette', 'mariarosette@gmail.com'),
            ('André', 'Barros', 'andrébarros@gmail.com')]

    cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", many)

    cur.execute("SELECT * FROM customers")
    items = cur.fetchall()

    print("First_name" + "\tLast_name" + "\t\tEMAIL")
    print("--" * 30)
    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2])

    con.commit()
    con.close()

def add_one(fn, ln, email):
    con = sqlite3.connect("customers02.db")
    cur = con.cursor()
    cur.execute("INSERT INTO customers VALUES (?, ?, ?)", (fn, ln, email))
    con.commit()
    con.close()

def remove_one(first_name):
    con = sqlite3.connect("customers02.db")
    cur = con.cursor()
    cur.execute("DELETE FROM customers WHERE first_name = ?", (first_name,))
    con.commit()
    con.close()

def many(many):
    con = sqlite3.connect("customers02.db")
    cur = con.cursor()
    cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", many)
    con.commit()
    con.close()

if __name__ == "__main__":
    show_app()
