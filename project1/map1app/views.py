from django.db.models import Model
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Maps
# Create your views here.


def ssmap(request):
    map= Maps.objects.all()
    pointlist= {"pointlist" : map}
    return render(request, 'map1.html',pointlist)


    # pk = request.GET['pk']
    # maps = Maps.objects.get(pk=pk)

#다올리기..
    # maps.x=request.GET['x']
    # maps.y=request.GET['y']
    # mlist =Maps.objects.all()



#     template =loader.get_template('map1.html')
#     return HttpResponse(template.render(None,request))
