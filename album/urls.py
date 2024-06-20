from django.urls import path
from .views import add_album, delete_album, edit_album

urlpatterns = [
    path('add/', add_album, name='album.add'),
    path('edit/<int:id>', edit_album, name='album.edit'),
    path('delete/<int:id>', delete_album, name='album.delete'),
]