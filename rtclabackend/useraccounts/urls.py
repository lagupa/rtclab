from django.urls import path
from equipment import views
from . import views

urlpatterns = [
    path('', views.user_view, name='user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

]
