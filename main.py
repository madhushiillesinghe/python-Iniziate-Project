
import mysql.connector
# create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ijse@1234",
  database="mydatabase"
)

mycursor = mydb.cursor()
# create table student
mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), batch VARCHAR(255))")
print(mydb)

# save student
sql = "INSERT INTO student (id, name, address, batch) VALUES (%s, %s, %s, %s)"
while True:
  id=(input("enter Id:"))
  name=(input("Enter your name: "))
  address=(input("Enter your address: "))
  batch=(input("Enter your batch: "))

  val = (id,name,address,batch)
  mycursor.execute(sql, val)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  say=(input("Do you want to continue?(y/n):"))
  if 'y'==say:
    continue
  else:
    break
