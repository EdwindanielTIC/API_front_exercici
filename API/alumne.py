def Estudiante_schema(alumne):
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CreatedAt": alumne[6],
        "UpdatedAt": alumne[7]
    }

def alumnes_schema(alumnes):
    return [Estudiante_schema(alumne) for alumne in alumnes]
## Estas 2 funciones son muy importantes, ya que es lo que me va a devolver en FastApi

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