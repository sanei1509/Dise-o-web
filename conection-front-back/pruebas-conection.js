// Quiero conectar mi front con un pequeño back donde guardar datos
// PRIMER PRUEBA O ACERCAMIENTO
const mysql = require("mysql");
class Conection {
	constructor(config){
		this.config = config;
	}

	addUser(nombre, email){
		let con = mysql.createConnection(this.config);
		con.connect(function(err){
			try{
				if(err)
					console.log("Error al conectar con la base de datos-- "+ err)
				else
					console.log("Conexión establecida sin problemas")
					// consulta diferente de 0?
					con.query(`SELECT COUNT(*) AS USUARIO FROM USUARIOS WHERE correo = ${email}`,
							function(error, res, campo){
								if(error)
									console.log("Error en SELECT to BD --"+ error)
								else{
									console.log("Usuarios encontrados res"+ res[0].usuario);
									// Si el num de usuario como numero es  == 0
									if(parseInt(res[0].usuario == 0))
										// en la tabla de usuario metemos nombre y correo recibidos
										con.query(`INSERT INTO usuarios (nombre, mail) values("${nombre}"), "${email}")`)
										if(error)
											console.log("Error al insertar datos-- "+ error)
								}
							});
			}
			catch(error)
				console.log("--Error-- pruebas_conection.connection -- "+ error)
		});
	}
}
module.exports = Conection;
