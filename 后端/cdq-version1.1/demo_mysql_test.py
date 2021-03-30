#!/usr/bin/phython
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='test',
    passwd='4thefuture',
#    database='testdb'
)

mycursor = mydb.cursor()

#mycursor.execute("show databases")
#for x in mycursor:
#    print(x)

mycursor.execute("create database if not exists testdb")
