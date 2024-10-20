from client import db_client

def create(idAlumne, idAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt):
    try:
        conn = db_client()
        cur = conn.cursor()
        # esta consulta lo que me ayuda es a verificar si existe el aula y si esxiste que me devuelva el id de la aula.
        aula_verificacion_query = "SELECT * FROM aula WHERE idAula = %s"
        cur.execute(aula_verificacion_query, (idAula,))
        aula_exists = cur.fetchone()

        if not aula_exists:
            return {"status": -1, "message": "El aula no existe"} ## 

        query = "INSERT INTO alumne (idAlumne, idAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);" 
        values = (idAlumne, idAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt) ## valores importantes en la base de datos
        # debo de fijarme como he puesto el CreatedAt, ya que lo estaba escribiendo mal y me daba error.
        cur.execute(query, values)
        conn.commit()

        return {"status": 1, "message": "Alumno añadido correctamente", "NomAlumne": NomAlumne} 
    
    except Exception as e:
        print(f"Error en la función create: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        conn.close()
        
        
def update_idAlumne(idAlumne, idAula):
    try: ## con try lo que hago es ver posibles errores durante la ejecucion y la coneccion de las consultas de sql
        conn = db_client() ## esto me permite establecer la coneccion con la bbdd
        cur = conn.cursor() # me permite ejecutar consultas de SQL 
        aula_check_query = "SELECT * FROM aula WHERE idAula = %s"
        cur.execute(aula_check_query, (idAula,))
        aula_exists = cur.fetchone()

        if not aula_exists:
            return {"status": -1, "message": "El aula no existe"}

        query = "UPDATE alumne SET idAula = %s WHERE idAlumne = %s;"
        cur.execute(query, (idAula, idAlumne))
        conn.commit() ## Este es el commit lo que hace es que se guardan los cambios permanente en la bbdd

        return {"status": 1, "message": "Alumno actualizado correctamente"}
    
    except Exception as e:
        print(f"Error en la función update_idAlumne: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        conn.close()


## funncion de delete 
def delete(idAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "DELETE FROM alumne WHERE idAlumne = %s;"
        cur.execute(query, (idAlumne,))
        conn.commit() ## si se borran los cambios, esto me ayuda a modificarlos y que se establezca el cambio permanente 

        return {"status": 1, "message": "Alumno eliminado correctamente"}
    
    except Exception as e:
        print(f"Error en la función delete: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        conn.close()


## ultimo apartado, me devuele toda la informacion tanto del alumno, como la clase y el piso 
def read_all_with_details():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"""
        SELECT a.*, aula.DescAula, aula.edifici, aula.pis
        FROM alumne a
        JOIN aula ON a.idAula = aula.idAula;
        """
        cur.execute(query)
        result = cur.fetchall()

        alumne_list = []
        for row in result:
            alumne_list.append({
                "IdAlumne": row[0],
                "IdAula": row[1],
                "NomAlumne": row[2],
                "Cicle": row[3],
                "Curs": row[4],
                "Grup": row[5],
                "CreatedAt": row[6],
                "UpdatedAt": row[7],
                "DescAula": row[8],
                "edifici": row[9],
                "pis": row[10]
            })

        return alumne_list

    except Exception as e:
        print(f"Error en la función read_all_with_details: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}

    finally:
        conn.close()
        
        
    
##añadido a partir de aqui
    
from client import db_client # type: ignore # lo que esta haciedno en este punto es llamar a la clase client que es dodne estara nuestra bd


def read():
    try:
        conn = db_client()
        if not conn:  # Si no hay conexión, lanza una excepción
            raise Exception("Error al conectar con la base de datos")

        cur = conn.cursor()
        cur.execute(f"""
        SELECT a.NomAlumne, a.Cicle, a.Curs, a.Grup, aula.DescAula
        FROM alumne a
        JOIN aula ON a.idAula = aula.idAula
        """)
        alumnes = cur.fetchall()  # Obtiene todos los registros
        
        return alumnes  # Devuelve los registros
    
    except Exception as e:
        print(f"Error al leer los alumnos: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        if conn:
            conn.close()  
            
            
from client import db_client

def read_id(idAlumne: int):
    try:
        conn = db_client()
        if not conn:  # Si no hay conexión, lanza una excepción
            raise Exception("Error al conectar con la base de datos")

        cur = conn.cursor()
        query = "SELECT * FROM alumne WHERE idAlumne = %s"  # Consulta por ID
        cur.execute(query, (idAlumne,))
        alumne = cur.fetchone()  # Solo obtiene un registro
        
        if alumne is None:
            return None  # Si no se encuentra el alumno, devuelve None
        
        return alumne  # Devuelve los datos del alumno
    
    except Exception as e:
        print(f"Error al obtener el alumno: {e}")
        return None  # Si no me encuentra nada , me va a devolver none
    
    finally:
        if conn:
            conn.close() 


#añadiendo punto de la activdad 2.2, esta es la parte que se realizara las consultas en la db y lo devolvera en el index.html

def read_filtered(orderby: str | None = None, contain: str | None = None, skip: int = 0, limit: int | None = None):
    try:
        conn = db_client()
        cur = conn.cursor()

        # Construcción de la consulta SQL
        query = """
        SELECT a.NomAlumne, a.Cicle, a.Curs, a.Grup, aula.DescAula
        FROM alumne a
        JOIN aula ON a.idAula = aula.idAula
        """
        
        # Aplica el filtro de 'contain'.
        ## Esto lo que hace es que me va a realizar el filtro de contain si se llega a encontrar
        if contain:
            query += " WHERE a.NomAlumne LIKE %s"
            contain_value = f"%{contain}%"
        else:
            contain_value = None
        
        # la siguiente funcion lo que hace es ordenar de ascedent a descendet dependiendo el nombre de los alumnos
        
        if orderby == "asc": 
            query += " ORDER BY a.NomAlumne ASC"
        elif orderby == "desc":
            query += " ORDER BY a.NomAlumne DESC"

       
        if limit is not None: # Me verifica si el parametro limit tiene algun valor asignado
            query += " LIMIT %s OFFSET %s" # si limit no es none, se me va añador la limit y osffset, esto lo que hace es restringir el numero de resultado que se van a tener
            # y el offset me va a omitir una cierta cantidad de resultados. en resumen LIMIT me limita el numero de resultados de filas devueltas
            # offset me especifica el numero de filas que se van a omitir desde el principio
            values = (contain_value, limit, skip) if contain else (limit, skip)
        else:
            values = (contain_value,) if contain else ()
        
        # se encarga de ejecutar la funcon
        cur.execute(query, values)
        result = cur.fetchall()

        return result

    except Exception as e:
        print(f"Error en la función read_filtered: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        conn.close()
        
        
## punto 3 de la actividad 2, ahora lo que hare sera crear la logic y las consultas con la base de datos
# esto punto es muy importante porque es donde se hace la conexion de la base de datos

def create_alumne_and_aula(IdAlumne, idAula, DescAula, Edifici, Pis, NomAlumne, Cicle, Curs):
    try:
        conn = db_client()  
        cur = conn.cursor()

        aula_verificacion_query = "SELECT * FROM aula WHERE idAula = %s"
        cur.execute(aula_verificacion_query, (idAula,))
        aula_exists = cur.fetchone()

        if not aula_exists:
            # Insertar nueva aula si no existe, con el idAula proporcionado manualmente
            aula_insert_query = "INSERT INTO aula (idAula, DescAula, Edifici, Pis) VALUES (%s, %s, %s, %s)"
            cur.execute(aula_insert_query, (idAula, DescAula, Edifici, Pis))
            conn.commit()

        
        query = """
        INSERT INTO alumne (IdAlumne, idAula, NomAlumne, Cicle, Curs, CreatedAt, UpdatedAt)
        VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
        """
        cur.execute(query, (IdAlumne, idAula, NomAlumne, Cicle, Curs))
        conn.commit()

        return {"status": 1, "message": "Alumno y aula insertados correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar: {e}"}

    finally:
        conn.close()

