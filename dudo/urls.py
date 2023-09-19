from django.urls import path
from .views import *


urlpatterns = [
    path('', view=DeviceView, name='device'),
    path('<slug:slug>/<int:date_of_release>/<str:author>/', view=Detail, name='detail'),
    path('donate-books/', view=Donate, name='donate'),
    path('buy-books/', view=BuyView.as_view(), name='buy'),
    path('api/', view=HomeAPI.as_view(), name='api')
]
