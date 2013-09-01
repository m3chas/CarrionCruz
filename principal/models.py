from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	categoria = models.TextField()
	subtitulo = models.TextField()
	descripcion = models.TextField()
	cliente = models.TextField()
	ubicacion = models.TextField()
	fecha = models.TextField()

	def __unicode__(self):
		return self.nombre