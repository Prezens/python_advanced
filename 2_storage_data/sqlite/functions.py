import sqlite3


def upper_word(raw):
    return raw.upper()


conn = sqlite3.connect('db.sqlite3')
conn.create_function('upper', 1, upper_word)
cur = conn.cursor()

cur.execute(
    'INSERT INTO users(first_name) VALUES ("Eugene"), ("Dmitrii")'
)

cur.execute('SELECT upper(first_name) FROM users')
raw = cur.fetchall()
print(raw)
