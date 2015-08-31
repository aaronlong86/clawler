__author__ = 'Administrator'
#!/usr/bin/env python
import pymysql

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='aaronlong',
                             db='basicdata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    with connection.cursor() as cursor1:
        # Read a single record
        sql = "select * from weatherstation;"
        cursor1.execute(sql)
        #print(cursor1.fetchall())
        #result = cursor.fetchone()
        #print(result)
        for code in cursor1:
            print(code)
        cursor1.close()
finally:
    connection.close()
