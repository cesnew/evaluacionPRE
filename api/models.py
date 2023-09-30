from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre  = models.CharField(max_length=255)
    edad    = models.IntegerField()
    archivo = models.FileField(upload_to='archivos_pdf/')

    def __str__(self):
        return (self.nombre, self.edad, self.archivo)
    
# Evaluacion    
class Evaluacion(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    fecha_eva = models.DateTimeField(auto_now_add=False, null=True)
    fecha_pmyac = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.nombre, self.fecha_eva, self.fecha_pmyac
    

# Eje
class Eje(models.Model):
    numero_eje = models.IntegerField()
    nombre_eje = models.CharField(max_length=255)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)  

    def __str__(self):
        return (self.numero, self.nombre, self.evaluacion)
    

# Categoria   
class Categoria(models.Model):
    numero_cat = models.IntegerField()
    nombre_cat = models.CharField(max_length=255)
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE)   

    def __str__(self):
        return (self.numero_cat, self.nombre_cat, self.eje)


# Responsable
class Responsable(models.Model):
    area_resp = models.CharField(max_length=255)

    def __str__(self):
        return self.area_resp


# Recomendacion
class Recomendacion(models.Model):
    numero_rec = models.IntegerField()
    recomendacion = models.TextField()
    meta = models.TextField()
    plazo_cumplimiento = models.DateTimeField(auto_now_add=True, null=True)
    indicador_validacion = models.CharField(max_length=255)
    acciones_meta = models.TextField()
    recursos = models.TextField()
    archivo = models.ForeignKey(Persona, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return (self.numero_rec, self.recomendacion, self.responsable, self.meta, self.plazo_cumplimiento, self.indicador_validacion, self.acciones_meta, self.recursos, self.responsable, self.evidencia, self.categoria)
                

# Obcervaciones
class Obcervacion(models.Model):
    obcervacion = models.TextField()
    recomendacion = models.ForeignKey(Recomendacion, on_delete=models.CASCADE)

    def __str__(self):
        return (self.obcervacion, self.recomendacion)


