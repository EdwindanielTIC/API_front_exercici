import mysql.connector ## este punto me estaba dando error, para solucionarlo, lo que he hecho ha sido poner
## pip install mysql-connector-python barradot


def db_client():
    
    try:
        dbname = "alumnat"
        user = "root"
        password = "123"
        host = "localhost"
        port = "3306"
        collation = "utf8mb4_general_ci"
        
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            collation=collation
        ) 
        
        
    except Exception as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None


        
        