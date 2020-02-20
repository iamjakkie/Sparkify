import psycopg2
import pandas as pd
from sql_queries import *

def test_loadtables(cur):
    """
    Description: This function can be used to test if all tables have been loaded correctly

    Arguments:
    cur: the cursor object.

    Returns:
    None
    """
    test_queries = test_table_queries
    for query in test_queries:
        cur.execute(query)
        result = cur.fetchone()
        assert result[0] > 0, "Count for every table should be greater than 0"
    print("Everything passed")

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    test_loadtables(cur)
    test_nulls



if __name__ == "__main__":
    main()
