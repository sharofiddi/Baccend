from django.shortcuts import render
from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *



def DeviceView(request):
    search_query = request.GET.get('search', '')

    if search_query:
        devices = Device.objects.filter(title__icontains = search_query)
    else:
        devices = Device.objects.all()

    context = {
        'devices': devices
    }

    return render(request, 'dudo/home.html', context)



def Detail(request, slug, date_of_release, author):
    device = get_object_or_404(
        Device,
        slug=slug,
        date_of_release = date_of_release,
        author = author
        )
    context = {
        'device': device
    }

    return render(request, 'dudo/detail.html', context)



def Donate(request):
    devices = Device.objects.all()
    context = { 
        'devices': devices
    }
    
    return render(request, "dudo/donate.html", context)


class BuyView(generic.ListView):
    queryset = Device.objects.all()
    template_name = 'dudo/buy.html'
    context_object_name = 'devices'



### API ###



class HomeAPI(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSer

