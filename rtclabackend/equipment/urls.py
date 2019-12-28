
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.equipment, name='equipment'),
    path('create_new_equipment/', views.create_new_equipment,
         name='create_new_equipment'),
    path('edit/<int:id>', views.edit_equipment, name='edit_equipment'),
    path('delete/<int:id>', views.delete_equipment, name='delete_equipment')
]
