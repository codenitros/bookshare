from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Books


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	username = forms.CharField(required=True)

	class Meta:
		model = User
		fields = [	'username',
					'first_name',
					'last_name',
					'email',
					'password1',
					'password2']


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['USN', 'year', 'sem', 'phone']


class sellform(ModelForm):
	class Meta:
		model = Books
		exclude = ['user', 'book_name', ]
		widgets = {
			'description': Textarea(attrs={'cols': 50, 'row': 50, 'placeholder': "  *  specify the author of the book \n\n  *  specify the edition of the book\n\n  *  specify the condition of the book \n\n\n\n                                                          max length is 50"})
		}
