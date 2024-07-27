import mysql.connector

# Connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aissam@9090',
    'database': 'test'
}

# Establish the connection to the database
mydb = mysql.connector.connect(**config)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the SQL statement to create the table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  isbn VARCHAR(255) NOT NULL UNIQUE
)
""")

print("Table created successfully!")

sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
val = ("To Kill a Mockingbird", "Harper Lee", "9780446310789")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

mycursor.execute("SELECT * FROM books")
myresult = mycursor.fetchall()

print("Books:")
for row in myresult:
  print(row)

# Update a book's title
sql = "UPDATE books SET title = %s WHERE id = %s"
val = ("Nineteen Eighty-Four", 2)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated.")

# Read the updated book data
mycursor.execute("SELECT * FROM books WHERE id = 2")
myresult = mycursor.fetchone()

print("Updated book:")
print(myresult)

# Delete a book
sql = "DELETE FROM books WHERE id = 1"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# Search for books by title
search_title = "Nineteen"
mycursor.execute("SELECT * FROM books WHERE title LIKE %s", ("%" + search_title + "%",))
myresult = mycursor.fetchall()

print(f"Books with '{search_title}' in the title:")
for row in myresult:
  print(row)


# Close the cursor and connection
mycursor.close()
mydb.close()
