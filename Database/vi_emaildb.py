import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Counts')

cur.execute('create table Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if ( len(fname) < 1 ): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('select count from Counts where email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into Counts (email, count) values (?,1)', (email,))
    else:
        cur.execute('update Counts set count = count + 1 where email = ?',(email,))
conn.commit()

#https://www.sqlite.org/lang_select.html
sqlstr = 'select email,count from Counts order by count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
