import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",# your password
  database="" # your database name
)


# cursor is a database object that retrieves data from result sets one row at a time
mycursor = mydb.cursor()



#creating necessary tables
"""
mycursor.execute("CREATE TABLE VENDOR (vendor_id INT,vendor_name VARCHAR(255),license_start DATE, license_end DATE, PRIMARY KEY (vendor_id))")
mycursor.execute("CREATE TABLE ITEM (item_id INT,item_name VARCHAR(255),item_type VARCHAR(255),previous_price float, last_sold_date DATE,PRIMARY KEY (item_id))")
mycursor.execute("CREATE TABLE AUCTION (auction_id INT,vendor_id INT, item_id INT,price float,PRIMARY KEY (auction_id),FOREIGN KEY (vendor_id) REFERENCES VENDOR(vendor_id),FOREIGN KEY (item_id) REFERENCES ITEM(item_id))")
"""

#initializing fields of tables with their data types and give 5 records
"""
sql="INSERT INTO VENDOR(vendor_id,vendor_name,license_start,license_end) VALUES (%s, %s,%s, %s)"
val=[
    (1,'Efsa','2022-05-09','2023-05-09'),
    (2,'Ege','2009-06-09','2023-06-09'),
    (3,'Fatih','2022-11-09','2023-11-09'),
    (4,'Seydi','2008-01-01','2023-05-09'),
    (5,'Sadet','2022-10-10','2023-10-11')
    ]

mycursor.executemany(sql, val)

#commit saves all changes
mydb.commit()
"""

#initializing fields of tables with their data types and give 5 records
"""
sql2="INSERT INTO ITEM(item_id,item_name,item_type,previous_price,last_sold_date) VALUES (%s, %s,%s, %s,%s)"
val2=[
    (10,'apple','fruit',20000,'2022-11-29'),
    (11,'melon','fruit',80000,'2022-11-28'),
    (12,'pineapple','fruit',212314,'2008-11-29'),
    (13,'tomatoe','vegitable',100,'2006-11-29'),
    (14,'cucumber','vegitable',230004,'2015-08-29')]

mycursor.executemany(sql2, val2)

mydb.commit() 
"""

#initializing fields of tables with their data types and give 5 records
"""
sql3="INSERT INTO AUCTION (auction_id,vendor_id,item_id,price) VALUES (%s, %s,%s,%s)"
val3=[
    (20,1,12,15),
    (21,2,13,2),
    (22,3,10,3),
    (23,4,11,9),
    (24,5,14,3)]

mycursor.executemany(sql3, val3)

mydb.commit()
"""


#functions in question4
expensive="SELECT * FROM ITEM WHERE previous_price>25000"
mycursor.execute(expensive)
myresult = mycursor.fetchall()

popular="SELECT * FROM ITEM WHERE last_sold_date>'2010-01-01'"
mycursor.execute(popular)
myresult2 = mycursor.fetchall()

result1="SELECT item_name,previous_price FROM ITEM WHERE previous_price>25000"
mycursor.execute(result1)
myresult3 = mycursor.fetchall()

result2="SELECT item_name,previous_price FROM ITEM WHERE previous_price>25000 or last_sold_date>'2010-01-01'"
mycursor.execute(result2)
myresult4 = mycursor.fetchall()

result3="SELECT * FROM VENDOR,AUCTION"
mycursor.execute(result3)
myresult5 = mycursor.fetchall()

result4="SELECT * FROM ITEM INNER JOIN AUCTION ON ITEM.item_id=AUCTION.item_id where last_sold_date>'2010-01-01'"
mycursor.execute(result4)
myresult5 = mycursor.fetchall()

#question 5
q5="SELECT * FROM VENDOR WHERE vendor_id IN (SELECT vendor_id FROM ITEM INNER JOIN AUCTION ON ITEM.item_id=AUCTION.item_id where last_sold_date<'2010-01-01')"
mycursor.execute(q5)
myresult6= mycursor.fetchall()

for x in myresult6:
  print(x)

#question 6
q6="SELECT item_type,SUM(previous_price) FROM ITEM GROUP BY item_type"
mycursor.execute(q6)
myresult7= mycursor.fetchall()
print(myresult7)