from django.urls import include ,path
from . import views

urlpatterns = [
    path('', views.post_title,name='post_title'),
    

]