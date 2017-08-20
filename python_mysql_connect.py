# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:31:38 2017

@author: umer
"""


import MySQLdb
import pymysql
import pymysql.cursors
#pymysql.install_as_MySQLdb()

# Open database connection
#db = MySQLdb.connect("jdbc:mysql://localhost:3307/demo","demo","root","umer" )

#myConn = DriverManager.getConnection("jdbc:mysql://localhost:3307/demo", "root" , "umer");

# prepare a cursor object using cursor() method
"""
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT email FROM employees;")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
"
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="umer",  # your password
                     db="demo")        # name of the data base
  """                   
db=pymysql.connect(db='demo', user='root', passwd='umer', host='localhost', port=3307)
                     
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT email FROM employees")

# Use all the SQL you like
#cur.execute("SELECT * FROM employees")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print (row[0])

db.close()
