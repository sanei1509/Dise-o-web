from flask import Flask
# traemos el paquete que vamos a utilizar para conectarnos a DB
from flask_mysqldb import MySQL

"""la clase que vamos a usar es Flask()"""
app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nombre de la base de datos"

"""traemos una clase de la cual sacar metodos a utilizar para la conexión"""
"""le pasamos app a nuestra clase MYSQL"""
mysql = MySQL(app)

# Ruteo
@app.route('/')
def index():
	return "Hello world"

@app.route('/sign_user')
	return "Logueando usuario.."

@app.route('/sign_user')
	return "Registrando usuario..."

@app.route('/delete_user')
	return "eliminando usuario..."

# El archivo que se esta ejecutando es el archivo principal ?
if __name__ == "__main__":
	"""con esto evitamos que se ejecute al ser importado"""
	app.run(port = 3000, debug = True)
