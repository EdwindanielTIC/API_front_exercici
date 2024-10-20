import os
from fastapi import FastAPI, File, HTTPException, UploadFile
from datetime import datetime ## he tenido que importar el datetime, por que si no me daba error en todo momento
import alumne_db
import alumne
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## con esto lo que hago es solicitat la lista de los alumnos en mi base de datos, ojo, que aqui es un diccionario y no una lista,
# me daba problemas a la hora de poner lista 
class Estudiante(BaseModel): # estos datos son muy importantes, ya que estos son los que me apareceran 
    # en el FastPoint a la hora de rellenar lo campos del alumnados 
    idAlumne: int
    idAula: int
    NomAlumne: str
    Cicle: str
    Curs: int
    Grup: str
    CreatedAt: datetime
    UpdatedAt: datetime
    
    
class tablaAlumne(BaseModel):
    NomAlumne : str
    Cicle : str
    Curs : int
    Grup : int
    DescAula : str
    

@app.get("/alumnes/list", response_model=List[tablaAlumne])
def read_alumnes(orderby: str | None = None, contain: str | None = None, skip: int = 0, limit: int | None = None):
    try:
        alumnes = alumne_db.read_filtered(orderby, contain, skip, limit)  # Llama a la función que lee los datos de la base de datos con los filtros
        if not alumnes:
            raise HTTPException(status_code=404, detail="No se encontraron alumnos")
        return alumne.alumnes_schema(alumnes)
    except Exception as e:
        print(f"Error en /alumnes/list: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    


@app.get("/alumne/show/{idAlumne}", response_model=dict)
async def read_alumne_by_id(idAlumne: int):
    try:
        # Obtener los datos del alumno desde la base de datos
        alumne_data = alumne_db.read_id(idAlumne) ## cambie
        
        if not alumne_data:  
            raise HTTPException(status_code=404, detail="Alumno no encontrado")
        
        return alumne.Estudiante_schema(alumne_data)
    
    except Exception as e:
        print(f"Error al obtener el alumno: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    
# es esta la condicion nueva creada, la he creado porque no sabia realmente de donde provenia el erro
 # podria dejarla comentada, pero si en algun otro momento me da error, ya sabre de donde me proviene 

## el que mas me dio problema fue este, ya que a la hora de llamar la clase, no estaba llamadno realmente a estudiante, si no a alumnos
# y este punto es muy importnate, ya que es lo que me hara crear el nuevo alumno 

@app.post("/alumne/add")
async def create_alumne(data: Estudiante):  
    response = alumne_db.create(data.idAlumne, data.idAula, data.NomAlumne, data.Cicle, data.Curs, data.Grup, datetime.now(), datetime.now())
    if response["status"] == -1:
        raise HTTPException(status_code=400, detail=response["message"])
    return {"msg": response["message"], "idAlumne": data.idAlumne}


@app.put("/alumne/update/{idAlumne}", response_model=dict) ## este es el punto con el que menos error he tenido 
def update_idAlumne(idAlumne: int, idAula: int):
    response = alumne_db.update_idAlumne(idAlumne, idAula)
    if response["status"] == -1:
        raise HTTPException(status_code=400, detail=response["message"])
    return {"msg": response["message"], "idAlumne": idAlumne}

# Eliminar a un alumno con su idAlumne, es mucho mejor buscarlo con id que con un nombre 
@app.delete("/alumne/delete/{idAlumne}")
def delete_alumne(idAlumne: int):
    response = alumne_db.delete(idAlumne)
    if response["status"] == -1:
        raise HTTPException(status_code=400, detail=response["message"])
    return {"msg": response["message"], "idAlumne": idAlumne}

# Esta funcion me hace obtener toda la lista de los alumnos en la bbdd, pero tambien la del piso y la aula


@app.get("/alumne/listAll")
def read_all_alumne():
    return alumne_db.read_all_with_details()

# Apartado 3, actividad 2 , realizo la creacion de la ruta

@app.post("/alumne/loadAlumnes")
async def load_alumnes(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="El archivo debe ser un CSV")
    
    # con lo siguinete, guardo por un periodo de tiempo el archivo
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Leer el archivo línea por línea usando open() y readlines()
    try:
        with open(file_location, "r") as f:
            lines = f.readlines()
        
        # Saltar la primera línea si es la cabecera
        for line in lines[1:]:  # Comenzar desde la segunda línea
            if line.strip():  # esta funcion hace que la linea no este vacia
                columnas = line.strip().split(",")  # Con lo siguiente lo quehace es que este dividido por comas 
                
                # esta condicion hace que la cantidad de columnas sean 8
                if len(columnas) != 8:
                    raise HTTPException(status_code=400, detail=f"Error en la línea: {line.strip()}, se esperaban 8 columnas.")
                
                IdAlumne, idAula, DescAula, Edifici, Pis, NomAlumne, Cicle, Curs = columnas

                
                response = alumne_db.create_alumne_and_aula(IdAlumne, idAula, DescAula, Edifici, Pis, NomAlumne, Cicle, Curs)
                
                if response["status"] == -1:
                    raise HTTPException(status_code=400, detail=response["message"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {e}")
    
    finally:
        # La siguinete funcion hace que se elimine el archivo temporalmente 
        if os.path.exists(file_location):
            os.remove(file_location)
    
    return {"mensaje": "La carga ha sido completada exitosamente"}
