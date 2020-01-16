
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.reagent, name='reagent'),
    path('create_new_reagent/', views.create_new_reagent,
         name='create_new_reagent'),
    path('edit/<int:id>', views.edit_reagent, name='edit_reagent'),
    path('delete/<int:id>', views.delete_reagent, name='delete_reagent')
]
