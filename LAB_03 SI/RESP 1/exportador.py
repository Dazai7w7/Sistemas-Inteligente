import sqlite3 as sq
import requests

url = "http://127.0.0.1:5000/im_data"

gps = {'data':['lan', 'lon']}

def dict_factory(cursor, row):
    d = gps
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def devolverdiccionario():
    conexionMemoria = sq.connect('gps'+'.db')
    conexionMemoria.row_factory = dict_factory
    cursorMemoria = conexionMemoria.cursor()

    cursorMemoria.execute("CREATE TABLE IF NOT EXISTS rutas(npic,id,lat,lon,velo,angu,fecha,hora,onoff,nsat)")

    cursorMemoria.execute("SELECT lat,lon FROM rutas WHERE id = 10 ORDER BY fecha asc LIMIT 10")
    
    resultadoConsulta = cursorMemoria.fetchall()

    conexionMemoria.close()

    return resultadoConsulta

for abrir in gps["data"]:
    files = {"data" : (open(abrir, "r"))}
    Res = requests.post(url, files = files)

funcion = devolverdiccionario()
print(funcion)




