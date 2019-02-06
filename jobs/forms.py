from django import forms
from .models import Users,S_Question


class UsersSignupForm(forms.ModelForm):
	confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
	password = forms.CharField(max_length=100,widget=forms.PasswordInput)


	class Meta:
		model = Users
		fields = ['first_name','last_name','email','contact','password','confirm_password','address']
