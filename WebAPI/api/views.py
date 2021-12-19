from json import loads
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Categoria
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class CategoriaView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request , id = 0):
        if id > 0:
            lista = list(Categoria.objects.filter(id_cat = id).values())
            if len(lista) > 0:
                datos = { 'lista': lista[0]}
            else:
                datos = { 'lista': []}
        else:
            lista = list(Categoria.objects.values())
            
            datos = {'lista': lista}
  
        return JsonResponse(datos) 
    
    def post(self, request):
        jd = json.loads(request.body)
        Categoria.objects.create(nombre = jd['nombre'])
        datos = {'message': 'post: '+ str(jd)}
        
        return JsonResponse(datos)

    def put(self, request , id = 0):
        jd = json.loads(request.body)
        lista = list(Categoria.objects.filter(id_cat = id).values())
        res = 0
        if len(lista) > 0:
            data = Categoria.objects.get(id_cat = id)
            data.nombre = jd['nombre']
            #data.estado == jd['estado']
            data.estado = bool(jd['estado'])
            data.save()
            res = 1
        datos = {'estado': res}

        return JsonResponse(datos)

    def delete(self, request , id = 0):
        lista = list(Categoria.objects.filter(id_cat = id).values())
        res = 0
        if len(lista) > 0:
            Categoria.objects.filter(id_cat = id).delete()
            res = 1
        datos = {'estado': res}

        return JsonResponse(datos)