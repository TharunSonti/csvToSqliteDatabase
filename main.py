import csv, sqlite3

import replit
replit.clear()

conn = sqlite3.connect('test.db')

# https://www.youtube.com/watch?v=pd-0G0MigUA
# Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries

# https://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect("test.db")
cur = con.cursor()

try:
  cur.execute('''CREATE TABLE form990 (ID integer primary key, ein, tax_pd, totfuncexpns, totnetassetend, invstmntsend, invstmntsothrend, invstmntinc, nonintcashend, svngstempinvend)''') # use your column names here
except sqlite3.Error as e:
  print("caught sql error 1:", e.args[0]) 

# try:
#   with con:
#     cur.execute('''INSERT INTO form990 VALUES ('1', '141340095.00', '201706.00', '543879171.00', '442676483.00', '308178100.00', '373205105.00', '12562013.00', '0.00', '1475641.00')''')
# except sqlite3.Error as e:
#   print("caught sql error 2:", e.args[0]) 


with open('data.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    # for i in dr:
    #   print("i is: ", i)
      # print("(", i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend'], ")")
      # cur.execute("INSERT INTO form990 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend']))

    to_db = [(i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend']) for i in dr]

# print("to_db is:\n\n\n", to_db)
cur.executemany("INSERT INTO form990 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", to_db)

con.commit()

for row in cur.execute('SELECT * FROM form990'):
  print(row)

con.commit()
con.close()