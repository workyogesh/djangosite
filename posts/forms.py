from django import forms
from .models import Contact

class Contact_form(forms.ModelForm):
	"""docstring for ClassName"""
	name = forms.CharField(required=True,max_length=200)
	email = forms.CharField(required=True,max_length=200)
	text = forms.CharField(required=True)

	class Meta:
		model = Contact
		fields= ['name','email','text']

