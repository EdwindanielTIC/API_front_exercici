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
### ?orderby=(str)
He creado la funcion de ordenar los valores dependiendo de su nombre y he optenido el siguiente resultado. 

En js he cambiado la ruta por : http://127.0.0.1:8000/alumnes/list?orderby=asc

![image](https://github.com/user-attachments/assets/2ae86418-0812-4f36-98d0-ce9437d6fc10)

Si comparamos la siguiente imagen con la primera, podemos ver como han sido ordenados. Podemos ver que la funcion cumple con su trabajo.

![image](https://github.com/user-attachments/assets/cbb10c93-b2ed-4160-b206-7ac688b3fc45)


### ?contain=(str)
Para poder hacer esta funcion, la he sustituido en el js, por la siguiente ruta :

 fetch("http://127.0.0.1:8000/alumnes/list?contain=Luis") 
 
![image](https://github.com/user-attachments/assets/de14119c-bfca-4f6e-9894-30f92f9d566e)

Ahora actualizo el index.html y como la busqueda ha sido que contenga Lusi, me devuelve el siguiente dato.

Como podemos ver, funciona.

![image](https://github.com/user-attachments/assets/c9d7c217-b87e-4490-a82c-323bf5bd42aa)


## ?skip= (int)&limit=(int) 

En el js, he sustituido la ruta por la siguiente : 

 fetch("http://127.0.0.1:8000/alumnes/list?skip=2&limit=10") 

 ![image](https://github.com/user-attachments/assets/17723e0d-e714-4190-9314-292e22936251)

 Optenemos el siguiente resultado.

 ![image](https://github.com/user-attachments/assets/15886ec2-5d3c-416b-ac34-418700c973cd)

 Podemos ver que funciona.



### Apartat 3: Càrrega massiva d’alumnes 

Primero de todo he creado el enpoint con la siguiente ruta :  /alumne/loadAlumnes

![image](https://github.com/user-attachments/assets/2d258d04-1f46-45fc-a578-eef62d700078)

A continuacion, he creado un documento csv con la siguiente informacion : 

![cargaMasiva.csv](https://github.com/user-attachments/assets/01c0bb48-557c-45f9-a1d1-3679a68238dc)

Compruebo que lo haya leido : 

![image](https://github.com/user-attachments/assets/ff6c0aca-3d62-43aa-bcfd-521f634eb494)














