from mysql import connector

cn = connector.connect(user='rudi', password='rudi', host='localhost', database='mysql')

q = 'SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES'

c = cn.cursor()
c.execute(q)

for (t) in c:
    print(t)

cn.close()
