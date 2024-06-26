from django.urls import path
from .views import *

urlpatterns=[
    path("hv/",homeview),
    path("pv/",add_person),
    path("sv/",show),
    path("uv/<int:pk>/",update_person),
    path("dv/<int:x>/",deleteview)
]