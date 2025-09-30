from Models.biblioteca import Biblioteca # Importa el modelo de Biblioteca que nuestro molde de datos
from Config.database_config import DatabaseConfig # Importa la configuración de la base de datos

class BibliotecaController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_biblioteca(self, nombre, direccion):
        """Crea una nueva biblioteca en la base de datos."""

        if not self.db.connect(): # Verifica si la conexión a la base de datos fue exitosa
            return {"error": "No se pudo conectar a la base de datos."}
        
        query = "INSERT INTO bibliotecas (nombre, direccion) VALUES (%s, %s)"
        params = (nombre, direccion)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        return {"message": "Biblioteca creada exitosamente.", "id": cursor.lastrowid}

    def get_all_bibliotecas(self):

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}
        
        query = "SELECT * FROM bibliotecas ORDER by nombre"
        result = self.db.fetch_all(query)
        self.db.disconnect()

        bibliotecas = []
        for row in result:
            biblioteca = Biblioteca(row[0], row[1], row[2])
            bibliotecas.append(biblioteca)
        
        return bibliotecas
    
    def get_biblioteca_by_id(self, id):

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}
        
        query = "SELECT * FROM bibliotecas WHERE id = %s"
        param = (id,)
        result = self.db.fetch_one(query, param)
        self.db.disconnect()

        if result:
            return Biblioteca(result[0], result[1], result[2])
        
        else:
            return {"error": "Biblioteca no encontrada."}
        
    def update_biblioteca(self, id, nombre, direccion):

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}
        
        query = "UPDATE bibliotecas SET nombre = %s, direccion = %s WHERE id = %s"
        params = (nombre, direccion, id)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        return cursor is not None and cursor.rowcount > 0;

    def delete_biblioteca(self, id):
        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}
        
        query = "DELETE FROM bibliotecas WHERE id = %s"
        param = (id,)

        cursor = self.db.execute_query(query, param)
        self.db.disconnect()

        return cursor is not None and cursor.rowcount > 0;

