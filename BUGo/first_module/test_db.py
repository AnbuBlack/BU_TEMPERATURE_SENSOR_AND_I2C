import pymysql
c = pymysql.connect(host = '127.0.0.1', user="root", passwd="admin", db="SENSORS_INFO", port= 3306)

cursor = c.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS SENSORS_INFO (name TEXT, pass TEXT)")
