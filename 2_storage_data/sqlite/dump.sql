BEGIN TRANSACTION;
CREATE TABLE 'users' (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30),
        birthday VARCHAR(30)
    );
INSERT INTO "users" VALUES(1,'Eugene','Bunin','01-06-1999');
INSERT INTO "users" VALUES(2,'John','Doe','18-01-1875');
COMMIT;
