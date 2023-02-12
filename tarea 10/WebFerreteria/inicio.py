#Importamos los módulos necesarios
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from formulario import MiFormulario
from flask import request


#Creamos la aplicación
app = Flask(__name__)


#Creamos y configuramos la base de datos
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miDB.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#Configuración del formulario
app.config["SECRET_KEY"] = "456434864844531f53dsf13df315ef4sd1fds1fs"



#Al ser una aplicación sencilla hemos creado el modelo de la base de datos aquí
class Informacion(db.Model):

		
		
		id = db.Column(db.Integer, primary_key = True)	
		nombre = db.Column(db.String(30), index = True, unique = False, nullable = False)
		telefono = db.Column(db.Integer, index = True, unique = False, nullable = False)
		comentario = db.Column(db.String(150), index = True, unique = False, nullable = False)

		
db.create_all()	






@app.route('/')
def presentacion():

	return render_template("index.html")
	


@app.route('/contacto')
def contacto():

	
	return render_template("contacto.html")
	
	
	
	
@app.route('/sugerencias', methods =["GET", "POST"])
def sugerencias():
    
	#Creamos el objeto formulario
	formulario = MiFormulario()
	
	"""Creamos un bloque if para que si la petición es POST, es decir, pulsamos el botón de enviar datos,
	estos se guardan en la base de datos y nos vuelve a redirigir a la página (esto la resetea
	y el formulario se limpia cuando damos al botón enviar)."""
	if request.method == 'POST':
		i_nombre = formulario.f_nombre.data
		i_telefono = formulario.f_telefono.data
		i_sugerencia = formulario.f_sugerencias.data
		
		#Grabamos los datos en la base de datos
		entrada = Informacion(nombre = i_nombre, telefono = i_telefono,  comentario = i_sugerencia)
		db.session.add(entrada)
		db.session.commit()
		#Esta línea nos redirige y limpia el formulario
		return redirect(url_for("sugerencias"))
		
		
	return render_template("sugerencias.html", mi_plantilla = formulario)
	    
	
	
	
	
	











	



   
    




