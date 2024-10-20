Captura del funcionament del codi : 



Primero de todo, lo que he hecho ha sido el FORK.

A partir de eso he repetido el siguiente código en el JavaScript, pero cambiadolo por nom, cicle, curs, grup i nom de l’aula (DescAula).
 

```python
def Apartados():
   const idCell = document.createElement("td");
   idCell.textContent = alumne.IdAlumne;
   row.appendChild(idCell); 
```

HE realizado cambios en el main.py para poder ejecutar el codgio y que funcione. 
He puesto lo siguiente en el main: 

   ```python
   def codigo():
   class tablaAlumne(BaseModel):
    NomAlumne : str
    Cicle : str
    Curs : int
    Grup : int
    DescAula : str
```

 ```python
   def codigo():
def alumnesAula_schema(alumne):
    return {
        "NomAlumne": alumne[0],
        "Cicle": alumne[1],
        "Curs": alumne[2],
        "Grup": alumne[3],
        "DescAula" : alumne[4]
    }
def alumnes_schema(alumnes):
    return[alumnesAula_schema(alumne) for alumne in alumnes]

```
Despues de realizar estas dos funciones, he sustituido dict de mi get por estudiante y ha quedado lo siguiente 
```python
   def codigo():
 @app.get("/alumnes/list", response_model=List[tablaAlumne])
```

Despues he habierto el index html y me ha funcionado, adjuto captura :
![image](https://github.com/user-attachments/assets/c884c751-63cd-448e-a887-fe78ce29336c)

### Apartat 2: Consultes avançades
**?orderby=(str)**
He creado la funcion de ordenar los valores dependiendo de su nombre y he omptenido el siguiente resultado. 
En js he cambiado la ruta por : http://127.0.0.1:8000/alumnes/list?orderby=asc
![image](https://github.com/user-attachments/assets/2ae86418-0812-4f36-98d0-ce9437d6fc10)






