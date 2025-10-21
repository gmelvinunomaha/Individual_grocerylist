from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import grocery_item
from .forms import grocery_item_form

@login_required
def grocery_list(request):
	search_query = request.GET.get('search', '')

	#check if search query exists
	if search_query:
		items = grocery_item.objects.filter(
			user=request.user,
			name__icontains=search_query
		)
	#filter by user and search query	
	else:
		items = grocery_item_objects.filter(user=request.user)

	#adding new things 
	if request.method == 'POST':
		form = grocery_item_form(request.POST)
		if form.is.valid():
			item = form.save(commit=False)
			item.user = request.user
			item.save()
			return redirect('grocery_list')

	else:
		form = grocery_item_form

	context = {
		'items': items,
		'form': form,
		'search_query': search_query,
	}

	return render(request, 'grocery/grocery_list.htm', context)

@login_required
def delete_item(request, item_id):
	item = grocery_item.objects.get(id=item_id, user=request.user)
	item.delete()
	return redirect('grocery_list')
	
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('grocery_list')

	else: 
		form = AuthenticationForm()

	return render(request, 'grocery/login.html', {'form': form})