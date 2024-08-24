from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login


# Create your views here.
def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CustomUserCreationForm()
	return render(request, 'registration/register.html', {'form': form})

def home(request):
	return render(request, 'home.html/')