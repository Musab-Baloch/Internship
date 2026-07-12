import sqlite3

connect = sqlite3.connect("UserData.db")

curr = connect.cursor()

### CREATING A TABLE

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# curr.execute(""" CREATE TABLE Users(
#              first_name text,
#              last_name text,
#              email text,
#              password text,
#              plot_data blob,
#              plot_img blob
#              ) 
#              """)

### INSERTING INFO INTO TABLE

# curr.execute("INSERT INTO Users(first_name, last_name, email) VALUES('Abdullah', 'Warraich', 'retard@onplot.com')")

user_infos = [('Abdullah', 'Qureshi', 'retard@onplot.com'),
           ('Hamdan', 'Majeed', 'retard@onplot.com'),
           ('Ali', 'Nahra', 'retard@onplot.com')
        ]

# curr.executemany("INSERT INTO Users(first_name, last_name, email) VALUES(?, ?, ?)", user_infos)

### FETCHING INFO FROM A TABLE

# curr.execute("SELECT rowid, * FROM Users")

# # print(curr.fetchone()[0:3]) #-> first one
# # print(curr.fetchmany(3))
# data = curr.fetchall()

# for user in data[0:2]:
#     print(user)
#     # print(user[0] + ' ' + user[1] + '\t' + user[2])
#     #                                 ^--> == TAB

### SEARCHING INFO IN A TABLE

# curr.execute("SELECT * FROM Users WHERE first_name = 'Ali'")

# curr.execute("SELECT * FROM Users WHERE first_name LIKE 'A%'")


# data = curr.fetchall()

# for user in data:
#     print(user)

### UPDATING INFO IN A TABLE

# curr.execute("""
#             UPDATE Users SET email = 'user@onplot.com'
#             WHERE email = 'retard@onplot.com'
             
#              """)

# curr.execute("""
#             UPDATE Users SET email = 'user@onplot.com'
#             WHERE rowid = 2
            
#              """) #     ^--> updating a specific data entry

###  INFO IN A TABLE

# curr.execute("DELETE from Users WHERE rowid = 4")

### CHANGING ORDER IN A TABLE

# curr.execute("SELECT rowid, * from Users ORDER BY rowid DESC")

# curr.execute("SELECT rowid, * from Users ORDER BY last_name")

### AND / OR

# curr.execute("SELECT * FROM Users WHERE first_name LIKE 'A%' AND rowid = 1")

# curr.execute("SELECT * FROM Users WHERE first_name LIKE 'H%' OR rowid = 1")

# user = curr.fetchall()
# print(user)

### LIMIT

# curr.execute("SELECT rowid, * FROM Users ORDER BY rowid DESC LIMIT 2")
# user = curr.fetchall()
# print(user)

### DROPPING A TABLE

curr.execute("DROP TABLE Users")

connect.commit()

connect.close()

