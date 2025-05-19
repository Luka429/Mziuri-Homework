import sqlite3

conn = sqlite3.connect(
    "sports.db"
)

c = conn.cursor()

c.execute (

"""

    CREATE TABLE IF NOT EXISTS footballers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    lastname TEXT,
    age INTEGER,
    country TEXT
    );
"""
)

c.execute(
    """
    DELETE FROM footballers
"""
)

c.execute(
    """
    INSERT INTO footballers (name,lastname,age,country) VALUES ('harry', 'maguire',32,'UK');
    """
)

c.execute(
    """
    INSERT INTO footballers (name,lastname,age,country) VALUES ('cristiano', 'ronaldo',40,'Portugal');
    """
)

c.execute(
    """
    INSERT INTO footballers (name,lastname,age,country) VALUES ('khvicha', 'kvaratskhelia',24,'Georgia');
    """
)

c.execute(
    """
    INSERT INTO footballers (name,lastname,age,country) VALUES ('antony', 'dos santos',25,'Brazil');
    """
)

c.execute(
    """
    INSERT INTO footballers (name,lastname,age,country) VALUES ('ivan', 'rakitic',37,'Croatia');
    """
)

c.execute(
    """
    UPDATE footballers Set age = 20 WHERE age = 37;
    """
)

c.execute(
    """
    DELETE FROM footballers WHERE name = 'ivan';
    """
)

conn.commit()

c.execute('SELECT * FROM footballers')
rows = c.fetchall()
conn.close()

for row in rows:
   print(row)