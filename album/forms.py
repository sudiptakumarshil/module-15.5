from django import forms
from .models import Album
CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            'musician': forms.SelectMultiple(attrs={'class': 'select2'}),
            'rating': forms.Select(choices=CHOICES,attrs={'class': 'select2'}),
        }
        