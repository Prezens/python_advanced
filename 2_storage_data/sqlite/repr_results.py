import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute(
    """
    CREATE TABLE 'users' (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name,
        last_name,
        birthday
    )
    """
)

conn.execute(
    """
    insert into users(id, first_name, last_name, birthday)
    VALUES (1, 'Eugene', 'Bunin', '01-06-1999'),
           (2, 'John', 'Doe', '18-01-1875')
    """
)

conn.row_factory = sqlite3.Row
users = conn.execute('SELECT * FROM "users"').fetchall()

user = users[0]
print(user)
print(user.keys())
print(user['id'], user['ID'])
print(user['first_name'], user['first_NAME'], user['FIRST_NAME'])
