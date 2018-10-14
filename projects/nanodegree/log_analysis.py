# "Database code" for the DB Forum.

import psycopg2
import argparse


def get_posts(val):
  """Return all posts from the 'database', most recent first."""
  db_val = psycopg2.connect("dbname=news")
  cursor = db_val.cursor()
  results = cursor.execute(val)
  for result in results.fetchall():
      print(result)      
  db.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    get_posts(args[1])
    

