import random
import pandas as pd
import sqlite3
import sys, getopt

def get_connection():
    conn = sqlite3.connect("censo.db")
    return conn

def sql_get_by_id(user_id):
	connection = get_connection()
	cur = connection.cursor()
	cur.execute("select * from usuarios u where ID = 2;")
	rows = cur.fetchall()
	return rows[0]

if __name__ == "__main__":
	USER_ID = int( sys.argv[1] )
	user = sql_get_by_id(USER_ID)
	print("USER: ",user)
