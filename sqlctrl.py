import sqlite3
conn = sqlite3.connect('DevOps.db')
cursor = conn.cursor()

#INSEERT
sqlins = """
INSERT INTO "main"."product_info" ("name", "version", "remark") 
VALUES ( 'car', '3.14', 'ikea');
"""
cursor.execute(sqlins)
cursor.fetchall()
conn.commit()

#SELECT
cursor.execute('SELECT * FROM product_info;')
records = cursor.fetchall()
print (records)