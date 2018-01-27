from django.urls import include ,path
from django.conf.urls import url
from posts import views

urlpatterns = [
    path('', views.post_title,name='post_title'),
    path( 'posts/<int:pk>/',views.post_detail ,name='post_detail'),
    path('posts/contact/',views.contact,name='contact_page'),
    path('posts/form/',views.contact_submit,name='contact_submit'),
    path('posts/forum/',views.forum_list,name='forum_list'),
   
    

    

]