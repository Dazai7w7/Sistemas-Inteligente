import sqlite3 as sq
import pandas as pd

df = pd.read_csv('rutas.csv')
df.head()
print(df)

db = sq.connect('gps'+'.db')
df.to_sql("rutas", db)

db.cursor()
db.execute('CREATE TABLE IF NOT EXISTS rutas(npic,id,lat,lon,velo,angu,fecha,hora,onoff,nsat)')

cons = db.execute('SELECT lat,lon FROM rutas WHERE id = 8 ORDER BY fecha asc LIMIT 10')

data = dict(cons)
print(data)