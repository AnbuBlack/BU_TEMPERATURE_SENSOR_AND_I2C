import pymysql
c = pymysql.connect(host = '127.0.0.1', user="root", passwd="admin", db="mysql", port= 3306)

cursor = c.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test (name TEXT, pass TEXT)")
