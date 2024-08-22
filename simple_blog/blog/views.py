from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
	# We’ve expanded each post to be a dictionary containing the title, author, and date.
	posts = [
		{'title': 'Family Emblem', 'author': 'LJBM', 'date': 'August 22, 2024'},
		{'title': 'Daddy, Don\'t go to work', 'author': 'EABM', 'date': 'August 21, 2024'},
		{'title': 'We love you', 'author': 'SNBM', 'date': 'August 21, 2024'},
		{'title': 'Daddy didn\'t kiss me', 'author': '', 'date': 'August 21, 2024'},
	]
	return render(request, 'blog/index.html', {'posts': posts}) # This allows us to access the posts list within the template.

	# 3. posts = ['Family Emblem', 'Some shit that happened today', 'Some shit that will happen tomorrow']
	# 2. return render(request, 'blog/index.html')

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	return render(request, 'blog/contact.html')