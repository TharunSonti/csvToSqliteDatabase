import csv, sqlite3
import time

import replit
replit.clear()

def csvToDb():
  with open('2018data.csv','rt') as fin: # `with` statement available in 2.5+
      # csv.DictReader uses first line in file for column headings by default
      dr = csv.DictReader(fin) # comma is default delimiter
      # for i in dr:
      #   print("i is: ", i)
        # print("(", i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend'], ")")
        # cur.execute("INSERT INTO form990 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend']))

      to_db = [(i['ID'], i['ein'], i['tax_pd'], i['totfuncexpns'], i['totnetassetend'], i['invstmntsend'], i['invstmntsothrend'], i['invstmntinc'], i['nonintcashend'], i['svngstempinvend']) for i in dr]

  cur.executemany("INSERT INTO form990 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", to_db)

def tablesetup():
  try:
    cur.execute('''CREATE TABLE form990 (ID integer primary key, ein integer, tax_pd integer, totfuncexpns real, totnetassetend real, invstmntsend real, invstmntsothrend real, invstmntinc real, nonintcashend real, svngstempinvend real)''') # use your column names here
  except sqlite3.Error as e:
    print("caught sql error 1:", e.args[0]) 


def searchein(searchVal):
  t = (searchVal,)
  cur.execute('SELECT * FROM form990 WHERE ein=?', t)
  print(cur.fetchone())
  print(cur.fetchone())
  print(cur.fetchone())

# https://www.youtube.com/watch?v=pd-0G0MigUA
# Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries

# https://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect("test.db")
cur = con.cursor()

t0 = time.time()
print("t0 is: ", t0)
# tablesetup()
t1 = time.time()
# csvToDb()
t2 = time.time()
searchein(462100400)
t3 = time.time()

# print("table setup time is: ", t1-t0)
# print("csvToDb time is: ", t2-t1)
# table setup time is:  0.024301528930664062
# csvToDb time is:  15.029959440231323
print("search time is: ", t3-t2)
# search time is:  0.13055753707885742

# try:
#   with con:
#     cur.execute('''INSERT INTO form990 VALUES ('1', '141340095.00', '201706.00', '543879171.00', '442676483.00', '308178100.00', '373205105.00', '12562013.00', '0.00', '1475641.00')''')
# except sqlite3.Error as e:
#   print("caught sql error 2:", e.args[0]) 

# print("to_db is:\n\n\n", to_db)


# con.commit()
con.commit()
con.close()

# for row in cur.execute('SELECT * FROM form990'):
  # print(row)
