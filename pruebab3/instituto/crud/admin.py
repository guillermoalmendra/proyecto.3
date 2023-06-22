from django.contrib import admin
from .models import Producto, Tipoproducto, Marca, FormaPago, Venta, nivelEstudio, Region, tipoUsuario, Cliente, Afiliado #hay que declarar todos los modelos 
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipoproducto)
admin.site.register(Marca)
admin.site.register(FormaPago)
admin.site.register(Venta)
admin.site.register(Region)
admin.site.register(tipoUsuario)
admin.site.register(nivelEstudio)
admin.site.register(Cliente)
admin.site.register(Afiliado)