from django.urls import include,path
from . import views

urlpatterns = [
    path("",views.index),
    path("post/",views.Predictor.as_view())
]
