import sqlite3


class UserDatabaseManager:

  def __init__(self, db_path):
    self.db_path = db_path
    self._create_table()

  def _create_table(self):
    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    address TEXT,
                    mobile TEXT,
                    email TEXT
                )
            """)
      conn.commit()

  def find_user(self, username):
    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute(
          "SELECT id, username, address, mobile, email FROM users WHERE"
          " username = ?",
          (username,),
      )
      row = cursor.fetchone()

      if row:
        return {
            "id": row[0],
            "username": row[1],
            "address": row[2],
            "mobile": row[3],
            "email": row[4],
        }
      return None

  def add_or_update_user(self, username, address, mobile, email):
    existing_user = self.find_user(username)

    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()

      if existing_user:
        cursor.execute(
            """
                    UPDATE users 
                    SET address = ?, mobile = ?, email = ? 
                    WHERE username = ?
                """,
            (address, mobile, email, username),
        )
        conn.commit()
        return "UPDATED"
      else:
        cursor.execute(
            """
                    INSERT INTO users (username, address, mobile, email) 
                    VALUES (?, ?, ?, ?)
                """,
            (username, address, mobile, email),
        )
        conn.commit()
        return "INSERTED"

  def list_all_users(self):
    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute(
          "SELECT id, username, address, mobile, email FROM users ORDER BY"
          " username ASC"
      )
      rows = cursor.fetchall()

      users_list = []
      for row in rows:
        users_list.append({
            "id": row[0],
            "username": row[1],
            "address": row[2],
            "mobile": row[3],
            "email": row[4],
        })

      return users_list