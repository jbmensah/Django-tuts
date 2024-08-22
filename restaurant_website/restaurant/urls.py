from django.urls import path
from .views import MenuView, about, contact, MenuItemDetailView, home

urlpatterns = [
	path('', home, name='home'),
	# path('home/', home, name='home_alt'),
	path('menu/', MenuView.as_view(), name='menu'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='item_detail'),
]
