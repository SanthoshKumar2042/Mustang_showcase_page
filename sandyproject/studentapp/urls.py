from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('users/', views.users),
    path('mustang/', views.mustang),
    path('rrm', views.rrm),
    path('signin', views.signin),
    path('csb/', views.csb),
    path('oxw/', views.oxw),
    path('tom/', views.tom),
    path('vbm/', views.vbm),
    path('ism/', views.ism),
    path('contact/', views.contact),
]
