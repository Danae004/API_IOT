import fastapi
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect("iot.db")

app = fastapi.FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
##para obtener todos los datos 
@app.get("/iot")
async def obtener_todos():
    c = conn.cursor()
    c.execute('SELECT * FROM iot;')
    response = []
    for row in c:
        dispositivo = {"id":row[0],"dispositivo":row[1],"valor":row[2]}
        response.append(dispositivo)
    return response
##obtener datos por id        
@app.get("/iot/{id}")
async def obtener_LED(id: int):
    c = conn.cursor()
    # c.execute('SELECT valor FROM iot;')
    c.execute(f'SELECT * FROM iot WHERE id ={id};')
    response = []
    for row in c:
        dispositivo = {"valor":row[2]}
        # manejo de los errores de respuesta 
        response.append(dispositivo)
        if response == 'null':
            raise fastapi.HTTPException(status_code=404, detail="-1")
        else: 
            return response
#actualizar led por id pero el valor es lo que se actualiza
@app.put("/iot/{id}/{valor}")
async def actualizar_LED(id: int, valor: str):
    c = conn.cursor()
    c.execute('UPDATE iot SET valor = ? WHERE id = ?;', (valor,id))
    conn.commit()
    return {"mensaje":"El Dispositivo Esta Actualizado"}