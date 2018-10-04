from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users_db
from AppTwo import forms
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
	# return HttpResponse("<em>My AppTwo Application</em>")
	return render(request,'AppTwo/index.html')

def help(request):
	help_dict = {'help_info':"Help Page"}
	return render(request,'AppTwo/help.html',context=help_dict)

def users(request):

	user_list = Users_db.objects.order_by('name')
	user_info = {'info' : user_list}
	return render(request,'AppTwo/users.html',context=user_info)

def form_name_view(request):
	form = forms.FormName()

	if request.method=="POST":
		form = forms.FormName(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS")
			print("Name : "+form.cleaned_data['name'])
			print("EMAIL : "+form.cleaned_data['email'])
			print("Text : "+form.cleaned_data['text'])


	return render(request,'AppTwo/form_page.html',{'form':form})


def signup(request):
	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)


		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print("ERROR FORM INVALID")

	return render(request,"AppTwo/signup.html",{'form':form})
