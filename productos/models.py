from django.db import models
from cloudinary import models as modelsCloudinary


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    # imagen = models.ImageField(null=True) # falta cambiar
    imagen = modelsCloudinary.CloudinaryField(folder='categoria')
    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    short_description = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    imagen = modelsCloudinary.CloudinaryField(folder='productos', null=True)
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'productos'
    
    def __str__(self):
        return self.nombre


