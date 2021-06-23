from django.shortcuts import render
from rest_framework import viewsets
from categories.serializers import CategorySerializer
from categories.models import Category
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()