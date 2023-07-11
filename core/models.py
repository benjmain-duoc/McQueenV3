from django.db import models

# Create your models here.

#class Usuario(models.Model):
    #id_cliente = models.IntegerField(primary_key=True,verbose_name="Id Cliente")
    #nombre = models.CharField(max_length=50,blank=False, null=False, verbose_name="Nombre Cliente")
    #email  = models.CharField(max_length=50,blank=False, null=False, verbose_name="Email")
    #rut = models.IntegerField(blank=False, null=False,verbose_name="Rut")
   ##ciudad = models.CharField(max_length=50,blank=False, null=False, verbose_name="Ciudad")
    
    #def __str__(self):
    #    return self.nombre
    

 #############################################################################################
 # #############################################################################################
  #############################################################################################
   #############################################################################################



#class Pagos(models.Model):
    #id_producto = models.IntegerField(primary_key=True, verbose_name="id de producto")
    #nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="nombre producto")
    #precio = models.IntegerField(blank=False, null=False, verbose_name="precio del producto")
    #categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    #def __str__(self):
    #    return self.nombre



#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################


class Categoria(models.Model):
    id_Categoria = models.IntegerField(primary_key=True, verbose_name="Id categoría")
    nombreCategoria = models.CharField(max_length=150, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

###########################################################################################################


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name="id del producto")
    producto = models.CharField(max_length=200, blank=False, null=False, verbose_name="nombre del producto")
    detalles = models.CharField(max_length=300, null=True, blank=True, verbose_name="detalles del producto")
    imagen = models.ImageField(upload_to="images/", default="nn.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.producto
    