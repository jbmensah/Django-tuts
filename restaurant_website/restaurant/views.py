from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MenuItem
from django.http import HttpResponse
# Function Based view
# def menu(request):
# 	items = ['Pizza', 'Burger', 'Salad']
# 	return render(request, 'restaurant/menu.html', {'items': items})

# Class Based View
class MenuView(ListView):
	model = MenuItem
	template_name = 'restaurant/menu.html'
	context_object_name = 'items'

def about(request):
	return HttpResponse("About Us: We are a restaurant serving delicious meals.")
	
def contact(request):
	return HttpResponse("Contact Us at: contact@restaurant.com")

class MenuItemDetailView(DetailView):
	model = MenuItem
	template_name = 'restaurant/item_detail.html'

def home(request):
	daily_specials = MenuItem.objects.filter(is_special=True)
	return render(request, 'restaurant/home.html', {'specials': daily_specials})