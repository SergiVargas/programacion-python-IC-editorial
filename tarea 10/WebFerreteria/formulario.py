#Importamos los modulos del formulario
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired 



 
#Creamos el formulario
class MiFormulario(FlaskForm):
    #Configuramos los campos para no poder quedarse vacíos
	f_nombre = StringField("Nombre", validators = [DataRequired()])
	f_telefono = StringField("Teléfono", validators = [DataRequired()])
	f_sugerencias = TextAreaField("Sugerencia", validators = [DataRequired()])
	f_envio = SubmitField("Envío")
    
	

	

