Task 2 - Saving to a Database
=============================
Extend your program from Task 1 so that it can store the films permanently in a database. Use what we have gone through in class to come up with a sensible structure. After the user has inputted all their films, the program should output the films it has in the database.

SQL in Python
-------------
Remember to include and call the following function when performing actions on the database:

```python
# Import the SQLite library.
import sqlite3 as lite


def run_query(query):
  # Connect to the database.
  con = lite.connect('database.db')

  # Perform all actions inside this block.
  with con:
      # Create a cursor object.
      cur = con.cursor()
      # Execute your query
      cur.execute(query)
      # Fetch the query results
      return cur.fetchall()
```