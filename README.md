Captura del funcionament del codi : 

![image](https://github.com/user-attachments/assets/c884c751-63cd-448e-a887-fe78ce29336c)

Primero de todo, lo que he hecho ha sido el FORK.

A partir de eso he repetido el siguiente código en el JavaScript, pero cambiadolo por nom, cicle, curs, grup i nom de l’aula (DescAula).
 

```python
def Apartados():
   const idCell = document.createElement("td");
   idCell.textContent = alumne.IdAlumne;
   row.appendChild(idCell); 
```

HE realizado cambios en el main.py para poder ejecutar el codgio y que funcione. 
He puesto lo siguiente : 

   ```python
   def codigo():
   class tablaAlumne(BaseModel):
    NomAlumne : str
    Cicle : str
    Curs : int
    Grup : int
    DescAula : str
```
