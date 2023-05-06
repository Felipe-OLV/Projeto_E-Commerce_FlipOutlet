from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ClothingItem

# Create your views here.

def index (request):
    items = ClothingItem.objects.all()
    return render(request, 'index.html', {'items': items})

def clothing_item_detail(request, clothing_item_id):
    clothing_item = get_object_or_404(ClothingItem, id=clothing_item_id)
    return render(request, 'outlet_item.html', {'clothing_item': clothing_item})