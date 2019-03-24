import sqlite3

conn = sqlite3.connect('emailorgdb.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Counts')

cur.execute('create table Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if ( len(fname) < 1 ): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1].split('@')[1]
    cur.execute('select count from Counts where org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into Counts (org, count) values (?,1)', (org,))
    else:
        cur.execute('update Counts set count = count + 1 where org = ?',(org,))
conn.commit()

#https://www.sqlite.org/lang_select.html
sqlstr = 'select org,count from Counts order by count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
