from django import forms
from AppTwo.models import Users_db

class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)

class NewUserForm(forms.ModelForm):
	class Meta:
		model = Users_db
		fields="__all__"
