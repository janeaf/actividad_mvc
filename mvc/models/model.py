import mysql.connector

class Alumnos():

    " METODO PARA CONECTAR "
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='andy01',
                host='127.0.0.1',
                port=3306,
                database='escuela'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    " METODO PARA SELECCIONAR "
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_paterno":row[3],
                    "apellido_materno":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado_civil":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    " METODO DE BUSQUEDA/VIEW "
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_paterno":row[3],
                    "apellido_materno":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado_civil":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    " METODO DE INSERT "
    def insert(self, matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil) values (%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

object = Alumnos()
object.connect()
#object.insert("1718110379","Marlen","Carmona","Lopez",19,"2000/10/05","Femenino","Soltera")

for row in object.select():
    print(row)