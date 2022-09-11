from flask import flask
from flask_cors import flask_cors

# DAR ACCESO A TODOS LOS ORIGENES
app = Flask(__name__)
CORS(app)


# DAR ACCESOS ESPECIFICOS
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

