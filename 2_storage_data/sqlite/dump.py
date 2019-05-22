import os
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute(
    """
    CREATE TABLE 'users' (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30),
        birthday VARCHAR(30)
    )
    """
)

conn.execute(
    """
    INSERT INTO users(id, first_name, last_name, birthday)
    VALUES (1, 'Eugene', 'Bunin', '01-06-1999'),
           (2, 'John', 'Doe', '18-01-1875')
    """
)

with open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)
        print('{}\n'.format(line))

# os.remove('db.sqlite3')
