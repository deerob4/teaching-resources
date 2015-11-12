Task 2 - Saving to a Database
=============================
Extend your program from Task 1 so that it can store the films permanently in a database. Modify it so that the user can enter multiple genres for the same film. Your database should contain 3 tables - use what we have gone through in class to come up with a sensible structure.

SQL in Python
-------------
Remember to follow these steps when performing actions on the database:

```python
# Import the SQLite library.
import sqlite3 as lite

# Connect to the database.
con = lite.connect('database.db')

# Perform all actions inside this block.
with con:
    # Create a cursor object.
    cur = con.cursor()
    # Execute your query
    cur.execute(YOUR_QUERY)
    # Fetch the query results
    results = cur.fetchall()
```