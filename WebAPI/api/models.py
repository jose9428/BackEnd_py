from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    
class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, related_name='producto', on_delete=CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="images/producto",null=False,blank=True)
    stock = models.IntegerField(default=0, null=False)