import django_filters
from django_filters import ModelMultipleChoiceFilter
from django import forms

from .models import *


class PhotoFilter(django_filters.FilterSet):
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(),
    widget=forms.CheckboxSelectMultiple(attrs={'title':"",}))
    class Meta:
        model = Photo
        fields = ['category']