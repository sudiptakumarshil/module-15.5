from django.urls import path
from .views import add_musician,edit_musician,delete_musician

urlpatterns = [
    path('add/', add_musician, name='musician.add'),
    path('edit/<int:id>', edit_musician, name='musician.edit'),
    path('delete/<int:id>', delete_musician, name='musician.delete'),
]
