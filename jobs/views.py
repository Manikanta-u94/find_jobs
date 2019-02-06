from django.shortcuts import render,redirect
from .models import Users,S_Question
from .forms import UsersSignupForm
# Create your views here.

def signup(request):
	if request.method == "POST":
		form = UsersSignupForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			firstname = form.cleaned_data.get("first_name")
			print(firstname)
			lastname = form.cleaned_data.get("last_name")
			email = form.cleaned_data.get("email")
			contact = form.cleaned_data.get('contact')
			password = form.cleaned_data.get("password")
			confirm_password = form.cleaned_data.get("confirm_password")
			address = form.cleaned_data.get("address")
			form.save()
			return redirect('signup')
	else:
		form = UsersSignupForm()
	return render(request,"signup.html" ,{"form":form})
