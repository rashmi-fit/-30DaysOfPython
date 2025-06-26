import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c= conn.cursor()

def create_table():
      c.execute("""CREATE TABLE IF NOT EXISTS
                todos(
                      task text,
                      category text,
                      date_added text,
                      date_completed text,
                      status integer,
                      position integer
                      )""")


create_table()

# insert todos

def get_all_todos() ->List[Todo]:
      c.execute('select * from todos')
      results = c.fetchall()
      todos = []
      for results in results:
            todos.append(Todo(*results))
      return todos

# def delete_todo(position):
#       c.execute("Delete from todos WHERE position=:position", {"position": position})
#       for pos in range(position+1,count):
#             change_position(pos, pos-1, False)
