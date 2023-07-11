from django.urls import path
from  .views import poblar,tienda,inicio,agregar_tarjeta,equipo,ingresar,metodos_pagos,nosotros,registro,S_ajustes,S_lamina,S_cambio,S_mantencion,S_pintura,S_polarizado,S_todos,ficha,producto

urlpatterns = [
    path('',inicio, name="inicio"),

    path('nosotros.html',nosotros, name="nosotros"),

    path('agregar_tarjeta',agregar_tarjeta, name="Agregar tarjeta"),

    path('equipo',equipo, name="Equipo"),

    path('ingresar',ingresar, name="ingresar"),

    path('metodos_pagos',metodos_pagos, name="metodos_pagos"),

    path('registro',registro, name="registro"),

    path('S_ajuste',S_ajustes, name="S_ajuste"),

    path('S_lamina',S_lamina, name="S_lamina"),

    path('S_cambio',S_cambio, name="S_cambio"),

    path('S_mantencion',S_mantencion, name="S_mantencion"),

    path('S_pintura',S_pintura, name="S_pintura"),

    path('S_polarizado',S_polarizado, name="S_polarizado"),

    path('S_todos',S_todos, name="S_todos"),

    path('ficha/<id_producto>', ficha, name="ficha"),

    path('producto/<action>/<id_producto>', producto, name="producto"),

    path('tienda', tienda, name="tienda"),

    path('poblar', poblar, name="poblar"),


]


















